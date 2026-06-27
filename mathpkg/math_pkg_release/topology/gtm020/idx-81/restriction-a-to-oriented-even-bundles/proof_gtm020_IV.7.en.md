---
role: proof
locale: en
of_concept: restriction-a-to-oriented-even-bundles
source_book: gtm020
source_chapter: "IV"
source_section: "7"
---

The construction of $a$ and $m$ proceeds as in the proof of Theorem (4.3): paragraph 1 for the construction and paragraphs 2 and 3 for the monomorphic character of $a$ and $m$ as semigroup morphisms.

Let $\eta$ be the oriented $4$-plane bundle over $\mathbb{CP}^n \times \mathbb{CP}^n$ which is the Whitney sum $\eta_1 \oplus \eta_2$, where $\eta_i = \mathrm{pr}_i^*(\varepsilon_0(\gamma))$ for $i = 1, 2$. Observe that $\varepsilon_0(\gamma) = \gamma_2^+$ over $\mathbb{CP}^n = G_2^+(\mathbb{R}^{2n+2})$. Then $H^*(\mathbb{CP}^n \times \mathbb{CP}^n, R)$ is the polynomial ring $R[x, y]$ modulo the relations $x^{n+1} = 0$ and $y^{n+1} = 0$.

We have
$$a(\phi)(x) + a(\phi)(y) = \phi(\eta_1 \oplus \eta_2) = \phi(\eta_1^* \oplus \eta_2^*) = a(\phi)(-x) + a(\phi)(-y)$$
and
$$m(\phi)(x) m(\phi)(y) = \phi(\eta_1 \oplus \eta_2) = \phi(\eta_1^* \oplus \eta_2^*) = m(\phi)(-x) m(\phi)(-y)$$
since reversing the orientation of both $\eta_1$ and $\eta_2$ leaves the orientation of $\eta_1 \oplus \eta_2$ unchanged. By writing a power series $f(t) = g_1(t^2) + t g_2(t^2)$, we conclude that $a(\phi)(t) \in R^+[[t]]$ and $m(\phi)(t) \in R^\pm[[t]]$.
