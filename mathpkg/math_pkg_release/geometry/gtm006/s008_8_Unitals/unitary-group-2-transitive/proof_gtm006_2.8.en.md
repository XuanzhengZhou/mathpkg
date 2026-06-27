---
role: proof
locale: en
of_concept: unitary-group-2-transitive
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* By the corollary to Theorem 2.49, any two non-empty unitals are equivalent, so it suffices to work with the canonical form. Choose $X = \langle(1,0,0)\rangle$ as a point of $\mathcal{U}$.

Consider the matrix
$$S = \begin{bmatrix} 1 & 0 & 0 \\ s & 1 & 0 \\ a^{1+\phi} & a & 1 \end{bmatrix}$$
where $a \in K$ is arbitrary and $s = a^{\phi}(1 + c^{\phi}c^{-1})$. This matrix fixes $X$ and maps an arbitrary point $(y^{1+\phi} + c^{-1}k, y, 1)$ of $\mathcal{U}$ to another point of $\mathcal{U}$, as verified by direct computation using the unital equation. Since $a$ can be chosen to achieve any desired image, the stabilizer of $X$ is transitive on $\mathcal{U} \setminus \{X\}$.

Since $X$ was an arbitrary point of $\mathcal{U}$ and the full group $\Gamma$ is transitive on $\mathcal{U}$ (by considering the orbit of $X$), it follows that $\Gamma$ is $2$-transitive on the points of $\mathcal{U}$. $\square$