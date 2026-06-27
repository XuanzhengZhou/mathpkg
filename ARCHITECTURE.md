# mathpkg 架构设计

## 设计哲学

**照搬 apt 架构，不做重新发明。** apt 在 1998-2024 年间解决了去中心化包管理的所有核心问题：
多源合并、依赖解析、状态追踪、事务回滚、插件式传输层。数学知识管理面临完全同构的挑战。

## apt 核心组件 → mathpkg 映射

```
apt 组件                     mathpkg 对应              文件
══════════════════════════════════════════════════════════════
sources.list / sources.list.d  → 知识源注册表           sources.yaml
Packages.gz (每源索引)         → concept 索引             index.yaml
pkgCache (mmap 二进制缓存)     → 合并知识图谱            graph.db (SQLite)
DepCache (依赖状态)            → 学习状态追踪            status.yaml
SAT Solver                     → 学习路径解析器          resolver/
dpkg status file               → 用户知识状态            ~/.mathpkg/status.yaml
apt-get install/upgrade        → math CLI                cmd/math
Transport Methods              → 源适配器                sources/
```

## 一、源系统 (Source System)

### sources.yaml 格式

```yaml
# /etc/mathpkg/sources.yaml 或 ~/.config/mathpkg/sources.yaml
sources:
  - name: mathpkg-core
    uri: https://github.com/mathpkg/core-graph.git
    branch: main
    trust: community
    
  - name: alice-algebraic-geometry
    uri: git@gitlab.com:alice/ag-graph.git
    branch: main
    trust: signed  # GPG 签名验证

  - name: arxiv-math-ag
    uri: https://arxiv.org/math/auto-index
    type: arxiv
    categories: [math.AG, math.CT]
    
  - name: local-notes
    uri: /home/user/my-math-notes
    type: local
```

### 设计要点（照搬 apt）

1. **sources.list.d/ 目录模式**：一个源一个文件，方便脚本添加/删除
2. **Type 插件系统**（对应 apt 的 `pkgSourceList::Type::GlobalList`）：
   - `git` 类型：Git 仓库
   - `arxiv` 类型：arXiv API 自动提取
   - `local` 类型：本地文件系统
   - `http` 类型：HTTP 服务器
3. **VolatileFiles 机制**（对应 apt）：临时加载单个概念文件，不加入持久索引

## 二、概念包格式 (Concept Package Format)

### 每个概念一个 YAML 文件

```yaml
# concept/galois_theory/concept.yaml
id: "galois_theory"
name:
  en: "Galois Theory"
  zh: "伽罗瓦理论"
type: "theory"  # definition | theorem | lemma | theory | exercise_bridge
  
# 依赖声明（对应 apt 的 Depends/Suggests/Recommends）
depends:
  required:          # 等价于 Depends: 不满足则无法理解
    - group_theory
    - field_theory
    - linear_algebra
  recommended:       # 等价于 Recommends: 学了更好
    - ring_theory
  suggested:         # 等价于 Suggests: 可选扩展
    - algebraic_number_theory

# 跨书引用（对应 apt 的 Version 多版本机制）
versions:
  - source: "GTM101"
    chapter: 4
    section: "4.1-4.3"
    pages: "42-78"
    approach: "historical"
    
  - source: "GTM167"
    chapter: 3
    section: "3.1-3.5"
    pages: "89-134"
    approach: "abstract_axiomatic"
    
  - source: "UTM146"
    chapter: 5
    pages: "101-145"
    approach: "naive_introductory"

# 关键定理/定义（概念的内容单元）
statements:
  - type: "theorem"
    name: "Fundamental Theorem of Galois Theory"
    latex: "L/K \\text{ finite Galois} \\implies \\exists \\text{ bijection between } \\{\\text{intermediate fields}\\} \\text{ and } \\{\\text{subgroups of } \\operatorname{Gal}(L/K)\\}"
    
# Lean 4 形式化状态
lean:
  status: "complete"  # none | partial | complete
  source: "Mathlib/Algebra/Galois.lean"
  theorem_name: "galois_correspondence"

# 习题（类型B和C——有知识价值的习题）
exercises:
  - type: "bridge"
    source: "GTM101"
    number: "4.3"
    description: "Show that the fixed field of Aut(L/K) equals K iff L/K is Galois"
    connects: [galois_extension, fixed_field, automorphism_group]
    
  - type: "introduction"
    source: "GTM101"
    number: "5.1"
    description: "Define the norm N(α) = ∏σ σ(α) and prove multiplicativity"
    introduces: "norm_of_algebraic_element"
```

### 设计要点（照搬 apt）

1. **depends 三级分类**直接对应 apt 的 `Depends/Recommends/Suggests`
2. **versions 多源机制**对应 apt 同一包的多版本——同一概念在不同书里有不同讲法（GTM101 vs GTM167），用户可以选择"入门版"或"严谨版"
3. **Provides 机制**（未在上述示例展开）：如果一个概念 A 完全覆盖概念 B（比如 "度量空间" provides "拓扑空间的基础直觉"），可以用 provides 声明

## 三、知识图谱缓存 (Knowledge Graph Cache)

### 对应 apt 的 pkgCache

apt 用 mmap 二进制格式追求极限性能（处理数万包）。数学知识图谱规模小得多（数千概念），用 SQLite。

```sql
-- 概念表（对应 apt Package）
CREATE TABLE concepts (
    id TEXT PRIMARY KEY,
    name_en TEXT NOT NULL,
    name_zh TEXT,
    type TEXT NOT NULL,  -- definition/theorem/lemma/theory/exercise
    lean_status TEXT,    -- none/partial/complete
    confidence REAL      -- AI 提取置信度
);

-- 依赖边表（对应 apt Dependency）
CREATE TABLE dependencies (
    from_concept TEXT NOT NULL,
    to_concept TEXT NOT NULL,
    dep_type TEXT NOT NULL,  -- required/recommended/suggested
    source_file TEXT,        -- 来自哪个源
    PRIMARY KEY (from_concept, to_concept, dep_type)
);

-- 版本/来源表（对应 apt Version + PackageFile）
CREATE TABLE concept_versions (
    concept_id TEXT NOT NULL,
    source_name TEXT NOT NULL,    -- GTM101 / GTM167 / ...
    chapter TEXT,
    pages TEXT,
    approach TEXT,                -- historical/axiomatic/naive/...
    source_uri TEXT,              -- 源的 URI
    PRIMARY KEY (concept_id, source_name)
);

-- 用户知识状态表（对应 apt dpkg status）
CREATE TABLE user_status (
    concept_id TEXT PRIMARY KEY,
    state TEXT NOT NULL,   -- not_learned/learning/learned/mastered
    started_at TEXT,
    completed_at TEXT,
    confidence INTEGER     -- 用户自评 1-5
);
```

### 设计要点

1. **缓存可丢弃重建**（对应 apt cache 设计原则）：`math update` 重新从所有源生成 SQLite
2. **哈希表查找**（对应 apt `pkgCache::Hash`）：概念 ID 的快速查找，用于依赖解析
3. **单向链表遍历**（对应 apt GrpIterator）：虽然 SQLite 不需要 mmap 指针，但遍历接口保持一致

## 四、依赖解析器 (Dependency Resolver)

### 对应 apt 的 DepCache + solver3

核心算法分两步：

```
Step 1: 拓扑展开（Topological Expansion）
  输入: 目标概念 target
  输出: 偏序依赖树
  算法: BFS/DFS 从 target 出发，沿 required 边向下展开
  
Step 2: 学习路径生成（Learning Path Generation）
  输入: 偏序依赖树 + 用户状态
  输出: 有序学习列表
  算法: 拓扑排序 + 剪枝（跳过已掌握概念）

Step 3: 冲突检测（Conflict Detection）
  检查循环依赖（A requires B, B requires A）
  检查缺失概念（依赖的概念不在任何源中）
  检查版本冲突（不同源对同一概念有冲突的定义）
```

```python
# 伪代码
def resolve(target_concept, user_status, graph):
    """解析学习路径"""
    # Step 1: 收集所有 required 依赖
    needed = set()
    queue = [target_concept]
    while queue:
        c = queue.pop(0)
        if c in user_status.mastered:
            continue
        needed.add(c)
        for dep in graph.get_dependencies(c, type='required'):
            if dep not in user_status.mastered:
                queue.append(dep)
    
    # Step 2: 拓扑排序
    order = topological_sort(needed, graph)
    
    # Step 3: 插入 recommended（建议学）
    for c in list(order):
        for rec in graph.get_dependencies(c, type='recommended'):
            if rec not in needed and rec not in user_status.mastered:
                # 插入到 c 之前
                order.insert(order.index(c), rec)
                needed.add(rec)
    
    return LearningPath(
        required=order,
        suggested=graph.get_suggested(target_concept),
        total_estimated_hours=estimate_time(order)
    )
```

### 设计要点（照搬 apt）

1. **Mark and Sweep**（对应 apt `DepCache::MarkAndSweep`）：
   - Mark: 从目标概念出发，标记所有需要安装的依赖
   - Sweep: 检查已安装但不被任何目标依赖的概念（可以"卸载"的知识垃圾回收）
   
2. **Transaction/Rollback**（对应 apt `DepCache::Transaction`）：
   - 用户说"我想学代数几何但不确定前置够不够"
   - 解析器生成一个学习计划的 Transaction
   - 用户可以接受（commit）或拒绝（rollback）
   - 所有状态变更原子操作

3. **Policy 机制**（对应 apt `DepCache::Policy`）：
   - `InstallRecommends=true` → 建议学的依赖自动加入学习路径
   - `InstallSuggests=false` → 可选的扩展不自动加入
   - 用户可以自定义 Policy（"我只想快速入门，跳过严谨证明"）

4. **三种状态比较**（对应 apt 的 Now/Install/Candidate）：
   - Now: 用户当前知识状态
   - Install: 学习后的目标状态
   - Candidate: 最优可达状态（考虑所有可选依赖）

## 五、用户知识状态 (User Knowledge State)

### 对应 apt 的 dpkg status

```yaml
# ~/.mathpkg/status.yaml
user:
  name: "Alice"
  
concepts:
  group_theory:
    state: mastered
    learned_from: "GTM080"
    completed: "2026-03-15"
    confidence: 4
    
  galois_theory:
    state: learning
    started: "2026-06-20"
    current_source: "GTM101"
    current_page: 67
    
  algebraic_geometry:
    state: not_learned
    # 但系统知道：一旦群论+交换代数都 mastered，就可以开始了
```

### 设计要点

1. **状态机**（对应 apt `State::PkgCurrentState`）：
   ```
   not_learned → learning → learned → mastered
                              ↓
                           stuck (用户标记困难)
   ```

2. **知识垃圾回收**（对应 apt autoremove）：
   - 如果用户很久没碰某个概念（比如 6 个月），且它只是某个已学概念的 recommended（而非 required）
   - `math autoremove` 可以提示"你是否还记得这些？建议复习或标记遗忘"

## 六、CLI 命令体系

### 对应 apt-get / apt

```bash
# 源管理
math source add <uri>          # 添加知识源
math source remove <name>      # 移除知识源
math source list                # 列出所有源
math update                     # 刷新所有源的索引，重建知识图谱

# 概念管理
math search <query>             # 搜索概念
math show <concept>             # 查看概念详情（定义、多书讲法、依赖）
math install <concept>          # 生成学习路径并开始学习
math install --with-suggests    # 包含可选依赖

# 状态管理
math status                     # 查看当前学习状态
math mark <concept> mastered    # 标记已掌握
math mark <concept> stuck       # 标记困难
math autoremove                 # 提示可能需要复习的概念

# 扩展
math lean <concept>             # 查看/交互该概念的 Lean 形式化
math compare <concept>          # 比较不同书对同一概念的讲法
```

## 七、源适配器插件系统

### 对应 apt 的 Transport Methods

```python
# sources/adapters/git_adapter.py
class GitAdapter(SourceAdapter):
    """从 Git 仓库加载知识图谱"""
    
    def fetch_index(self, uri: str) -> Index:
        """拉取 index.yaml"""
        
    def fetch_concept(self, uri: str, concept_id: str) -> Concept:
        """拉取单个概念 YAML"""

# sources/adapters/arxiv_adapter.py  
class ArxivAdapter(SourceAdapter):
    """从 arXiv API 自动提取概念"""
    
    def fetch_index(self, uri: str) -> Index:
        """查询 arXiv API，自动管道提取"""
```

### 设计要点

直接照搬 apt 的 `pkgSourceList::Type::GlobalList` 插件注册机制：
- 每个适配器注册到一个全局列表
- 新适配器只需实现 `fetch_index` + `fetch_concept` 两个方法
- URI scheme 决定使用哪个适配器（git:// → GitAdapter, arxiv:// → ArxivAdapter）

## 八、硬件评估

### 本地服务器配置
- CPU: 192 核心
- GPU: RTX 5060 Ti 16GB (Compute Capability 12.0)
- RAM: 62GB + 63GB swap
- 磁盘: NVMe 1TB (328GB 可用)

### 工作量评估

| 任务 | 是否需要 GPU | 本地可完成 | 说明 |
|------|-------------|-----------|------|
| PDF → Markdown (数字版) | ❌ | ✅ | CPU 密集型，192核绰绰有余 |
| OCR (扫描版) | ✅ | ✅ | 5060Ti 16GB 足够 GLM-OCR |
| 概念提取 (LLM) | 可选 | 部分 | 小模型可本地跑，大模型用 API |
| Lean 翻译 (LLM) | 可选 | 部分 | 同上 |
| Lean 编译验证 | ❌ | ✅ | CPU 密集型，192核极快 |
| 知识图谱构建 | ❌ | ✅ | SQLite + Python |
| 依赖解析 | ❌ | ✅ | 图算法，毫秒级 |

### 结论

**不需要租 5090。** 原因：
1. OCR 任务 5060Ti 完全胜任（GLM-OCR 针对消费级 GPU 优化）
2. LLM 推理用 DeepSeek V4 API 更划算（¥2-6/百万token），本地 GPU 只跑小模型
3. 真正消耗算力的 Lean 编译是 CPU 任务，192核是巨大优势
4. 管道跑通后，重复构建的边际成本极低

## 九、项目结构

```
mathpkg/
├── ARCHITECTURE.md           # 本文档
├── README.md
├── sources.yaml              # 默认源配置
│
├── cmd/
│   └── math                  # CLI 入口
│
├── mathpkg/
│   ├── source/               # 源管理（对应 apt-pkg/sourcelist）
│   │   ├── source_list.py    #   读取和管理源列表
│   │   ├── adapters/         #   源适配器插件（对应 apt methods/）
│   │   │   ├── git.py
│   │   │   ├── arxiv.py
│   │   │   └── local.py
│   │   └── index.py          #   索引解析（对应 apt-pkg/tagfile）
│   │
│   ├── graph/                # 知识图谱（对应 apt-pkg/pkgcache）
│   │   ├── cache.py          #   SQLite 缓存管理
│   │   ├── concept.py        #   概念数据模型
│   │   └── merge.py          #   多源合并
│   │
│   ├── resolver/             # 依赖解析（对应 apt-pkg/depcache + solver3）
│   │   ├── dep_cache.py      #   依赖状态管理
│   │   ├── solver.py         #   学习路径求解
│   │   └── policy.py         #   策略配置
│   │
│   ├── status/               # 用户状态（对应 dpkg status）
│   │   └── user_state.py
│   │
│   └── pipeline/             # 内容提取管道
│       ├── pdf_extract.py    #   PDF → Markdown
│       ├── concept_extract.py #   Markdown → 概念 JSON
│       └── lean_translate.py #   概念 → Lean 4 代码
│
├── concepts/                 # 核心概念库（第一个"源"）
│   └── algebra/
│       ├── index.yaml
│       └── nodes/
│           ├── group.yaml
│           ├── ring.yaml
│           └── ...
│
├── lean/                     # Lean 4 形式化库
│   └── MathPkg/
│       └── Algebra/
│           └── Group.lean
│
└── tests/
    ├── test_resolver.py
    └── test_pipeline.py
```

## 十、里程碑路线

### Phase 0: 最小原型（1周）
- [ ] 手工创建 20 个群论概念结点（YAML）
- [ ] 实现 `math source add/list` + `math update`
- [ ] 实现 `math install <concept>` 依赖拓扑排序
- [ ] 本地 SQLite 缓存

### Phase 1: 自动化管道（2-3周）
- [ ] 选 5 本数字版代数教材
- [ ] PDF → Markdown 提取
- [ ] LLM 概念提取管道
- [ ] 自动化概念 YAML 生成

### Phase 2: Lean 集成（2-4周）
- [ ] Mathlib4 覆盖度自动比对
- [ ] 从依赖树叶子向上构建 Lean
- [ ] 编译通过率统计

### Phase 3: 去中心化（2周）
- [ ] Git 适配器完善
- [ ] 多源合并去重
- [ ] 社区贡献指南

### Phase 4: 交互学习（持续）
- [ ] AI 导师 RAG 集成
- [ ] 学习进度追踪
- [ ] Web UI
