---
role: proof
locale: en
of_concept: discriminant-of-basis-theorem
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

The discriminant, like the different, is determined by local data. For a prime ideal $\mathfrak{p}$ of $R$ with complement $M$, the discriminant $\mathfrak{d}_M$ of $R'_M$ over $R_M$ equals $\mathfrak{d} R_M$, and the exponent of $\mathfrak{p}$ in $\mathfrak{d}$ equals $\sum_{\mathfrak{P} \cap R = \mathfrak{p}} f(\mathfrak{P}) m(\mathfrak{P})$.

Since $R_M$ is a PID, $R'_M$ admits a basis $\{u_1, \dots, u_n\}$ over $R_M$ (Corollary 2 to Theorem 7, §4). Construct elements $v_1, \dots, v_n$ by $T(u_i v_j) = \delta_{ij}$. Then $\{v_1, \dots, v_n\}$ forms a basis of the complementary module $\mathcal{C}_M$ over $R_M$.

The complementary module is a principal fractionary ideal in the local case; write $\mathcal{C}_M = R'_M y$. Then $\{y u_1, \dots, y u_n\}$ is also a basis of $\mathcal{C}_M$. Computing discriminants gives $d(yu) = (N(y))^2 d(u)$. Since $d(u) d(v) = 1$ in $K$, we get $(N(y) d(u))^2$ is a unit in $R_M$, so $N(y) d(u)$ is a unit. By Lemma 3, $N(y)^{-1}$ generates $\mathfrak{d}_M$, hence $\mathfrak{d}_M = R_M d(u)$.

For the global statement, $\{u_1, \dots, u_n\}$ is an integral basis if and only if it's a basis of $R'_M$ over $R_M$ for every $\mathfrak{p}$, which holds exactly when $\mathfrak{d}_{R'/R} = R \cdot d(u)$.
