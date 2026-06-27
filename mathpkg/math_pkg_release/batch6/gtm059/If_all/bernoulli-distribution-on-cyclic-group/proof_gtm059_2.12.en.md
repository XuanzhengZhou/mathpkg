---
role: proof
locale: en
of_concept: bernoulli-distribution-on-cyclic-group
source_book: gtm059
source_chapter: "2"
source_section: "12"
---

Let $y \in \frac{1}{N}\mathbb{Z}/\mathbb{Z}$ and let $M$ be a multiple of $N$. The elements in the inverse image of $y$ under the natural projection $\frac{1}{M}\mathbb{Z}/\mathbb{Z} \to \frac{1}{N}\mathbb{Z}/\mathbb{Z}$ are $y + \frac{j}{M}$ for $j = 0, 1, \dots, M/N - 1$. We must verify the distribution compatibility condition:
$$\varphi_N^{(k)}(y) = \sum_{j=0}^{M/N - 1} \varphi_M^{(k)}\!\left(y + \frac{j}{M}\right).$$

Substituting the definition and factoring out $N^{k-1}$, this is exactly the distribution relation (B.4):
$$N^{k-1} \sum_{j=0}^{M/N - 1} B_k\!\left( \left\langle y + \frac{j}{M} \right\rangle \right) = B_k(N \langle y \rangle).$$

Multiplying the distribution relation $B_k(X) = N^{k-1} \sum_{a=0}^{N-1} B_k(\frac{X+a}{N})$ by $M^{k-1}$ and setting $X = N\langle y \rangle$ yields precisely the required identity. The boundedness follows from the fact that $B_k(x)$ is a polynomial, hence bounded on $[0,1]$.
