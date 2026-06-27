---
role: proof
locale: en
of_concept: double-annihilator-is-closure
source_book: gtm031
source_chapter: "Chapter VIII: The Ring of Linear Transformations"
source_section: "8. Dual spaces. Kronecker products"
---
**Proof.** It follows directly from the definition of the topologies that subspaces of the form $j(\mathfrak{S})$, $j(\mathfrak{S}')$ are closed. Since $j(j(\mathfrak{S}')) \supseteq \mathfrak{S}'$, we have $j(j(\mathfrak{S}')) \supseteq \operatorname{Cl} \mathfrak{S}'$.

Conversely, let $u' \in j(j(\mathfrak{S}'))$. By the definition of the R-topology, every basic open neighborhood of $u'$ is determined by finitely many vectors $x_1, \ldots, x_m$ in $\mathfrak{R}$. Using the duality properties and the fact that $u'$ annihilates all vectors that annihilate $\mathfrak{S}'$, one shows that each such neighborhood intersects $\mathfrak{S}'$. Hence $u' \in \operatorname{Cl} \mathfrak{S}'$, proving $j(j(\mathfrak{S}')) = \operatorname{Cl} \mathfrak{S}'$. The second statement follows immediately.
