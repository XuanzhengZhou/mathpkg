---
role: proof
locale: en
of_concept: theorem-1-2
source_book: gtm011
source_chapter: "Runge's Theorem"
source_section: "1. Runge's Theorem"
---

Proof. Suppose $f$ is analytic in $\{z: 0 < |z - a| < R\}$, and define $g(z) = (z - a)f(z)$ for $z \neq a

To show that $g$ is analytic we apply Morera’s Theorem. Let $T$ be a triangle in $B(a; R)$ and let $\Delta$ be the inside of $T$ together with $T$. If $a \notin \Delta$ then $T \sim 0$ in $\{z: 0 < |z-a| < R\}$ and so, $\int_T g = 0$ by Cauchy’s Theorem. If $a$ is a vertex of $T$ then we have $T = [a, b, c, a]$. Let $x \in [a, b]$ and $y \in [c, a]$ and form the triangle $T_1 = [a, x, y, a]$. If $P$ is the polygon $[x, b, c, y, x]$ then $\int_T g = \int_{T_1} g + \int_P g = \int_{T_1} g$ since $P \sim 0$ in the punctured disk. Since $g$ is continuous and $g(a) = 0$, for any $\epsilon > 0$ $x$ and $y$ can be chosen such that $|g(z)| \leq \epsilon/\ell$ for any $z$ on $T_1$, where $\ell$ is the length of $T$. Hence $|\int_T g| = |\int_{T_1} g| \leq \epsilon$; since $\epsilon$ was arbitrary we have $\int_T g = 0$.

If $a \in \Delta$ and $T = [x, y, z, x]$ then consider the triangles $T_1 = [x, y, a, x]$, $T_2 = [y, z, a, y]$, $T_3 = [z, x, a, z]$. From the preceding paragraph $\int_{T_j} g = 0$ for $j = 1, 2, 3$ and so, $\int_T g = \int_{T_1} g + \int_{T_2} g + \int_{T_3} g = 0$. Since this exhausts all possibilities, $g$ must be analytic by Morera’s Theorem. Since the converse is obvious, the proof of the theorem is complete
