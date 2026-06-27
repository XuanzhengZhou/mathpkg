---
role: proof
locale: en
of_concept: product-polar-formula
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Proof.** Let $S = \prod_\alpha S_\alpha$ with $S_\alpha \in \mathfrak{S}_\alpha$. For any $y = (y_\alpha) \in G = \bigoplus_\alpha G_\alpha$, the condition $|\sum_\alpha \langle x_\alpha, y_\alpha \rangle| \leq 1$ for all $x = (x_\alpha) \in S$ is equivalent to $\sum_\alpha |\langle x_\alpha, y_\alpha \rangle| \leq 1$ for all $x \in S$, since one can vary a single component independently.

Let $\lambda_\alpha = \sup\{|\langle x_\alpha, y_\alpha \rangle| : x \in S\}$. Since $y$ has only finitely many non-zero components, and $S = \prod_\alpha S_\alpha$, it follows that $\lambda_\alpha = 0$ except for finitely many $\alpha \in A$, and $\sum_\alpha \lambda_\alpha \leq 1$. Now $y_\alpha \in \lambda_\alpha S_\alpha^\circ$; hence

$$y = \sum_\alpha y_\alpha \in \Gamma_\alpha S_\alpha^\circ,$$

which shows that $S^\circ = \Gamma_\alpha S_\alpha^\circ$.

Since the totality of sets $\{\Gamma_\alpha S_\alpha^\circ\}$ form a 0-neighborhood base for the locally convex direct sum of the $\mathfrak{S}_\alpha$-topologies (cf. (*) preceding (II, 6.2)), this topology is identical with the $\mathfrak{S}$-topology on $G$. $\square$
