---
role: proof
locale: en
of_concept: theorem-6-structure-dense-rings
source_book: gtm031
source_chapter: "IX"
source_section: "10"
---
**First direction.** Let $\mathfrak{R}'$ be a total subspace of $\mathfrak{R}^*$ and let $\mathfrak{A}$ be a subring of $\mathfrak{L}(\mathfrak{R}' \mid \mathfrak{R})$ containing $\mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$. We first show that $\mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$ contains non-zero transformations. Let $\phi_1, \phi_2, \cdots, \phi_m$ be non-zero elements of $\mathfrak{R}'$, let $u_1, u_2, \cdots, u_m$ be arbitrary vectors in $\mathfrak{R}$, and set $F = \sum_{i=1}^m \phi_i \times u_i$. Then $F$ is of finite rank. For any linear function $f$, we have $fF^*(x) = \sum \phi_i(x) f(u_i)$, so $fF^*$ is a linear combination of the $\phi_i$, hence $F^* \in \mathfrak{L}(\mathfrak{R}' \mid \mathfrak{R})$. Thus $F \in \mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$, showing this set is non-zero.

We prove that $\mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$ is dense. Let $(y_1, \cdots, y_m)$ be linearly independent and $(u_1, \cdots, u_m)$ arbitrary. Since $\mathfrak{R}'$ is total, there exist $\phi_i \in \mathfrak{R}'$ with $\phi_i(y_j) = \delta_{ij}$. Then $F = \sum \phi_i \times u_i \in \mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$ satisfies $y_i F = u_i$. Hence $\mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$ is dense, and therefore $\mathfrak{A}$ is dense.

**Conversely**, let $\mathfrak{A}$ be a dense ring containing non-zero finite rank transformations. Define
$$\mathfrak{R}' = \{ fF^* \mid f \in \mathfrak{R}^*, F \in \mathfrak{J} \cap \mathfrak{A} \}.$$
Since $\mathfrak{J} \cap \mathfrak{A}$ is a non-zero two-sided ideal in $\mathfrak{A}$, Lemma 1 implies $\mathfrak{J} \cap \mathfrak{A}$ is irreducible. If $x \neq 0$, we can find $F \in \mathfrak{J} \cap \mathfrak{A}$ with $xF \neq 0$, and a linear function $f$ with $f(xF) \neq 0$. Then $fF^*(x) \neq 0$ and $fF^* \in \mathfrak{R}'$, proving $\mathfrak{R}'$ is total.

For $A \in \mathfrak{A}$, we have $\mathfrak{R}'A^* = \sum \mathfrak{R}^* F^* A^* = \sum \mathfrak{R}^*(AF)^* \subseteq \mathfrak{R}'$ since $\mathfrak{J} \cap \mathfrak{A}$ is an ideal. Thus $\mathfrak{A} \subseteq \mathfrak{L}(\mathfrak{R}' \mid \mathfrak{R})$. The reverse inclusion $\mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R}) \subseteq \mathfrak{A}$ follows from Lemma 2.
