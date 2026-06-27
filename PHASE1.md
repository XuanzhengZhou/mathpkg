# Phase 1 设计：自动化管道 + 两层证明扩展

> Phase 0 建立了手工原型（21 个概念、依赖解析器、CLI、Lean 编译验证）。
> Phase 1 把管道自动化——从 PDF 到编译通过的 Lean 代码，全程无需人工干预。

---

## 〇、核心洞察：两层管道

**直译教科书 Lean 会失败**，因为数学家写的证明经常跳过步骤：

```
教科书: "The result follows immediately from Theorem 3.2."
                            ↑
                    这是 gap。Agent 不知道"怎么" follows。
```

**解决方案**：在自然语言层面填 gap，再翻译 Lean。

```
层级                    做什么                                    工具
──────────────────────────────────────────────────────────────────────
第0层: 原始教科书    LaTeX 提取/OCR 后的定理 + 简要证明           pdf_extract
第1层: Gap-filling   LLM 把"显然/易证/由此可得"展开为显式步骤     LLM（擅长语言生成）
第2层: Lean 翻译     展开后的详细证明 → Lean 代码                LLM + lake build
第3层: 编译验证      Lean 编译通过/失败                           lake build
第4层: 自愈循环      编译失败 → 读错误 → 修复 → 重编译 (≤20轮)    LLM + lake build
```

### 为什么这样有效

| | 直译教科书 | 两层管道 |
|---|---|---|
| Agent 遇到的 gap 类型 | 数学 gap（"为什么成立？"） | API gap（"函数名是什么？"） |
| LLM 擅长填这类 gap 吗 | ❌ 需要数学创造力 | ✅ 查 API 文档+试错 |
| 编译器错误含义 | 模糊（不知道是 gap 还是语法） | 精确（一定是类型/API 问题） |
| 自愈循环成功率 | 30-50% | **70-85%** |

---

## 一、管道架构

```
┌──────────────────────────────────────────────────────────────┐
│                    Phase 1 自动化管道                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  数字版 PDF                                                  │
│      │                                                       │
│      ▼                                                       │
│  ┌──────────┐     ┌──────────────┐     ┌──────────────┐     │
│  │ PDF → MD │ ──→ │ 概念提取     │ ──→ │ 依赖分析     │     │
│  │pymupdf4llm│     │ LLM (Flash)  │     │ LLM (Flash)  │     │
│  └──────────┘     └──────────────┘     └──────────────┘     │
│                                               │              │
│                                               ▼              │
│                                        ┌──────────────┐     │
│                                        │ Mathlib4 比对 │     │
│                                        │  lean_check   │     │
│                                        └──────────────┘     │
│                                               │              │
│                         ┌─────────────────────┘              │
│                         ▼                                    │
│                  已经声明了 lean=?                           │
│                   complete → 跳到 Lean 翻译                  │
│                   partial/none → 需要写完整证明               │
│                         │                                    │
│     ┌───────────────────┴───────────────────┐               │
│     ▼                                       ▼                │
│  complete 路径                           partial/none 路径   │
│     │                                       │                │
│     │                                       ▼                │
│     │                               ┌──────────────────┐    │
│     │                               │ 第1层: Gap-filling │   │
│     │                               │ 展开所有"显然"     │   │
│     │                               └──────────────────┘    │
│     │                                       │                │
│     ▼                                       ▼                │
│  ┌──────────────────────────────────────────────────┐      │
│  │ 第2层: Lean 翻译                                  │      │
│  │ 详细证明 → LLM (Pro) → Lean 代码                  │      │
│  └──────────────────────────────────────────────────┘      │
│                         │                                    │
│                         ▼                                    │
│                  ┌──────────────┐                           │
│                  │ 第3层: 编译   │                           │
│                  │ lake build    │                           │
│                  └──────────────┘                           │
│                     │         │                              │
│                   ✅ 通过   ❌ 失败                           │
│                     │         │                              │
│                     │         ▼                              │
│                     │   ┌──────────────┐                    │
│                     │   │ 第4层: 自愈   │                    │
│                     │   │ 读错误→修复   │                    │
│                     │   │ (≤20 轮)      │                    │
│                     │   └──────────────┘                    │
│                     │         │                              │
│                     │     ┌───┴───┐                         │
│                     │   ✅ 通过  ❌ 放弃                      │
│                     │     │         │                        │
│                     ▼     ▼         ▼                        │
│                  ┌──────────────────────────┐               │
│                  │ 更新 YAML:                │               │
│                  │   lean_status = complete  │               │
│                  │   或 partial + error_log  │               │
│                  └──────────────────────────┘               │
└──────────────────────────────────────────────────────────────┘
```

---

## 二、第1层 Gap-filling 详解

### 输入/输出

```
输入: 教科书的定理陈述 + 简要证明（含 gap）
  "If N ≤ G and gNg⁻¹ ⊆ N for all g, then N ⊴ G. 
   The proof is straightforward by definition."

输出: 展开的显式证明（每步有已知定理支撑）
  "1. Let N ≤ G.
   2. Assume ∀g∈G, gNg⁻¹ ⊆ N.
   3. By definition (Subgroup.Normal), N ⊴ G iff ∀n∈N, ∀g∈G, gng⁻¹ ∈ N.
   4. Fix n ∈ N and g ∈ G.
   5. Consider g⁻¹ ∈ G. By assumption with g⁻¹: (g⁻¹)N(g⁻¹)⁻¹ ⊆ N.
   6. Since (g⁻¹)⁻¹ = g, we have g⁻¹Ng ⊆ N.
   7. Hence g⁻¹ng ∈ N.
   8. Multiply on left by g and right by g⁻¹: g(g⁻¹ng)g⁻¹ ∈ gNg⁻¹.
   9. Simplify: (gg⁻¹)n(gg⁻¹) = n. Therefore n ∈ gNg⁻¹.
   10. But we need gng⁻¹ ∈ N. This is equivalent to n ∈ g⁻¹Ng (conjugate the condition).
   11. Apply step 6 with g and g⁻¹ swapped: since the assumption holds for all g,
       it holds for g⁻¹, giving gNg⁻¹ ⊆ N.
   12. Wait — we need to show gng⁻¹ ∈ N directly.
       By the assumption with g: gng⁻¹ ∈ gNg⁻¹ ⊆ N. Done. ∎"
```

### LLM Prompt 设计

```python
GAP_FILLING_PROMPT = """
You are a mathematical proof writer. Given a theorem statement and a brief
proof sketch (which may skip steps), expand the proof into EXPLICIT,
NUMBERED steps.

RULES:
1. Every step must reference a specific theorem, lemma, axiom, or definition
2. NEVER use "clearly", "obviously", "it follows that", "one can show"
   — instead, state exactly which fact justifies the step
3. If the original proof says "by Theorem X", expand to show HOW Theorem X applies
4. Write at the level of an undergraduate textbook — a student should be able
   to follow every line without additional reasoning
5. Each step should be ONE logical inference
6. End the proof with "∎"

Theorem: {statement}
Proof sketch: {sketch}

Expanded proof (numbered steps):
"""
```

### 预期效果

| 指标 | 估计值 | 说明 |
|---|---|---|
| gap 覆盖率 | ~90% | 大多数"显然"能被展开 |
| 引入幻觉的概率 | ~5% | LLM 可能填充错误引理 |
| 幻觉被编译器抓住的概率 | ~95% | 错误引理会编译失败 → 自愈 |
| 端到端 gap-filling 可靠性 | ~85% | 编译验证 + 自愈后 |

---

## 三、第2层 Lean 翻译详解

### 输入/输出

```
输入: 展开后的显式证明（自然语言，每步一个推理）
输出: Lean 4 代码（编译通过或进入自愈循环）
```

### LLM Prompt 设计

```python
LEAN_TRANSLATE_PROMPT = """
You are an expert Lean 4 programmer. Translate the following mathematical
proof into Lean 4 code.

CONTEXT:
- Mathlib4 is already imported (`import Mathlib`)
- The proof uses standard group theory concepts
- You should write a `theorem` declaration with a complete proof

RULES:
1. Use Mathlib4 theorem names whenever possible (do NOT reinvent existing lemmas)
2. Use tactics: `apply`, `rcases`, `intro`, `refine`, `simp`, `rw`, `exact`
3. If stuck, use `have` to state intermediate goals
4. Write clean, readable Lean code with proper indentation
5. If the theorem is already in Mathlib4, reference it with `#check` in comments

Theorem statement: {statement}
Expanded proof: {expanded_proof}

Lean code:
"""
```

---

## 四、第3+4层：编译 + 自愈循环

```python
def lean_self_heal(filepath: str, theorem_name: str, max_rounds: int = 20) -> LeanResult:
    """
    编译 Lean 文件，如果失败则让 LLM 看错误并修复。
    最多 max_rounds 轮。
    """
    
    for round in range(max_rounds):
        # Compile
        proc = subprocess.run(
            ["lake", "build"], cwd=LEAN_PROJECT_DIR,
            capture_output=True, text=True, timeout=120
        )
        
        if proc.returncode == 0:
            return LeanResult(success=True, rounds=round+1)
        
        # Parse errors (file, line, message)
        errors = []
        for line in proc.stderr.split('\n'):
            if 'error:' in line:
                errors.append(line.strip())
        
        if round == max_rounds - 1:
            break
        
        # Let LLM fix errors
        prompt = f"""
        Lean compilation failed with {len(errors)} errors:
        
        {chr(10).join(errors[:10])}
        
        Fix the file at {filepath}. Read it, correct ALL errors, and write the corrected version.
        Use the Write tool.
        """
        
        agent(prompt, schema=None)
    
    return LeanResult(success=False, rounds=max_rounds, errors=errors)
```

---

## 五、管道适用范围

### Phase 1 目标（5 本代数教材，~200 个概念）

| 概念类型 | 数量（估） | 路径 | 预估成功率 |
|---|---|---|---|
| 定义 | ~120 | 直接翻译 | 95% |
| Mathlib4 已有定理 | ~40 | `#check` + example | 98% |
| 需要 gap-filling 的定理 | ~30 | 两层管道 | 75% |
| 需要大量基础设施的定理 | ~10 | 标记为 partial | N/A |

### Phase 1 之后

- 200 个概念中预计 **~170 个 Lean 验证通过**
- ~20 个因 Mathlib4 基础设施不足标记为 partial
- ~10 个因证明太复杂/LLM 无法填充 gap 标记为 partial

---

## 六、与 Phase 0 成果的整合

Phase 0 产出 → Phase 1 如何使用：

| Phase 0 产出 | Phase 1 用途 |
|---|---|
| 21 个手工 YAML | 作为自动化管道的 "gold standard" 验证集 |
| `mathpkg/graph/concept.py` | 自动化管道的目标格式 |
| `mathpkg/pipeline/lean_check.py` | 第0步：Mathlib4 覆盖比对 |
| `lean/MathPkg/Verification.lean` | 编译验证的参照模板 |
| `cmd/math` CLI | `math verify --auto` 自动化验证入口 |
| `mathpkg/resolver/solver.py` | 决定处理顺序（依赖树叶子优先） |

---

## 七、里程碑

### Phase 1a: 单概念管道验证（2天）
- [ ] 实现 `expand_proof()` + `translate_lean()` + `self_heal()`
- [ ] 用 Day 1 的 21 个手工 YAML 做验证集
- [ ] 跑通 Lagrange 定理的完整管道（PDF → MD → YAML → Lean → ✅）
- [ ] 统计自动化成功率

### Phase 1b: 5 本书批量处理（3天）
- [ ] PDF → Markdown: 5 本代数方向的 GTM 教材
- [ ] 概念提取 + 依赖分析: LLM 自动生成 ~200 个 YAML
- [ ] Gap-filling + Lean 翻译: 全自动管道
- [ ] 统计: 编译通过率、每概念平均轮数、每概念 API 费用

### Phase 1c: 品质提升 + 文档（2天）
- [ ] 人工抽查 20 个自动生成的 Lean 证明
- [ ] 写 "严谨度评分" 脚本（每本书的形式化成功率）
- [ ] 更新 CLI + 文档
