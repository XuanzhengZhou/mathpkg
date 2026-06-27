---
role: proof
locale: en
of_concept: projective-space-immersion-embedding-condition
source_book: gtm020
source_chapter: "10"
source_section: "10.3"
---

When $n = 2^r$, then
$$w(\mathbf{RP}^n) = (1 + x)^{2^r}(1 + x) = 1 + x + x^n$$
and
$$\tilde{w}(\mathbf{RP}^n) = (1 + x + x^n)^{-1} = (1 + x^n)(1 + x + \cdots + x^n) = 1 + x + \cdots + x^{n-1}.$$
Therefore, $\tilde{w}_i(\mathbf{RP}^n) \neq 0$ for $0 \leq i \leq n-1$ and $\tilde{w}_i(\mathbf{RP}^n) = 0$ for $n \leq i$.

In summary, the theorem follows by applying the vanishing conditions of (10.2). For $n = 2^r$, we have $\tilde{w}_i(\mathbf{RP}^n) \neq 0$ for $i \leq n-1$. If an immersion $\mathbf{RP}^n \to \mathbf{R}^{n+1}$ existed, then by (10.2) we would need $\tilde{w}_i(\mathbf{RP}^n) = 0$ for $i > 1$, which forces $n-1 \leq 1$, i.e., $n \leq 2$. Combined with the computation of $\tilde{w}(\mathbf{RP}^n)$, the only possible $n$ are $2^r - 1$ or $2^r - 2$ for immersion, and $2^r - 1$ for embedding. For $n = 2^r$, the stronger non-immersion into $\mathbf{R}^{2n-2}$ follows similarly from the non-vanishing of the dual classes up to dimension $n-1$.
