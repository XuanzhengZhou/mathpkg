---
name: pipeline-v3-design
description: "V3 pipeline: OCR → stitch → Pro concept extraction → Flash dedup → Pro Lean. Full pathway design."
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Pipeline V3 Design (2026-06-24)

## Full Pathway

```
OCR 逐页 JSON (GLM, 本地 GPU, 免费)
  ↓ stitch_chapters.py (Python, 正则匹配 CHAPTER, ~2s/book)
书名-章节.md (68K avg, LaTeX math preserved)
  ↓ Pro+Thinking Agent (高并发, 每章一个, 无冲突)
extracted/GTM073/ch01.json  ← 概念 entries (statement, proof, deps, sources)
  ↓
Phase B: Flash 去重循环
  ├─ Flash 扫全量概念名列表 → 疑似重复组 (¥0.002/次)
  ├─ Pro 复核: 合并 or 不同? (只在有疑点时)
  ├─ Python 精确匹配合并 (免费)
  └─ 循环直到 Flash 说 "没有了"
  ↓
标准概念目录 (每概念一目录, 三个文件):
  concepts/<id>/
  ├── <id>.md      ← 百科页 (Statement, Proof, Textbook Comparison, Dependencies, Lean Verification, Exercises)
  ├── <id>.lean    ← Lean 4 证明 (Pro Agent: gap-fill + grep Mathlib4 + self-heal)
  └── concept.yaml ← 依赖/源书/版本 (Python 脚本从概念数据生成)
```

## Why This Design

| 旧通路 | 新通路 | 原因 |
|---|---|---|
| Flash: JSON→百科.md | 消除, 合并进 Pro 输出 | Pro 直接产 .md 质量更高, 省一次调用 |
| Python 精确去重 | Flash 扫全量 + Pro 复核 | 中文名/英文名/同义词 Python 搞不定 |
| 每页一个 JSON | 缝合为章节 .md | 500页/本不能拆500次 API 调用 |
| 三个独立模型调用 | 两次 (Pro+Pro) | Flash 只在去重时用, 极便宜 |

## Key Design Decisions

1. **缝合在本地, 不在模型内.** stitch_chapters.py 纯正则匹配 CHAPTER 标记, 1,565 本书 <1 分钟.
2. **概念提取输出 .md + yaml 数据.** Pro 一次性产出陈述+证明+依赖, 不再需要 Flash 美化.
3. **Flash 扫全局去重.** 中文 "拉格朗日定理" 和英文 "Lagrange's Theorem" 要合并 — Python 做不到, Flash 可以.
4. **每个概念一个目录, 永不冲突.** 高并发 Agent 各自写自己的文件.
5. **混合模型策略.** Flash (便宜) 负责扫描/格式化. Pro (贵) 只负责推理: 概念提取 + 复核去重 + Lean 翻译.

## Concept .md Specification

固定 6 节:
1. Statement — 定理陈述 (LaTeX)
2. Proof — 详细证明步骤
3. Textbook Comparison — 各教材讲法对比表
4. Dependencies — 前置/后继概念图
5. Lean Verification — Lean 代码块 + 编译状态
6. Exercises — 分层习题 (Basic/Intermediate/Advanced)

## Related
- [[concept-format-v2]] — three-file format
- [[ocr-lessons]] — GLM-OCR quality comparison
- [[resilient-workflow]] — Checker+Fixer pattern
