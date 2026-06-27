---
role: proof
locale: en
of_concept: argument-principle
source_book: gtm011
source_chapter: "V"
source_section: "3"
---

**Proof.** Suppose $f$ has a zero of order $m$ at $z = a$. Then $f(z) = (z-a)^m g(z)$ where $g$ is analytic and $g(a) \neq 0$. Taking the logarithmic derivative gives

$$
\frac{f'(z)}{f(z)} = \frac{m}{z-a} + \frac{g'(z)}{g(z)},
$$

and $g'/g$ is analytic near $z = a$ since $g(a) \neq 0$. Thus $f'/f$ has a simple pole at $z = a$ with residue $m$.

Similarly, if $f$ has a pole of order $m$ at $z = a$, write $f(z) = (z-a)^{-m} g(z)$ where $g$ is analytic and $g(a) \neq 0$. Then

$$
\frac{f'(z)}{f(z)} = \frac{-m}{z-a} + \frac{g'(z)}{g(z)},
$$

so $f'/f$ has a simple pole at $z = a$ with residue $-m$.

Since $f$ is meromorphic on $G$, the function $f'/f$ is meromorphic on $G$ with simple poles precisely at the zeros and poles of $f$, and the residues are the multiplicities (positive for zeros, negative for poles). Let $\{a_j\}$ be the zeros of $f$ and $\{b_k\}$ the poles of $f$. The function $f'/f$ has no other singularities in $G$. By the Residue Theorem,

$$
\frac{1}{2\pi i} \int_{\gamma} \frac{f'(z)}{f(z)} \, dz = \sum_{j} n(\gamma; a_j) \, \operatorname{Res}\!\left(\frac{f'}{f}; a_j\right) + \sum_{k} n(\gamma; b_k) \, \operatorname{Res}\!\left(\frac{f'}{f}; b_k\right)
$$

$$
= \sum_{j} n(\gamma; a_j) \, m(a_j) - \sum_{k} n(\gamma; b_k) \, m(b_k),
$$

where $m(a_j)$ is the multiplicity of the zero $a_j$ and $m(b_k)$ is the order of the pole $b_k$. This completes the proof. $\square$
