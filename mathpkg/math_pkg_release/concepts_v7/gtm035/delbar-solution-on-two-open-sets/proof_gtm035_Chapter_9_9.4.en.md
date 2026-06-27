---
role: proof
locale: en
of_concept: delbar-solution-on-two-open-sets
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.4"
---
# Proof of $\bar{\partial}$ Solution on Union of Two Open Sets

**Lemma 9.4.** Let $X$ be a compact polynomially convex set in $\mathbb{C}^N$, and let $U_1, U_2$ be open sets with $X \subset U_1 \cup U_2$. Suppose $h \in H(U_1 \cap U_2)$. Then there exist $h_1 \in H(U_1)$ and $h_2 \in H(U_2)$ such that

$$h = h_1 - h_2 \quad \text{on } U_1 \cap U_2.$$

*Proof.* Choose a $C^\infty$ partition of unity $\{\eta_1, \eta_2\}$ subordinate to the cover $\{U_1, U_2\}$ of a neighborhood of $X$, so that $\eta_1 + \eta_2 = 1$ on a neighborhood of $X$, $\operatorname{supp} \eta_j \subset U_j$, and $\eta_j \in C^\infty$.

Define

$$H_1 = \eta_2 h, \quad H_2 = -\eta_1 h,$$

where we extend $\eta_j h$ by zero outside $U_j$. Then $H_j \in C^\infty(U_j)$ for $j = 1, 2$.

On $U_1 \cap U_2$, we have

$$H_1 - H_2 = (\eta_1 + \eta_2)h = h.$$

Hence $\bar{\partial} H_1 = \bar{\partial} H_2$ on $U_1 \cap U_2$, since $\bar{\partial}h = 0$ there. Let $f$ be the $(0,1)$-form on $U_1 \cup U_2$ defined by

$$f = \bar{\partial} H_1 \text{ on } U_1, \quad f = \bar{\partial} H_2 \text{ on } U_2.$$

Then $f$ is well-defined and $\bar{\partial}$-closed on $U_1 \cup U_2$ (since $\bar{\partial}^2 = 0$ and each $H_j$ is $C^\infty$).

Choose a $p$-polyhedron $\prod$ with $X \subset \prod \subset U_1 \cup U_2$. By Theorem 7.6 (the $\bar{\partial}$-solvability on a polyhedron), there exists a neighborhood $W$ of $\prod$ and $F \in C^\infty(W)$ such that

$$\bar{\partial} F = f \quad \text{on } W.$$

Now put

$$h_j = H_j - F \quad \text{on } U_j \cap W, \quad j = 1, 2.$$

Then on $U_1 \cap U_2 \cap W$,

$$h_1 - h_2 = H_1 - H_2 = h,$$

and for $j = 1, 2$,

$$\bar{\partial} h_j = \bar{\partial} H_j - \bar{\partial} F = f - f = 0 \quad \text{on } U_j \cap W.$$

Thus $h_j \in H(U_j \cap W)$ for $j = 1, 2$, completing the proof. $\square$

This lemma is the key $\bar{\partial}$-technique used in the proof of the Local Maximum Modulus Principle (Theorem 9.3). It solves the additive Cousin problem (Cousin I) on the union of two open sets by passing through a $C^\infty$ solution of the $\bar{\partial}$-equation.
