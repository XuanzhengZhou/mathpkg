---
role: proof
locale: en
of_concept: frenet-equations-skew-symmetric
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

Since the vectors $e_1(t), \ldots, e_n(t)$ form a basis of $\mathbb{R}^n$ for each $t$, the derivatives $\dot{e}_i(t)$ can be expressed uniquely as linear combinations $\dot{e}_i(t) = \sum_j \omega_{ij}(t) e_j(t)$.

(i) Differentiating the orthonormality condition $e_i(t) \cdot e_j(t) = \delta_{ij}$ yields $\dot{e}_i \cdot e_j + e_i \cdot \dot{e}_j = 0$. Substituting the Frenet equations gives $\omega_{ij} + \omega_{ji} = 0$, proving skew-symmetry.

(ii) For the distinguished Frenet frame, $e_i(t)$ lies in the span of $\dot{c}(t), \ldots, c^{(i)}(t)$ by construction. Therefore $\dot{e}_i(t)$ lies in the span of $\dot{c}(t), \ldots, c^{(i+1)}(t)$ and hence in the span of $e_1(t), \ldots, e_{i+1}(t)$. This means $\omega_{ij} = 0$ for $j > i+1$. By skew-symmetry, $\omega_{ij} = 0$ whenever $|i-j| \geq 2$.
