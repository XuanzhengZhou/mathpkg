---
role: proof
locale: en
of_concept: direct-sum-decomposition-of-dual-space
source_book: gtm023
source_chapter: "II"
source_section: "2.30"
---

Let $\pi_1: E \rightarrow E_1$ and $\pi_2: E \rightarrow E_2$ be the canonical projections associated with the direct decomposition $E = E_1 \oplus E_2$. Let $f \in L(E)$ be any linear function, and define functions $f_1, f_2$ by

$$f_1(x) = f(\pi_2 x) \quad \text{and} \quad f_2(x) = f(\pi_1 x).$$

It follows that $f_i \in E_i^\perp$ ($i = 1, 2$) and $f = f_1 + f_2$. Consequently,

$$L(E) = E_1^\perp + E_2^\perp.$$

To show that the decomposition is direct, assume that $f \in E_1^\perp \cap E_2^\perp$. Then $f(x) = 0$ for $x \in E_1$ and $x \in E_2$, and since every $x \in E$ can be written as $x = x_1 + x_2$ with $x_i \in E_i$, we have $f(x) = 0$ for all $x \in E$, so $f = 0$.

Moreover, the restriction of the scalar product to $E_i, E_j^\perp$ ($i \neq j$) is non-degenerate, and

$$E_i^\perp \cong L(E_j) \quad (i \neq j).$$
