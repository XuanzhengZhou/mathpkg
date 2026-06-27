---
role: proof
locale: en
of_concept: df-space-linear-map-continuity
source_book: gtm003
source_chapter: "IV"
source_section: "6"
---

Let $W_n$ be the closure of $B_n \cap V + \frac{1}{2} U_n$; then $W_n \subset B_n \cap V + U_n$, hence
$$B_n \cap W_n \subset B_n \cap V + (2B_n) \cap U_n \subset B_n \cap V + 2(B_n \cap U_n) \subset 3(B_n \cap V);$$
letting $W = \bigcap_1^\infty W_n$, it follows that $B_n \cap W \subset 3B_n \cap 3V$ which, in view of $\bigcup_1^\infty B_n = \bigcup_1^\infty 3B_n = E$, implies that $W \subset 3V$. On the other hand, $W$ is closed, convex, circled, and absorbs each $B_n$, since for suitable $\rho_n > 0$, $B_n \subset \rho_n(B_n \cap U_n) \subset \rho_n(B_n \cap V) \subset \rho_n(B_{n+p} \cap V) \subset \rho_n W_{n+p}$ for all $p \in N$. Hence $\bigcup_1^\infty W_n^\circ$ is strongly bounded and therefore equicontinuous in $E'$. It follows that $W$ and hence $V \supset \frac{1}{3} W$ is a $0$-neighborhood in $E$.
