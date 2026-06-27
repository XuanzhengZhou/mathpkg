---
role: proof
locale: en
of_concept: alexanders-theorem-on-homeomorphism-of-ball
source_book: gtm047
source_chapter: ""
source_section: ""
---

Define $\phi: \mathbf{B}^n \times [0, 1] \to \mathbf{B}^n$ as follows:

$$\phi(P, 0) = P \quad \text{for every } P;$$

$$\phi(P, t) = P \quad \text{for } \|P\| \geq t > 0;$$

$$\phi(P, t) = t f_1\!\left(\frac{P}{t}\right) \quad \text{for } 0 < \|P\| \leq t.$$

When $t = 1$, we have $\phi(P, 1) = f_1(P)$ for all $P$. For each $t \in [0, 1]$, the mapping $P \mapsto \phi(P, t)$ is a homeomorphism of $\mathbf{B}^n$ onto itself which fixes the boundary $\mathbf{S}^{n-1}$. At $t = 0$, $\phi(P, 0) = P$ is the identity. Thus $\phi$ is an isotopy from the identity to $f_1$.
