# mathpkg — 完整工作交接文档

> 2026-06-24 · 10 个 Per-Chapter Workflow 运行中 · ¥7,000 预算

---

## 快速上手 — 怎么看这个项目

| 想了解什么 | 去看 |
|---|---|
| 项目全貌 + 进度 | 本文件 `HANDOVER.md` |
| 当前技术细节 | `CLAUDE.md` |
| 所有记忆索引 | `~/.claude/projects/-home-a123----Springer-Math-Textbooks/memory/MEMORY.md` |
| V7 概念格式最终规范 | `memory/concept-v7-spec.md` |
| V7 Pipeline 规格 | `memory/pipeline-v4-spec.md` |
| OCR 运行状态 | `/home/a123/文档/code/Model agent/glm_ocr_books_run.log` |
| Section 拆分输出 (推荐) | `/home/a123/文档/mathpkg/pipeline_output/stitched_sections/` |
| Chapter 拆分输出 (回退) | `/home/a123/文档/mathpkg/pipeline_output/stitched_v2/` |
| Section 分析结果 | `memory/section-strategy.md` |
| 工作流脚本 | `/home/a123/文档/mathpkg/workflows/` |

---

## 一、项目核心设计 (V7，最终版)

### 概念格式：一个文件夹 = 一个概念

```
concepts/algebra/group-theory/lagrange-theorem/
├── concept.yaml        ← 元数据 (id, type, deps, source_books)
├── theorem.tex         ← 纯 LaTeX 数学陈述，零自然语言
├── introduce.en.md     ← 英文导读 (换语言只换这个文件)
├── proof_gtm-0073_I.4_coset-partition.en.md  ← 每本书一个证明文件
├── exercise_gtm-0073_I.4.8.en.md             ← 每道习题一个文件
└── verify.lean         ← Lean 4 形式化验证
```

### 核心原则

1. **文件系统是真理，SQLite 是缓存** (graph.db = pkgCache)
2. **每章一个 Agent，不是每本书一个 Agent** (关键教训！)
3. **Slug = 语义英文** (kummers-theorem ✓, gtm006-thm-4-6 ✗)
4. **theorem.tex = 纯 LaTeX 陈述**，无证明、无自然语言
5. **source_books = 对象数组**，不是字符串数组
6. **两阶段依赖**：先提取后消解 (resolve_deps.py)

### Pipeline 完整流程 (12步)

```
0. OCR (GLM, 本地 GPU, 免费)
1. stitch_chapters.py → 章节 .md
2. Pro Agent (每章一个) → 概念文件夹 (staging)
3. stage_to_concepts.py → 移到 canonical 目录
4. compute_hashes.py → SHA256
5. generate_index.py → 构建 graph.db
6. flash_dedup.py (域名+向量) → 去重候选
7. Pro Agent 去重决策 → merge_concepts.py 执行合并
8. compute_hashes.py (重跑)
9. generate_index.py (重跑)
10. resolve_deps.py → 消解依赖
11. validate_deps.py → 检查完整性
12. Pro Agent (每概念) → verify.lean
13. verify_env.py → lake build
14. generate_encyclopedia.py → 编译百科页
```

---

## 二、当前状态

### ✅ 已完成 (2026-06-25)

| 产出 | 规模 | 位置 |
|---|---|---|
| **10 本书概念提取测试** | **6,374 concepts, ¥78.70, ¥8/书** | `pipeline_output/concepts_v7/` |
| Section 拆分 (131本) | 4,482 chunks, 55MB | `pipeline_output/stitched_sections/` |
| Flash 全量分析 | 20 本, ¥4 | `section_indexes/_flash_full/` |
| OCR 进度 | 171/1,565 本, OOM 回退已修复 | `/home/a123/文档/code/Model agent/` |
| Mathlib4 索引 | 204K entries, 50.9MB | `pipeline_output/mathlib4_index.json` |
| Mathlib4 匹配 | 71.6% (3,174概念→2,271命中) | `memory/lean-integration.md` |

### 10 本书提取测试详情

| Book | Sections | Concepts | Cost |
|---|---|---|---|
| gtm004 Homological Algebra | 67 | 1,217 | ~¥16 |
| gtm027 General Topology | 37 | 763 | ~¥9 |
| gtm077 Algebraic Numbers | 38 | 805 | ~¥9 |
| gtm012 Advanced Analysis | 38 | 756 | ~¥9 |
| gtm035 Complex Variables | 30 | 782 | ~¥7 |
| gtm053 Math Logic | 28 | 532 | ~¥7 |
| gtm033 Differential Topology | 35 | 512 | ~¥8 |
| gtm095 Probability | 50 | 473 | ~¥12 |
| gtm015 Functional Analysis | 21 | 425 | ~¥5 |
| gtm044 Algebraic Geometry | 21 | 109 | ~¥5 |
| **Total** | **365 sections** | **6,374** | **¥78.70** |

每概念 3 文件: concept.yaml + theorem.tex + introduce.en.md。依赖内嵌在 concept.yaml (required/recommended/suggested)。

### 正在运行

| 任务 | 状态 | 进度 |
|---|---|---|
| GLM-OCR | 🔄 nohup 后台 | 171/1,565 本, 7.4本/h, ETA ~8天 |

### 已完成

| 产出 | 规模 | 位置 |
|---|---|---|
| 藏书 | 1,565 本 (GTM+UTM+UTX+SMM+华章+散装) | `/home/a123/文档/Springer Math-Textbooks/` |
| OCR 逐页文件 | ~129 本, 逐页 JSON | `pipeline_output/ocr_output/` |
| 章节缝合 | 128 本 | `pipeline_output/stitched/` |
| GTM073 完整提取 | 486 概念, ¥8.25 | `pipeline_output/v7_test/staging/gtm-0073/` |
| 10 本书首次测试 | 921 概念, ¥8.52 | `pipeline_output/v7_test/staging_v2/` |
| **Section 拆分 129 本** | **4,100 sections, 10页/section** | `pipeline_output/stitched_sections/` |
| Chapter 拆分 129 本 | 1,321 chapters | `pipeline_output/stitched_v2/` |
| Lean 骨架 | 240 概念, lake build 通过 | `lean/MathPkg/MathPkg/Skeleton/` |
| 定义翻译 | 84/92 (92%) | `lean/MathPkg/MathPkg/Pipeline/` |
| Batch 1 翻译 | 部分完成 | `lean/MathPkg/MathPkg/Pipeline/` |

### 工作流脚本

| 脚本 | 用途 |
|---|---|
| `workflows/v7_book_extract.js` | 单本书按章提取 (当前在用) |
| `workflows/v7_extract_strict.js` | 严格版提取 (slug + theorem.tex 规则) |
| `workflows/resilient_v4.js` | Checker+Fixer 自愈模式 |
| `workflows/skel_fix.js` | Lean 骨架修复 |
| `workflows/defs_translate.js` | 定义翻译 |
| `workflows/phase1_gapfill.js` | Gap-fill 证明展开 |

### Python 工具

| 工具 | 位置 | 用途 |
|---|---|---|
| GLM-OCR 逐页 | `/home/a123/文档/code/Model agent/glm_ocr_books.py` | 本地 OCR, 断点续跑 |
| **Section 拆分 ⭐** | `pipeline_output/stitch_by_section.py` | 4-tier: regex→chapter→Flash→size. ~10p/chunk |
| Flash Section 分析 | `pipeline_output/flash_full_section.py` | 全量OCR→Flash识别section边界, ¥0.15/本 |
| Chapter 拆分 | `pipeline_output/stitch_chapters_v2.py` | OCR 逐页→Chapter .md (tier 2 回退) |
| 章节缝合(旧) | `pipeline_output/stitch_chapters.py` | 全文正则切分 (已废弃) |
| Flash 摘要分析 | `pipeline_output/flash_section_split.py` | 页面摘要→Flash (已升级为全量) |
| SQLite 索引 | `generate_index.py` (待写) | 构建 graph.db |
| 依赖消解 | `resolve_deps.py` (待写) | 两阶段依赖 |
| Hash 计算 | `compute_hashes.py` (待写) | SHA256 |
| 百科编译 | `generate_encyclopedia.py` (待写) | 编译最终 .md |

---

## 三、关键教训 (按重要性排序)

1. **⚠️ 必须分章！每章一个 Agent，不能整本书一个 Agent。** 整本书会触发输出 Token 上限，漏掉 ~60% 概念。

2. **⭐ 用 Section 拆分，不是 Chapter。** Section ~10页/个。131本验证：4-tier策略(regex→chapter→Flash→size)，94%自动成功。详见 `memory/section-strategy.md`。

3. **Flash 全量文本分析极便宜且有效。** 全量OCR送Flash识别section边界，28本只花¥4。修复了regex无法处理的20本书。仅150字符摘要不够——需要全量文本。

4. **页/section ≈ 10，极其稳定。** 短书 8p/section，长书 12p/section。依此可判断切分质量。

5. **10 本书概念提取验证通过。** 每 section 一个 Agent，365 sections → 6,374 concepts，¥8/书。依赖嵌入 concept.yaml，格式统一。网络断连自动重试。

6. **Slug 必须是语义英文。** 必须在 Prompt 里给 ✅/❌ 对比示例，否则 Agent 会用书编号命名。

7. **Mathlib4 复用：倒排索引 > 精确 grep。** 204K entries 建三级倒排索引，71.6%命中。精确名仅1%，签名词+域过滤69%。详见 `memory/lean-integration.md`。

6. **Agent 返回值不可信，磁盘文件才是真相。** 计数 Agent 因 API 错误报告 0 概念，但磁盘上有 194 个。

7. **source_books 必须是对象数组，不是字符串数组。** 必须在 Prompt 里给完整模板。

8. **网络每 5 分钟断 5 秒。** 所有 Agent 调用必须 try-catch + 磁盘 .done 标记 + resumeFromRunId。

9. **分阶段优于单体。** Phase 1 gap-fill + Phase 2 translate 比一次性完成通过率高 50%+。

10. **GLM-OCR 对数学内容优于 fitz + 数字 PDF。** 全部 1,565 本统一 GLM-OCR。

---

## 四、环境速查

```bash
# Lean 4
export PATH="$HOME/.elan/bin:$PATH"
cd ~/文档/mathpkg/lean/MathPkg && lake build

# DeepSeek API
API_KEY=sk-f9820c6cd6ff448d9f7f0d54a1411d28

# Python
cd ~/文档/mathpkg
source "/home/a123/文档/code/Model agent/.venv/bin/activate"

# OCR 日志
tail -f /home/a123/文档/code/Model\ agent/glm_ocr_books_run.log

# GPU 状态
nvidia-smi

# 代理
export https_proxy=http://127.0.0.1:7897
```

---

## 五、下一步 (优先级排序)

1. **OCR 继续跑** → ETA ~8天, `nohup`, 7.4本/h
2. **全量 131 本启动概念提取** → 用验证过的 v7_book_extract_v3.js 模板
3. **去重** → Flash 分域 + 向量嵌入（6,374 concepts 已有）
4. **消解依赖** → resolve_deps.py: 验证所有 depends_on slug 引用可解析
5. **Lean 翻译** → Pro Agent, 每概念一个, v5 self-heal
6. **lake build 验证** → 完整 DAG

---

## 六、记忆文件索引

`~/.claude/projects/-home-a123----Springer-Math-Textbooks/memory/`

| 文件 | 内容 |
|---|---|
| `MEMORY.md` | 全部记忆索引 |
| `concept-v7-spec.md` | V7 概念格式最终规范 (SQLite schema, frontmatter, 命名规则) |
| `pipeline-v4-spec.md` | V6 Pipeline 规格 (12步, Agent prompts, 成本) |
| `v7-test-lessons.md` | 10 本书测试教训 |
| `section-strategy.md` | ⭐ Section 级拆分: 10页/section, 79%成功率 |
| `lesson-must-split-by-chapter.md` | ⚠️ 必须分章的关键教训 (已升级为 section) |
| `resilient-workflow.md` | v5 自愈模式 (Agent 写 .done/.fail) |
| `ocr-lessons.md` | GLM-OCR vs fitz 对比 |
| `skeleton-blueprint.md` | 240 概念 lake build 通过 |
| `batch1-translation.md` | Batch 1 翻译记录 |
| `subagent-workflow.md` | Claude subagent 工作流模式 |
| `deepseek-api.md` | DeepSeek API 最佳实践 |
| `lean-integration.md` | Lean 4 集成 |
| `concept-format-v3.md` | 概念文件夹 portfoglio 设计 |
| `file-spec.md` | 文件命名规范 |
| `user-preferences.md` | 用户偏好、预算 |
