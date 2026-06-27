---
role: proof
locale: en
of_concept: acyclic-complex-boundaries-stably-free
source_book: gtm010
source_chapter: "13"
source_section: "13"
---

(A) By induction. For i = dim C, C_i = B_i, so B_i is free = stably free. Assuming B_{i-1} is stably free, use the exact sequence 0 -> B_i -> C_i -> B_{i-1} -> 0 and the fact that C_i is free. Since B_{i-1} is stably free, choose a section s: B_{i-1} -> C_i. Then C_i = B_i + s(B_{i-1}) and s(B_{i-1}) is stably free. Adding free modules if necessary, B_i is stably free.

(B) By (A), choose a section delta_i: B_{i-1} -> C_i for each surjection d_i: C_i -> B_{i-1}. Then C_i = B_i + delta_i(B_{i-1}). Define delta: C -> C by delta|B_i = delta_{i+1} and delta|delta_i(B_{i-1}) = 0. Then d delta + delta d = 1.
