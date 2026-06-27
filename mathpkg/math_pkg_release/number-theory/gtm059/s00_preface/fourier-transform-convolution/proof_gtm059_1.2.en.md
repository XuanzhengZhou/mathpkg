---
role: proof
locale: en
of_concept: fourier-transform-convolution
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof of Theorem 1.2.** We compute:

$$T(f * g)(x) = \sum_{y \in F} (f * g)(y) \lambda(-xy) = \sum_{y \in F} \left( \sum_{z \in F} f(z) g(y-z) \right) \lambda(-xy).$$

Interchanging the order of summation and making the change of variables $t = y - z$, so $y = z + t$,

$$T(f * g)(x) = \sum_{z \in F} f(z) \sum_{t \in F} g(t) \lambda(-x(z+t)) = \sum_{z \in F} f(z) \lambda(-xz) \sum_{t \in F} g(t) \lambda(-xt) = Tf(x) \cdot Tg(x).$$

Thus $T(f * g) = Tf \cdot Tg$. For the dual formula, write $f = T\varphi$ and $g = T\psi$ for unique $\varphi, \psi$ (since $T$ is an isomorphism by Theorem 1.1). Then $T(fg) = T(T\varphi \cdot T\psi) = T(T(\varphi * \psi)) = q \cdot (\varphi * \psi)^{-}$ up to normalization; more directly, applying $T$ to both sides of the first formula yields the second formula with factor $1/q$ after accounting for the normalization constant. 
