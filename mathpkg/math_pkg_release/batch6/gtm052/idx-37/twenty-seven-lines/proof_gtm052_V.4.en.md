---
role: proof
locale: en
of_concept: twenty-seven-lines
source_book: gtm052
source_chapter: "V"
source_section: "4"
---

Let $X$ be the blowup of $\mathbf{P}^2$ at $P_1, \ldots, P_6$. By the description of the Picard group of a blowup, $\operatorname{Pic} X \cong \mathbb{Z}^7$ with basis $l, e_1, \ldots, e_6$ where $l$ is the pullback of a line class and $e_i$ is the class of $E_i$. A line $C \subset X \subset \mathbf{P}^3$ is a curve of degree 1 with respect to the hyperplane class $h = 3l - \sum e_i$. Using the adjunction formula and the fact that $C$ is a line in $\mathbf{P}^3$ (degree 1, genus 0), one obtains:

$$C.h = 1, \quad p_a(C) = 0.$$

Writing $C \sim al - \sum b_i e_i$, the conditions become:

$$3a - \sum b_i = 1, \quad a^2 - \sum b_i^2 = 1, \quad \text{and} \quad a \geqslant 0, b_i \geqslant 0.$$

Eliminating $\sum b_i$ gives $\sum b_i(b_i - 1) = a(a - 1)$. Solving the inequalities yields $a \leqslant 2$. By trial:
- If $a = 1$: then two $b_i = 1$, the rest 0, giving the 15 lines $F_{ij}$.
- If $a = 2$: then five $b_i = 1$, one $b_j = 0$, giving the 6 lines $G_j$.
Together with the 6 exceptional curves $E_i$, we obtain $6 + 15 + 6 = 27$ lines. That these are the only irreducible curves with negative self-intersection follows from the structure of the effective cone on a Del Pezzo surface.
