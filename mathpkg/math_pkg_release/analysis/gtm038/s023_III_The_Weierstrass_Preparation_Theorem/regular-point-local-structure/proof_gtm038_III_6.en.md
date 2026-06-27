---
role: proof
locale: en
of_concept: regular-point-local-structure
source_book: gtm038
source_chapter: "III"
source_section: "6. Analytic Sets"
---

**Proof.** Let $f_1, \ldots, f_{n-k}$ be holomorphic functions defining $M$ near $\mathfrak{z}_0$ with the Jacobian matrix $(\partial f_i / \partial z_j)$ having maximal rank $n-k$ at $\mathfrak{z}_0$ (by the definition of a regular point). Define $F: U \to \mathbb{C}^n$ by
$$F(z_1, \ldots, z_n) := (f_1(z_1, \ldots, z_n), \ldots, f_{n-k}(z_1, \ldots, z_n), z_{n-k+1} - z_{n-k+1}^{(0)}, \ldots, z_n - z_n^{(0)}).$$
The functional matrix of $F$ at $\mathfrak{z}_0$ is
$$\mathcal{F} := \begin{pmatrix} \left( \frac{\partial f_i}{\partial z_j} \right)_{i=1, \ldots, n-k} & \star \\ 0 & I_k \end{pmatrix}.$$
Then $\det \mathcal{F} \neq 0$ and there exist open neighborhoods $V(\mathfrak{z}_0) \subset U$, $W(0) \subset \mathbb{C}^n$ such that $F|V: V \to W$ is biholomorphic. But
$$F(V \cap M) = W \cap \{(w_1, \ldots, w_n) \in \mathbb{C}^n: w_1 = \cdots = w_{n-k} = 0\},$$
which is a plane segment of real dimension $2k$.
