---
role: proof
locale: en
of_concept: projective-tensor-product-nuclear
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

To prove that $E \hat{\otimes} F$ is nuclear, it suffices by Theorem 7.2(c) to show that for every convex, circled $0$-neighborhood $W$ of the projective topology on $E \otimes F$, the canonical map $\phi_W: E \otimes F \to \widetilde{(E \otimes F)}_W$ is nuclear.

Let $W$ be of the form $\Gamma(U \otimes V)$ where $U$ and $V$ are convex, circled $0$-neighborhoods in $E$ and $F$ respectively. By nuclearity of $E$ and $F$, the canonical maps $\phi_U: E \to \tilde{E}_U$ and $\phi_V: F \to \tilde{F}_V$ are nuclear. Hence by (7.1) they admit representations
$$\phi_U = \sum_{i=1}^{\infty} \lambda_i f_i \otimes \hat{x}_i, \quad \phi_V = \sum_{j=1}^{\infty} \mu_j g_j \otimes \hat{y}_j$$
with $\sum |\lambda_i| < +\infty$, $\sum |\mu_j| < +\infty$, equicontinuous families $\{f_i\} \subset E'$, $\{g_j\} \subset F'$, and bounded families $\{\hat{x}_i\} \subset \tilde{E}_U$, $\{\hat{y}_j\} \subset \tilde{F}_V$.

Then the canonical map $\phi_W$ on $E \otimes F$, considered as an element of the completed tensor product, can be expressed as
$$\phi_W(x \otimes y) = \sum_{i,j=1}^{\infty} \lambda_i \mu_j f_i(x) g_j(y) (\hat{x}_i \otimes \hat{y}_j).$$

The family $\{\lambda_i \mu_j : (i,j) \in \mathbb{N} \times \mathbb{N}\}$ is summable (since it is the tensor product of summable families), the family $\{f_i \otimes g_j\}$ is equicontinuous (uniformly bounded on $\Gamma(U_1 \otimes V_1)$ for suitable neighborhoods $U_1$, $V_1$), and the family $\{\hat{x}_i \otimes \hat{y}_j\}$ is bounded in $\widetilde{G}_W$ because $\|\hat{x}_i \otimes \hat{y}_j\| = \|\hat{x}_i\| \|\hat{y}_j\|$. Hence $\phi_W$ is nuclear for each element $W$ of a $0$-neighborhood base of the projective topology on $E \otimes F$, and the nuclearity of $E \hat{\otimes} F$ follows from Theorem 7.2(c) (or equivalently from (7.1), Corollary 3).
