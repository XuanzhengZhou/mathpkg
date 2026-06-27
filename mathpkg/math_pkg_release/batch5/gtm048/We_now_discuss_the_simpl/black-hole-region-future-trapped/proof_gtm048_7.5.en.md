---
role: proof
locale: en
of_concept: black-hole-region-future-trapped
source_book: gtm048
source_chapter: "7"
source_section: "7.5"
---

Let $V$ be the vector field physically equivalent to $-dv$. Then $g(V,V) = 0$ and $g(U,V) < 0$, so $V$ is future-pointing, lightlike, and nowhere parallel to $U$.

We compute $(d/ds)(r \circ \gamma)$: On $M_{II}$,
$$dr = 2\mu\left(1 - \frac{2\mu}{r}\right)\left(\frac{dv}{v} + \frac{du}{u}\right)$$
Since $r < 2\mu$ in $M_{II}$, we have $1 - 2\mu/r < 0$. Moreover, along any future-directed causal curve in $M_{II}$, the term $(dv/v + du/u)$ is non-positive. Therefore $d(r \circ \gamma)/ds \leq 0$, and in fact strictly negative for timelike curves.

Since $r$ is strictly decreasing along $\gamma$ for all $s \geq s_0$, and $r \to 0$ corresponds to the singularity which is not part of $K$, the curve $\gamma$ can never return to the region where $r > 2\mu$ (i.e., region $M_I$). Hence $\gamma(\hat{\mathcal{E}}) \subset M_{II}$.
