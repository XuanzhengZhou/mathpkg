---
role: proof
locale: en
of_concept: root-continuity-functions
source_book: gtm043
source_chapter: "13"
source_section: "13.3"
---
Let $a$ be fixed, with distinct values $r_1 < \cdots < r_m$ among $\rho_1 a, \dots, \rho_n a$. For each $j$, choose a closed disk $W_j$ centered at $r_j$ on the real axis, small enough that the $W_j$ are pairwise disjoint and contain no roots of $\mathfrak{p}_a$ other than those with real part $r_j$. Let $\Gamma_j = \partial W_j$.

The continuous map $(b, z) \mapsto \mathfrak{p}_b(z)$ is continuous, and the distance from the complex plane to $\mathbb{R}$ has a positive lower bound $\epsilon$ on $\bigcup_j \Gamma_j$. Hence there exists a neighborhood $U$ of $a$ such that for $b \in U$ and $z \in \bigcup_j \Gamma_j$,
$$|\mathfrak{p}_b(z) - \mathfrak{p}_a(z)| < \epsilon < |\mathfrak{p}_a(z)|.$$
Thus $|\mathfrak{p}_a(z)| > |\mathfrak{p}_b(z) - \mathfrak{p}_a(z)|$ on each $\Gamma_j$.

By Rouche's theorem, $\mathfrak{p}_b$ has the same number of zeros (counting multiplicity) inside $\Gamma_j$ as $\mathfrak{p}_a$. Hence if $\rho_k a = r_j$, then $\rho_k b \in W_j$, establishing continuity.