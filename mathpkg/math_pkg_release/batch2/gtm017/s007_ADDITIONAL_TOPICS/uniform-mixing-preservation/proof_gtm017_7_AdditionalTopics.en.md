---
role: proof
locale: en
of_concept: uniform-mixing-preservation
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Since $Y_t$ is measurable with respect to $\{X_u : t-L \leq u \leq t\}$, the past $\sigma$-field $\mathcal{B}_t^Y$ is contained in $\mathcal{B}_t^X$. Similarly, $\mathcal{F}_\tau^Y \subset \mathcal{F}_{\tau-L}^X$ because $Y_\tau$ depends on $X$ over $[\tau-L,\tau]$.

For any $B \in \mathcal{B}_t^Y$ and $F \in \mathcal{F}_\tau^Y$ with $t < \tau$, we have $B \in \mathcal{B}_t^X$ and $F \in \mathcal{F}_{\tau-L}^X$. Applying the uniform mixing condition for $X$:
$$|P(B \cap F) - P(B)P(F)| < g((\tau - L) - t).$$
Define $h(s) = g(s - L)$ for $s \geq L$ (extended suitably). Then $h(s) \to 0$ as $s \to \infty$, establishing uniform mixing for $Y_t$.
