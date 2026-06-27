---
role: proof
locale: en
of_concept: delbar-solution-on-two-open-sets
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.4"
---
# Proof of the $\bar{\partial}$ Solution on the Union of Two Open Sets

Let $X$ be a compact, polynomially convex set in $\mathbb{C}^n$ and $U_1, U_2$ open sets with $X \subset U_1 \cup U_2$. Let $h \in H(U_1 \cap U_2)$. We construct a neighborhood $W$ of $X$ and functions $h_j \in H(W \cap U_j)$, $j = 1, 2$, such that $h_1 - h_2 = h$ on $W \cap U_1 \cap U_2$.

**Step 1: Decomposition of $X$.** Write $X = X_1 \cup X_2$ where each $X_j$ is compact and $X_j \subset U_j$, $j = 1, 2$.

**Step 2: Partition of unity.** Choose $f_1 \in C_0^\infty(U_1)$ with $0 \leq f_1 \leq 1$ and $f_1 = 1$ on $X_1$. Similarly choose $f_2 \in C_0^\infty(U_2)$. Then $f_1 + f_2 \geq 1$ on $X$, so $f_1 + f_2 > 0$ in some neighborhood $V$ of $X$. In $V$, define

$$\eta_1 = \frac{f_1}{f_1 + f_2}, \quad \eta_2 = \frac{f_2}{f_1 + f_2}.$$

Then $\eta_1, \eta_2 \in C^\infty(V)$, $\eta_1 + \eta_2 \equiv 1$ on $V$, and $\operatorname{supp} \eta_j \subset U_j$. Without loss of generality, replace $U_j$ by $U_j \cap V$.

**Step 3: Construction of smooth extensions.** Define $H_j \in C^\infty(U_j)$ by

$$H_1 = \begin{cases} \eta_2 h & \text{in } U_1 \cap U_2 \\ 0 & \text{in } U_1 \setminus U_2 \end{cases}, \qquad
H_2 = \begin{cases} -\eta_1 h & \text{in } U_1 \cap U_2 \\ 0 & \text{in } U_2 \setminus U_1 \end{cases}.$$

Then on $U_1 \cap U_2$,

$$H_1 - H_2 = (\eta_1 + \eta_2)h = h.$$

Hence $\bar{\partial} H_1 = \bar{\partial} H_2$ on $U_1 \cap U_2$. Define a $(0,1)$-form $f$ on $U_1 \cup U_2$ by

$$f = \bar{\partial} H_1 \text{ on } U_1, \quad f = \bar{\partial} H_2 \text{ on } U_2.$$

Then $f$ is well-defined and $\bar{\partial}$-closed on $U_1 \cup U_2$ (since $\bar{\partial}^2 = 0$).

**Step 4: Solving $\bar{\partial}$.** Since $X \subset U_1 \cup U_2$ and $X$ is polynomially convex, by Lemma 7.4 we can choose a $p$-polyhedron $\Pi$ with $X \subset \Pi \subset U_1 \cup U_2$. By Theorem 7.6, there exists a neighborhood $W$ of $\Pi$ and $F \in C^\infty(W)$ such that $\bar{\partial} F = f$ on $W$.

**Step 5: Holomorphic corrections.** Define, for $j = 1, 2$,

$$h_j = H_j - F \quad \text{on } U_j \cap W.$$

Then $h_1 - h_2 = H_1 - H_2 = h$ on $U_1 \cap U_2 \cap W$, and

$$\bar{\partial} h_j = \bar{\partial} H_j - \bar{\partial} F = f - f = 0 \quad \text{on } U_j \cap W,$$

so $h_j \in H(U_j \cap W)$ as required. $\square$
