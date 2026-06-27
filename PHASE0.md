# Phase 0: 最小可行原型 (MVP)

> 目标：用 20 个群论概念手工构建端到端管道，验证架构可行性
> 时间：约 1 周
> 成功标准：`math install lagrange_theorem` 输出正确的学习路径，且对应 Lean 定理编译通过

---

## 一、范围定义：20 个群论概念

选择群论基础是因为：
1. Mathlib4 覆盖率最高（~85%）
2. 依赖链清晰，拓扑排序有意义
3. 是代数方向所有后续学习的根

### 概念清单与依赖关系

```
编号  概念 ID                    类型         依赖 (required)              推荐 (recommended)
─────────────────────────────────────────────────────────────────────────────────────
C01   set_and_function           theory       -                            -
C02   binary_operation           definition   set_and_function             -
C03   semigroup                  definition   binary_operation             -
C04   monoid                     definition   semigroup                    -
C05   group                      definition   monoid                       semigroup
C06   abelian_group              definition   group                        -
C07   subgroup                   definition   group                        -
C08   group_homomorphism         definition   group                        set_and_function
C09   kernel_of_homomorphism     definition   group_homomorphism, subgroup  -
C10   image_of_homomorphism      definition   group_homomorphism, subgroup  -
C11   normal_subgroup            definition   subgroup, group_homomorphism  -
C12   quotient_group             definition   normal_subgroup              -
C13   group_isomorphism          definition   group_homomorphism            -
C14   first_isomorphism_theorem  theorem      quotient_group, kernel, image, group_isomorphism  -
C15   symmetric_group            definition   group, set_and_function       -
C16   cyclic_group               definition   group                        abelian_group
C17   group_action               definition   group, symmetric_group        -
C18   lagrange_theorem           theorem      subgroup, coset              -
C19   cayley_theorem             theorem      symmetric_group, group_action  -
C20   orbit_stabilizer_theorem   theorem      group_action, lagrange_theorem  -
```

**依赖图（ASCII）**：

```
                    set_and_function
                         │
                    binary_operation
                         │
                      semigroup
                         │
                       monoid
                         │
         ┌───────────── group ─────────────┐
         │               │                  │
    abelian_group    subgroup        group_homomorphism
         │               │            ┌────────┴────────┐
    cyclic_group    normal_subgroup  kernel           image
                         │               │              │
                    quotient_group      └──────┬────────┘
                         │                     │
                    coset (副节点)    group_isomorphism
                         │                     │
                  lagrange_theorem    first_isomorphism_theorem
                         │
                    group_action ───── symmetric_group
                         │                │
                  orbit_stabilizer   cayley_theorem
```

---

## 二、文件结构与产出物

```
mathpkg/
├── concepts/                              # Phase 0 产出：概念库（第一个"源"）
│   └── algebra/
│       └── group_theory/
│           ├── index.yaml                 # 源索引（对应 apt Packages.gz）
│           └── nodes/
│               ├── group.yaml             # C05
│               ├── subgroup.yaml          # C07
│               ├── lagrange_theorem.yaml  # C18
│               └── ...（共 20 个 .yaml）
│
├── lean/                                  # Phase 0 产出：Lean 形式化
│   └── MathPkg/
│       └── Algebra/
│           └── Group/
│               ├── Lagrange.lean          # Lagrange 定理（C18）
│               ├── Cayley.lean            # Cayley 定理（C19）
│               └── ...（对 Mathlib4 缺失的概念）
│
├── mathpkg/                               # Python 包
│   ├── __init__.py
│   ├── source/
│   │   ├── __init__.py
│   │   ├── source_list.py                 # 读取 sources.yaml，管理源列表
│   │   └── index.py                       # 解析 index.yaml
│   │
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── cache.py                       # SQLite 缓存管理
│   │   └── concept.py                     # 概念数据类
│   │
│   ├── resolver/
│   │   ├── __init__.py
│   │   ├── solver.py                      # 拓扑排序 + 学习路径生成
│   │   └── policy.py                      # InstallRecommends 等策略
│   │
│   └── status/
│       ├── __init__.py
│       └── user_state.py                  # ~/.mathpkg/status.yaml 读写
│
├── cmd/
│   └── math                               # CLI 入口（Python 脚本）
│
├── tests/
│   ├── test_solver.py                     # 依赖解析器单元测试
│   └── test_e2e.py                        # 端到端测试
│
├── sources.yaml                           # 默认源配置
└── ~/.mathpkg/status.yaml                 # 用户知识状态（运行时生成）
```

---

## 三、每日计划（7 天）

### Day 1: 概念数据模型 + 手工 YAML 编写

**任务**：
- [ ] 编写 `concept.py`：Concept 数据类（dataclass + Pydantic 验证）
- [ ] 编写 20 个概念的 YAML 文件（手工，质量优先）
- [ ] 编写 `index.yaml`
- [ ] 验证：所有 YAML 能正确解析

**产出**：
```
concepts/algebra/group_theory/index.yaml
concepts/algebra/group_theory/nodes/*.yaml (20个)
mathpkg/graph/concept.py
```

**每个 YAML 的格式**（以 C18 Lagrange 定理为例）：

```yaml
id: lagrange_theorem
name:
  en: "Lagrange's Theorem"
  zh: "拉格朗日定理"
type: theorem

depends:
  required:
    - subgroup
    - coset
  recommended:
    - group_action
  suggested: []

versions:
  - source: "GTM073"
    author: "Hungerford"
    chapter: "I"
    section: "I.4"
    pages: "38-40"
    theorem_number: "4.6"
    statement_latex: |
      \\text{Let } H \\leq G \\text{ with } G \\text{ finite. Then } |G| = [G:H] \\cdot |H|.
      
  - source: "GTM080"
    author: "Robinson"
    chapter: "1"
    section: "1.3"
    pages: "15-17"
    theorem_number: "1.3.6"
    
  - source: "GTM148"
    author: "Rotman"
    chapter: "2"
    section: "2.4"
    pages: "34-36"
    theorem_number: "2.30"

statements:
  - type: theorem
    name: "Lagrange's Theorem"
    latex: |
      \\text{Let } G \\text{ be a finite group and } H \\leq G.
      \\text{ Then } |H| \\text{ divides } |G|.
      \\text{ Moreover, } |G| = [G:H] \\cdot |H|.
    proof_sketch: |
      1. Define the left cosets gH for g ∈ G.
      2. Prove they partition G (equivalence relation).
      3. Prove |gH| = |H| for all g (left multiplication is bijection).
      4. Count: |G| = (number of cosets) × |H|.

lean:
  mathlib4_path: "Mathlib.Algebra.Group.Subgroup.Basic"
  mathlib4_theorem: "Subgroup.card_mul_card"
  status: "complete"  # Mathlib4 已有

exercises:
  - type: bridge
    source: "GTM073"
    number: "I.4.8"
    description: "Prove that any group of prime order p is cyclic."
    connects: [lagrange_theorem, cyclic_group]
```

### Day 2: 源管理系统 + SQLite 缓存

**任务**：
- [ ] 实现 `source_list.py`：读取 `sources.yaml`，支持 Git/本地源
- [ ] 实现 `index.py`：解析源中的 `index.yaml`
- [ ] 实现 `cache.py`：SQLite 建表 + 从源重建缓存
- [ ] 实现 `math source add/list` + `math update`

**产出**：
```
mathpkg/source/source_list.py
mathpkg/source/index.py
mathpkg/graph/cache.py
```

**核心函数签名**：

```python
# source_list.py
class SourceList:
    """对应 apt pkgSourceList"""
    def read_main_list(self) -> list[Source]
    def add_source(self, uri: str) -> None
    def remove_source(self, name: str) -> None

# cache.py
class KnowledgeCache:
    """对应 apt pkgCache"""
    def rebuild(self, sources: list[Source]) -> None
    def find_concept(self, id: str) -> Concept
    def get_dependencies(self, id: str, dep_type: str) -> list[str]
    def get_all_concepts(self) -> list[str]
```

### Day 3: 依赖解析器

**任务**：
- [ ] 实现 `solver.py`：拓扑展开 + 拓扑排序 + 学习路径生成
- [ ] 实现 `policy.py`：控制 recommended/suggested 是否自动加入
- [ ] 实现 `math show <concept>` + `math install <concept>`
- [ ] 处理循环依赖检测、缺失依赖检测

**产出**：
```
mathpkg/resolver/solver.py
mathpkg/resolver/policy.py
```

**核心算法**：

```python
def resolve_learning_path(
    target: str,
    graph: KnowledgeCache,
    user_state: UserState,
    policy: Policy
) -> LearningPath:
    """
    1. BFS 展开 required 依赖
    2. 剪枝已掌握的结点
    3. 拓扑排序（Kahn's algorithm）
    4. 按 policy 插入 recommended
    5. 返回有序学习列表
    """
```

### Day 4: 用户知识状态 + CLI 完善

**任务**：
- [ ] 实现 `user_state.py`：读写 `~/.mathpkg/status.yaml`
- [ ] 实现 `math status` + `math mark <concept> mastered/stuck`
- [ ] 格式化输出（带颜色的终端树）
- [ ] 编写单元测试

**产出**：
```
mathpkg/status/user_state.py
tests/test_solver.py
```

**CLI 输出效果预期**：

```
$ math install group_action

解析依赖中...
group_action (群作用)
├── group ✅ (已掌握, GTM080 §1)
├── symmetric_group
│   ├── group ✅ (已掌握)
│   └── set_and_function ✅ (已掌握)
└── [recommended] group_homomorphism ✅ (已掌握)

学习路径（3 个新概念）:
  1. symmetric_group     (~1.5h, GTM148 §2)
  2. group_action        (~2.0h, GTM073 §I.6)
  3. cayley_theorem      (~0.5h, 作为习题验证理解)

预估总时间: 4.0 小时
开始学习? [Y/n]
```

### Day 5: Lean 4 集成 — Mathlib4 比对

**任务**：
- [ ] 写脚本比对 20 个概念与 Mathlib4 的覆盖度
- [ ] 生成覆盖度报告：哪些已在 Mathlib4、哪些需要新建
- [ ] 对于已在 Mathlib4 的概念，记录精确的模块路径和定理名
- [ ] 为缺失的概念创建 Lean 项目骨架

**产出**：
```
lean/MathPkg/Algebra/Group/
mathpkg/pipeline/mathlib4_check.py
```

**覆盖度比对逻辑**：

```python
# 伪代码
def check_mathlib4_coverage(concept: Concept) -> CoverStatus:
    # 1. 按概念名搜索 Mathlib4
    # 2. 按定理陈述的 LaTeX 签名搜索
    # 3. 返回：complete（已有）/ partial（部分有）/ none（缺失）
```

### Day 6: Lean 4 形式化 — Lagrange 定理

**任务**：
- [ ] 在 Mathlib4 中找到 Lagrange 定理：`Subgroup.card_mul_card`
- [ ] 编写一个"包装"版本，展示从教科书定理到 Lean 代码的映射
- [ ] 编译验证通过
- [ ] 对于 Mathlib4 缺失的概念（如果有），尝试让 LLM 写 Lean 代码

**产出**：
```lean
-- lean/MathPkg/Algebra/Group/Lagrange.lean
import Mathlib

open Subgroup

-- Mathlib4 中的 Lagrange 定理
#check Subgroup.card_mul_card
-- Subgroup.card_mul_card: H.card * H.index = G.card

-- 教科书的等价陈述
theorem lagrange_textbook {G : Type*} [Group G] [Fintype G] (H : Subgroup G) :
    Fintype.card G = H.index * Fintype.card H := by
  -- 使用 Mathlib4 已有的定理
  rw [Subgroup.card_mul_card H]
  ring
```

### Day 7: 端到端测试 + 文档

**任务**：
- [ ] 端到端测试：`math install lagrange_theorem` → 学习路径 → Lean 验证
- [ ] 修复边界情况（孤立结点、循环依赖、缺失概念）
- [ ] 完善 README 和 ARCHITECTURE 中的关键部分
- [ ] 写一份 Phase 0 报告

---

## 四、成功标准

| 指标 | 目标 | 测量方式 |
|------|------|---------|
| CLI 可用 | `math install X` 输出正确学习路径 | 手动测试 5 个不同目标概念 |
| 依赖解析正确 | 100% 拓扑排序正确 | 单元测试覆盖 20 个概念 |
| Lean 集成 | 至少 1 个定理编译通过 | `lake build` 成功 |
| Mathlib4 覆盖报告 | 准确标注 20 个概念的覆盖状态 | 手动抽样验证 5 个 |
| 端到端管道 | 从 YAML 到 Lean 编译，无人工干预 | `make test-e2e` 通过 |

## 五、可复用资产

Phase 0 之后，以下资产可以直接用于 Phase 1：

```
✅ 概念 YAML 格式 → 自动化管道的目标格式
✅ SQLite 缓存设计 → 承载数千概念
✅ 依赖解析器 → 直接可用，只需扩展规模
✅ CLI 框架 → 逐步增加命令
✅ Lean 项目骨架 → 批量添加定理
```

## 六、依赖与风险

| 依赖 | 状态 | 备选方案 |
|------|------|---------|
| Lean 4.31.0 | ✅ 已安装 | - |
| Mathlib4 | ✅ 已安装（8175 .olean） | - |
| Python 3 | ✅ 系统自带 | - |
| SQLite | ✅ 系统自带 | - |
| Git | ✅ 系统自带 | - |
| clash-verge 代理 | ✅ 运行中 | 本地操作不需要代理 |
