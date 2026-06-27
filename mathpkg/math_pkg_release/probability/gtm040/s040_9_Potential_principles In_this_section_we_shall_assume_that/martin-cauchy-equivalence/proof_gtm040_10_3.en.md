---
role: proof
locale: en
of_concept: martin-cauchy-equivalence
source_book: gtm040
source_chapter: "10"
source_section: "3"
---

If $\{j_n\}$ is Cauchy, then $\{w_i N_{\pi i} K(i, j_n)\}$ is Cauchy, and since $w_i N_{\pi i} > 0$, $\{K(i, j_n)\}$ is Cauchy.

Conversely, let $\{K(i, j_n)\}$ be Cauchy for all $i$, and let $\epsilon > 0$. Choose a finite set $E$ such that $\sum_{k \in S-E} w_k N_{kk} < \epsilon/2$, and choose $M$ large enough so that $|K(i, j_m) - K(i, j_n)| < \epsilon / (2 \sum w_k N_{kk})$ for $i \in E$ and $n, m \geq M$. Then $d(j_m, j_n) < \epsilon$.
