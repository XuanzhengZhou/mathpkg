---
role: proof
locale: en
of_concept: characterization-of-ergodic-sets
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Since $\alpha_E P^E = \alpha_E$, the restricted chain $P^E$ has $\alpha_E$ as an invariant measure. A chain is ergodic if and only if its total invariant measure is finite. Hence $P^E$ is ergodic if and only if $\alpha_E 1 < \infty$.

For the remaining assertions: a finite set $E$ has $\alpha_E 1 = \sum_{i \in E} \alpha_i < \infty$ since each $\alpha_i$ is finite, so $E$ is ergodic. If $F \subseteq E$ and $E$ is ergodic, then $\alpha_F 1 \leq \alpha_E 1 < \infty$, so $F$ is ergodic. If $E$ and $F$ are ergodic, then $\alpha_{E \cup F} 1 \leq \alpha_E 1 + \alpha_F 1 < \infty$, so $E \cup F$ is ergodic.
