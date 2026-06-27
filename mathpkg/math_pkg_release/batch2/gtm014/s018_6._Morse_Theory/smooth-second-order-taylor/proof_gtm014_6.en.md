---
role: proof
locale: en
of_concept: smooth-second-order-taylor
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

Since $g_i(a) = 0$, by Lemma 6.10 applied to each $g_i$, there exist smooth functions $h_{ij}: U \to \mathbb{R}$ such that
$$g_i(x) = \sum_{j=1}^{n} h_{ij}(x)(x_j - a_j).$$
Substituting into the first-order expansion $f(x) = f(a) + \sum_i g_i(x)(x_i - a_i)$ gives
$$f(x) = f(a) + \sum_{i,j=1}^{n} h_{ij}(x)(x_i - a_i)(x_j - a_j).$$

Let $g_{ij} = \frac{1}{2}(h_{ij} + h_{ji})$. Then $g_{ij} = g_{ji}$ and
$$f(x) = f(a) + \sum_{i,j=1}^{n} g_{ij}(x)(x_i - a_i)(x_j - a_j).$$

To verify $g_{ij}(a) = \frac{1}{2} \frac{\partial^2 f}{\partial x_i \partial x_j}(a)$, differentiate both sides of the above equation with $\frac{\partial^2}{\partial x_i \partial x_j}$ and evaluate at $a$. The only terms on the right-hand side which do not vanish at $a$ are $g_{ij}(a)$ and $g_{ji}(a) = 2g_{ij}(a)$, giving the result.
