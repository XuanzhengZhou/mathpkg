---
role: proof
locale: en
of_concept: iwasawa-structure-theorem
source_book: gtm059
source_chapter: "5. Iwasawa Theory and Ideal Class Groups"
source_section: "3. Modules over Z_p[[T]]"
---

**Proof.** Suppose that $M$ has generators $u_1, \dots, u_m$. Relative to such generators we can form the matrix of relations: all vectors $(\lambda_1, \dots, \lambda_m) \in A^m$ such that $\lambda_1 u_1 + \dots + \lambda_m u_m = 0$. Since $A$ is Noetherian, a finite number of rows generate all of them.

The proof proceeds by a sequence of *admissible operations* on the relation matrix $R$, each corresponding to an embedding or surjection with finite kernel and cokernel (i.e., a pseudo-isomorphism). These operations are:

**(O.1)** If $R$ contains a row $(j_1, j_2, \dots, j_n)$ with $i_1$ not divisible by $p$, replace $R$ by the matrix whose rows consist of $(j_1, \dots, j_n)$ together with the rows of $R$ whose first element is multiplied by $p$.

**(O.2)** If there exists an element $i_1$ that is distinguished (or equivalently $i_1$ is not divisible by $p$), form the module $M'$ by adjoining a new element $v$ to $M$ with relations $p^n = p_1 v_1$ and $i_1 = -(p_2 v_2 + \dots + i_n v_n)$. Then $M$ is embedded in $M'$ and $M'/M$ is finite.

**(O.3)** If $(\lambda_{i_1}, \dots, \lambda_{i_k})$ is also a relation and there exists an element $i$ not divisible by $p$, replace the row $P(\lambda_1, \dots, \lambda_k)$ by $(\lambda_1, \dots, \lambda_k)$. This corresponds to a surjection with finite kernel.

Row and column operations over $A$ are also allowed and are called admissible operations.

Given a matrix $R$ over $A$, define $\deg^0(R) = \min \deg^0(a_i)$ for $i \ge j$, where $\deg^0(a_i)$ ranges over all admissible transformations of $R$ which leave neither component $i$ nor component $j$ unchanged.

**Lemma.** Suppose that $R$ is in $(r-1)$-normal form and that $R$ can be transformed into a matrix which is in $r$-normal form with the same dimension as $R$. Then, using admissible operations with respect to each of the first $r-1$ rows, one may assume without loss of generality that any given power $p^k$ divides all elements of $R$, and that $R$ can be transformed into a diagonalized matrix.

A matrix is said to be in $r$-normal form if it has the shape
$$
\begin{pmatrix}
\lambda_1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_r & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & 0
\end{pmatrix}
\neq 0
$$
where each $\lambda_i$ ($i = 1, \dots, r$) is a distinguished polynomial with $\deg^0(R) = \deg \lambda_i$.

Applying the lemma repeatedly, one transforms the relation matrix into a diagonal matrix. Each diagonal entry is either a distinguished polynomial $f_i$ (possibly with a power of $p$) or zero. The corresponding module is thereby pseudo-isomorphic to a direct sum:
$$
M \sim A^r \oplus \bigoplus_i A/(f_i^{n_i}) \oplus \bigoplus_j A/(p^{m_j})
$$
where $r$ counts the number of zero rows in the final diagonal form (the free rank), and each $f_i$ is a distinguished irreducible polynomial. The uniqueness of this decomposition follows from the invariance of the elementary divisors under admissible transformations, completing the proof. $\square$
