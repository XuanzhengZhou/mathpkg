---
name: deepseek-api-best-practices
description: "DeepSeek V4 API — thinking mode, token limits, retry strategy, parallelization"
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# DeepSeek API Best Practices

## Model Selection

| Task | Model | Thinking | Cost |
|---|---|---|---|
| Concept extraction (per-chapter) | Pro | ✅ Required | ¥3/M in, ¥6/M out |
| Gap-fill (proof expansion) | Pro | ✅ Required | Same |
| Lean translation | Pro | ✅ Required | Same |
| Quality classification | Flash | ❌ Not needed | ¥1/M in, ¥2/M out |
| Cross-book dedup (fuzzy match) | Flash | ❌ | Same |

## The Thinking Mode Trap

**Root cause of most failures**: With thinking mode enabled, `max_tokens` is shared between thinking tokens and output. If thinking consumes all tokens, `content` is EMPTY.

**Symptoms**: `"Expecting value: line 1 column 1 (char 0)"` — JSON parse error on empty response.

**Fix**: Set `max_tokens=393216` (384K, the model's max output). With 384K output budget, thinking will almost never exhaust it. Do NOT add retry logic for thinking exhaustion — it wastes tokens.

## Token Budget

- DeepSeek V4 Pro: 1M context, 384K max output
- **NEVER set a restrictive max_tokens** (like 4096 or 16384) — it WILL cause thinking to consume all output tokens
- Default should be 393216 (essentially unlimited)
- Only record token consumption; don't limit it

## API Timeout

- Pro + thinking for complex math proofs: can take 5-10 minutes
- Set timeout to **1200 seconds** (20 minutes)
- Exponential backoff for network errors: 5s, 10s, 20s, 40s (5 retries)

## Parallelization

- DeepSeek Flash: **2500 concurrent** requests supported
- DeepSeek Pro: Also supports high concurrency
- Use `ThreadPoolExecutor(max_workers=100)` for parallel API calls
- **DO NOT use serial loops** — each concept takes 3-10 minutes sequentially

## Cost Tracking

Track per-call costs:
```python
cost_yuan = (prompt_tokens * 3 + completion_tokens * 6) / 1_000_000  # Pro
cost_yuan = (prompt_tokens * 1 + completion_tokens * 2) / 1_000_000  # Flash
```

For GTM073 (611 concepts from 202 chunks): ~¥4/book.
For 20 books (5779 concepts from 2603 chunks): ~¥40 total.
