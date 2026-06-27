---
name: user-preferences-workflow
description: "User's preferences, workflow patterns, hardware, and feedback from Batch 1 translation"
metadata: 
  node_type: memory
  type: user
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# User Preferences & Project Context

## Hardware
- CPU: 192 cores
- GPU: RTX 5060 Ti 16GB
- RAM: 62GB (+63GB swap)
- Disk: NVMe 1TB
- Network: 2.4G WiFi (~150Mbps), drops ~5s every ~5min
- Comsol simulation permanently running (~52GB RSS) — must account for memory pressure
- Tailscale VPN for external access

## Workflow Preferences

1. **Phased over monolithic.** Break work into focused phases with QC gates between them.
   Each phase should have ONE clear goal.

2. **Disk files as truth, not API responses.** API disconnections are the norm. Always write
   marker files (.done, .fail) to disk and check those instead of trusting agent return values.

3. **Checker+Fixer pattern for any long-running agent task.** Cheap local checker (free, fast)
   validates work. Expensive fixer agent only runs when validation fails.

4. **Multi-workflow concurrency.** Single Workflow caps at ~16. Launch 2-3+ simultaneously
   for real parallelism. User has 192 cores — use them.

5. **50 agents at a time is acceptable.** Server can handle it. Use multi-workflow to achieve this.

6. **Retry, don't give up.** API errors should trigger retry, not stop. Exponential-ish backoff
   (natural delay from agent spawn time). 8-10 retries max.

7. **Quality control at every phase boundary.** Check outputs before moving to next phase.
   Failed QC → redo that specific item, not the whole batch.

8. **Definitions don't need gap-fill.** Skip Phase 1 for definitions — they just need correct
   `def`/`class`/`structure` translation.

## Dislikes

- Monolithic agent prompts (too long → thinking exhaustion → poor results)
- StructuredOutput with DeepSeek (unreliable, use disk files instead)
- Inline Python `-c` in Workflow JS prompts (escaping bugs → silent failures)
- Blindly trusting agent() return value (API errors make it null)
- Single Workflow for large batches (concurrency bottleneck)

## Successful Patterns

- `resilient_v4.js` — the Checker+Fixer pattern that finally worked
- `checker.py` — standalone Python compile checker
- Multi-workflow launch (2-3 workflows × 10-16 agents each)
- Phase 1 gap-fill with QC → Phase 2 Checker+Fixer
- `lake env lean` for local compilation (parallel, free, uses .olean cache)
- `xargs -P 16` for parallel local tasks

## Budget Context

- DeepSeek API budget: ~¥100
- Spent: ~¥93 (concept extraction ¥42.50, Batch 1 translation ~¥50)
- Remaining: ~¥7
- Batch 2-5 (191 concepts) needs additional budget or more efficient approach
