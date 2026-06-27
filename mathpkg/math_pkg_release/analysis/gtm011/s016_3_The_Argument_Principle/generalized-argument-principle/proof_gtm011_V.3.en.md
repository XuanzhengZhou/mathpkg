---
role: proof
locale: en
of_concept: generalized-argument-principle
source_book: gtm011
source_chapter: "V"
source_section: "3"
---

**Proof.** Let $a$ be a zero of $f$ of order $m$. Then $f(z) = (z-a)^m h(z)$ with $h$ analytic and $h(a) \neq 0$. Computing the logarithmic derivative,

$$
\frac{f'(z)}{f(z)} = \frac{m}{z-a} + \frac{h'(z)}{h(z)},
$$

where $h'/h$ is analytic near $a$. Multiplying by $g$,

$$
g(z) \frac{f'(z)}{f(z)} = \frac{m \, g(z)}{z-a} + g(z) \frac{h'(z)}{h(z)}.
$$

Since $g$ is analytic, $g(z) = g(a) + (z-a)k(z)$ with $k$ analytic. Hence

$$
\frac{m \, g(z)}{z-a} = \frac{m \, g(a)}{z-a} + m \, k(z),
$$

and the second term is analytic. Thus $\operatorname{Res}(g f'/f; a) = m \, g(a)$.

If $b$ is a pole of $f$ of order $m$, write $f(z) = (z-b)^{-m} h(z)$ with $h$ analytic and $h(b) \neq 0$. Then

$$
\frac{f'(z)}{f(z)} = \frac{-m}{z-b} + \frac{h'(z)}{h(z)},
$$

where $h'/h$ is analytic near $b$. Multiplying by $g$ and expanding $g(z) = g(b) + (z-b)\ell(z)$ gives

$$
g(z) \frac{f'(z)}{f(z)} = \frac{-m \, g(b)}{z-b} + \text{analytic part},
$$

so $\operatorname{Res}(g f'/f; b) = -m \, g(b)$.

The function $g f'/f$ is meromorphic on $G$ with singularities only at the zeros $\{a_j\}$ and poles $\{b_k\}$ of $f$. Applying the Residue Theorem yields

$$
\frac{1}{2\pi i} \int_{\gamma} g(z) \frac{f'(z)}{f(z)} \, dz = \sum_{j} n(\gamma; a_j) \, \operatorname{Res}\!\left(g \frac{f'}{f}; a_j\right) + \sum_{k} n(\gamma; b_k) \, \operatorname{Res}\!\left(g \frac{f'}{f}; b_k\right)
$$

$$
= \sum_{j} g(a_j) \, n(\gamma; a_j) \, m(a_j) - \sum_{k} g(b_k) \, n(\gamma; b_k) \, m(b_k).
$$

This completes the proof. $\square$
