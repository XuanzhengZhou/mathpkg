---
role: proof
locale: en
of_concept: w-c-embedded-in-w-star
source_book: gtm043
source_chapter: "5"
source_section: "5.13"
---

By 5.12(c), for each $f \in C(W)$, there exists $\alpha < \omega_1$ and $r \in \mathbb{R}$ such that $f[W - W(\alpha)] = \{r\}$. Define $f^\beta \in C(W^*)$ by setting $f^\beta(\sigma) = f(\sigma)$ for $\sigma \in W$, and $f^\beta(\omega_1) = r$. Since $f$ is constant on a tail, $f^\beta$ is continuous at $\omega_1$, hence $f^\beta \in C(W^*)$. This extension is the unique continuous extension of $f$.

Conversely, given $g \in C(W^*)$, the restriction $g|_W$ belongs to $C(W)$. The maps $f \mapsto f^\beta$ and $g \mapsto g|_W$ are mutually inverse, establishing an isomorphism between $C(W^*)$ and $C(W)$. Thus $W$ is $C$-embedded in $W^*$.
