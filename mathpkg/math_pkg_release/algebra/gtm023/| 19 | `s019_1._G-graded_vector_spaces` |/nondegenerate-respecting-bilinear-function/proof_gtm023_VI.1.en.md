---
role: proof
locale: en
of_concept: nondegenerate-respecting-bilinear-function
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

**Forward direction.** Suppose $\varphi$ is non-degenerate. Fix $k \in G$ and let $x \in E_k$ be such that $\varphi_k(x, y) = 0$ for all $y \in F_k$. Since $\varphi$ respects gradations, $\varphi(x, y) = 0$ for all $y \in F_j$ with $j \neq k$ (by orthogonality), and also for all $y \in F_k$ (by assumption). Hence $\varphi(x, y) = 0$ for all $y \in F$, and by non-degeneracy of $\varphi$, $x = 0$. Thus each $\varphi_k$ is non-degenerate. The argument is symmetric for $F_k$.

**Converse direction.** Suppose each $\varphi_k$ is non-degenerate. Let $x \in E$ satisfy $\varphi(x, y) = 0$ for all $y \in F$. Decompose $x = \sum_k x_k$ with $x_k \in E_k$. For any $y \in F_k$, we have $\varphi(x, y) = \varphi_k(x_k, y) = 0$ (all other terms vanish by orthogonality of distinct degrees). Since $\varphi_k$ is non-degenerate, $x_k = 0$ for each $k$, hence $x = 0$. Thus $\varphi$ is non-degenerate.

For the scalar product case: if $\varphi$ is a scalar product (i.e., a non-degenerate symmetric bilinear form) respecting the gradations, then each $\varphi_k$ is a non-degenerate bilinear form on $E_k \times F_k$, making $E_k$ and $F_k$ dual spaces. Therefore $\dim E_k = \dim F_k$ for all $k \in G$.
