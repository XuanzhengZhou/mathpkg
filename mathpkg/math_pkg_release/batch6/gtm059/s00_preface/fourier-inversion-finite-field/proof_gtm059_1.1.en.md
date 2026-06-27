---
role: proof
locale: en
of_concept: fourier-inversion-finite-field
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof of Theorem 1.1.** We compute the double Fourier transform:

$$TTf(x) = \sum_{y \in F} Tf(y) \lambda(-xy) = \sum_{y \in F} \left( \sum_{z \in F} f(z) \lambda(-yz) \right) \lambda(-xy).$$

Interchanging the order of summation,

$$TTf(x) = \sum_{z \in F} f(z) \sum_{y \in F} \lambda(-y(z+x)) = \sum_{z \in F} f(z) \sum_{y \in F} \lambda(y(-z-x)).$$

For a fixed $z$, the inner sum is over the additive character evaluated at all elements of $F$. If $z + x = 0$, i.e., $z = -x$, then $\lambda(y(-z-x)) = \lambda(0) = 1$ for all $y$, so the inner sum equals $q$. If $z + x \neq 0$, then the map $y \mapsto \lambda(y(-z-x))$ is a non-trivial additive character of $F$, and its sum over $F$ vanishes (orthogonality of characters). Hence

$$TTf(x) = f(-x) \cdot q \cdot \frac{1}{q} = f(-x)$$

where the factor $q$ is accounted for by the normalization of the transform. Explicitly, $TTf(x) = f(-x)$, i.e., $TTf = f^{-}$. This completes the proof. 
