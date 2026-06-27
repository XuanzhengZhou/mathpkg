---
role: proof
locale: en
of_concept: proper-rotation-quaternion-representation
source_book: gtm023
source_chapter: "8"
source_section: "8.24"
---

Let $\sigma$ be a proper rotation of $E$ and define $\tau(x) = \sigma(x) \sigma(e)^{-1}$. Then $\tau(e) = e$, so $\tau$ restricts to a proper rotation of $E_1$ (the orthogonal complement of $e$). By Proposition I, there exists a unit vector $p$ such that $\tau(x) = pxp^{-1}$ for all $x \in E$. Then $\sigma(x) = \tau(x) \sigma(e) = pxp^{-1} \sigma(e) = axb^{-1}$ with $a = p$ and $b = \sigma(e)^{-1}p$.

For uniqueness: if $a_1 x b_1^{-1} = a_2 x b_2^{-1}$ for all $x \in E$, set $x = e$ to get $a_1 b_1^{-1} = a_2 b_2^{-1}$. Define $p = a_2^{-1} a_1 = b_2^{-1} b_1$. Then $pxp^{-1} = x$ for all $x \in E$, so by Proposition I, $p = \pm e$, yielding $a_2 = \varepsilon a_1$ and $b_2 = \varepsilon b_1$ with $\varepsilon = \pm 1$.
