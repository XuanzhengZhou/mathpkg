---
name: resilient-workflow-pattern
description: "Self-healing Agent: writes .done/.fail itself. No separate checker. Retry loop only checks disk."
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Resilient Workflow Pattern (v5 — Simplified)

## Evolution

| Version | Pattern | Problem |
|---|---|---|
| v1-v3 | Monolithic, try-catch retry | API errors broke retry loop |
| v4 | Checker (agent) + Fixer (agent) | Checker costs 11.1K tokens per call |
| **v5** | **Agent writes .done/.fail itself** | Zero extra token cost |

## Key Insight

The **working agent itself** decides when it's done. No separate checker needed.

```
Agent does work:
  ├─ Finished successfully → writes .done → stops
  ├─ Stuck (errors remaining) → writes .fail → stops
  └─ API error mid-work → no .done, no .fail → retry

Workflow retry loop:
  └─ Check disk: .done? → complete
                 .fail? → retry (agent resumes from disk)
                 都没有? → API error, retry
```

## Why This Works

- Agent is the expert — it knows when it's done better than any checker
- Agent writes `.done` or `.fail` as its LAST action
- If API drops before writing either → retry (agent resumes from breakpoint)
- Zero extra token cost — no checker agent needed
- 11.1K tokens saved per retry cycle

## Template

```javascript
for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
  try { await agent(workPrompt + 'Write .done when done, .fail if stuck') } catch(e) {}

  // Check disk ONLY — no checker agent
  var doneCheck = await agent('python3 -c "import os; print(os.path.exists(\"' + df + '\"))"')
  if (doneCheck !== null && doneCheck.includes('True')) return { status: 'done' }

  var failCheck = await agent('python3 -c "import os; print(os.path.exists(\"' + ff + '\"))"')
  if (failCheck !== null && failCheck.includes('True')) {
    // Agent left .fail → resume with error info
    continue  // Next attempt, agent reads .fail and continues
  }

  // No marker → API error → retry
}
```

## Related
- [[concept-format-v3]] — portfolio folder design
- [[batch1-translation]] — where we learned this
