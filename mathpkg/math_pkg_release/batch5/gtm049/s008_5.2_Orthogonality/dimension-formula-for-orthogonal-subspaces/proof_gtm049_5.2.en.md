---
role: proof
locale: en
of_concept: dimension-formula-for-orthogonal-subspaces
source_book: gtm049
source_chapter: "5"
source_section: "5.2 Orthogonality"
---

Let $\dim V = n$ and $\dim M = m$. Choose a basis $a_1, \ldots, a_m$ of $V$ such that $a_1, \ldots, a_r$ span $M \cap V^{\top}$ (so $r = \dim(M \cap V^{\top})$). Then $a_{r+1}, \ldots, a_m$ together with $a_1, \ldots, a_r$ span $M$.

Consider the $m \times n$ matrix $A$ whose $i$-th row consists of the coordinates of $a_i \tilde{\sigma}$ with respect to the dual basis. A vector $b \in V$ lies in $M^{\perp}$ if and only if $\sigma(a_i, b) = 0$ for all $i = 1, \ldots, m$, which is equivalent to $A y^t = 0$ where $y$ is the coordinate vector of $b$.

Since $a_1, \ldots, a_r \in V^{\top}$, we have $a_i \tilde{\sigma} = 0$ for $i = 1, \ldots, r$, so the first $r$ rows of $A$ are zero. For $i > r$, the row $a_i \tilde{\sigma}$ is non-zero and the first $r$ rows being zero means the first $r$ rows are linearly independent from the rest (trivially).

By our choice of basis, the rows $a_{r+1}\tilde{\sigma}, \ldots, a_m\tilde{\sigma}$ are linearly independent. Thus exactly $m - r$ rows of $A$ are linearly independent.

Now appeal to Theorem 4 of Chapter III (p. 50), which states that there are $n - (m - r)$ linearly independent solutions of the equation $A y^t = 0$. Hence

$$\dim M^{\perp} = n - (m - r) = \dim V - (\dim M - \dim(M \cap V^{\top})),$$

from which equation (1) follows. The second equation is proved in the same way.

An alternative proof using the link between $\bot$, $\top$ and the annihilator mapping of §4.6 is also given: by Lemma 1, $M^{\perp} = (M\tilde{\sigma})^{\circ}$. Since $\dim(M\tilde{\sigma}) = \dim M - \dim(M \cap \operatorname{Ker}\tilde{\sigma}) = \dim M - \dim(M \cap V^{\top})$, the result follows from the dimension formula for annihilators.
