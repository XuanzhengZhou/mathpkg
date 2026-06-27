---
role: proof
locale: en
of_concept: e1-structure-and-mapping-case-iii
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

When $k \geq 3$, as established in section 9.27 of the book, a linear transformation whose minimum polynomial is $(t-1)^k$ on a space with an indefinite inner product necessarily possesses an eigenvector on the light-cone. Let $e$ be such an eigenvector: $\varphi e = e$ and $(e, e) = 0$.

The orthogonal complement $E_1 = e^\perp = \{x \in E : (x, e) = 0\}$ has dimension $\dim E - 1 = 3$ (since $e \neq 0$ and the inner product is nondegenerate on $E$). Because $e \in E_1$ (as $(e, e) = 0$), the induced inner product on $E_1$ is degenerate. The rank of this induced form is $2$ (one dimension is lost to degeneracy along $e$), and the index is $2$ (cf. sec. 9.21).

Since the induced form on $E_1$ has index $2$ and rank $2$, there exists a $2$-dimensional subspace $F \subset E_1$ on which the inner product is positive definite. Choose an orthonormal basis $\{e_1, e_2\}$ of $F$.

Since $\varphi$ preserves the inner product and $\varphi e = e$, the subspace $E_1$ is invariant under $\varphi$ (if $(x, e) = 0$, then $(\varphi x, e) = (\varphi x, \varphi e) = (x, e) = 0$). The restriction $\varphi|_{E_1}$ thus maps $E_1$ to $E_1$. Expressed in the basis $\{e_1, e_2, e\}$, the matrix of $\varphi|_{E_1}$ has the given form, where the $2 \times 2$ block on $F$ is an orthogonal matrix (rotation by angle $\omega$) since $\varphi$ preserves the positive definite inner product on $F$ up to the degeneracy direction $e$.

To see that $\alpha_1$ and $\alpha_2$ are not both zero, suppose $\alpha_1 = \alpha_2 = 0$. Then $\varphi(F) \subset F$, so $F$ is invariant under $\varphi$. Since $\varphi e = e$, the $1$-dimensional subspace spanned by $e$ is also invariant. The decomposition $E = F \oplus F^\perp$ would then be a direct sum of invariant subspaces, each of dimension $2$. The minimum polynomial of $\varphi$ would then be the least common multiple of the minimum polynomials on each summand, of degree at most $2$, implying $k \leq 2$, contradicting $k \geq 3$. Hence at least one $\alpha_i \neq 0$.
