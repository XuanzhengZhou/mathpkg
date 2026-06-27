---
role: proof
locale: en
of_concept: product-totally-bounded-iff-projections-totally-bounded
source_book: gtm036
source_chapter: ""
source_section: "F"
---

Let $B \subset \prod_{\alpha} E_\alpha$ and let $\pi_\alpha$ denote the projection onto $E_\alpha$.

If $B$ is totally bounded, then each $\pi_\alpha(B)$ is totally bounded by the previous proposition, since $\pi_\alpha$ is a continuous linear map.

Conversely, suppose each $\pi_\alpha(B)$ is totally bounded. Let $U$ be a basic neighborhood of $0$ in the product, so $U = \prod_{\alpha} U_\alpha$ where each $U_\alpha$ is a neighborhood of $0$ in $E_\alpha$, and $U_\alpha = E_\alpha$ for all but finitely many $\alpha$, say $\alpha \in A$. For each $\alpha \in A$, since $\pi_\alpha(B)$ is totally bounded, there exists a finite set $N_\alpha \subset E_\alpha$ such that $\pi_\alpha(B) \subset N_\alpha + U_\alpha$. Let $N = \prod_{\alpha \in A} N_\alpha \times \prod_{\alpha \notin A} \{0\}$, which is finite. Then $B \subset N + U$, so $B$ is totally bounded.
