---
role: proof
locale: en
of_concept: existence-of-metrically-transitive-automorphisms
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

The category method can be applied to the space $M$ of all measure-preserving automorphisms of the unit square $X = [0,1]^2$, equipped with the uniform metric

$$\varrho(S, T) = \sup_{x \in X} |Sx - Tx|.$$

This space is topologically complete (being a closed subspace of the complete space of all automorphisms of $X$, whose completeness follows from the same argument as in the 1-dimensional case of Chapter 13). One then defines, for each pair of basic open sets $U_i, U_j$ in a countable base for $X$, the set

$$E_{ij} = \left\{ T \in M : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

Each $E_{ij}$ is open in $M$. To show density, fix $T \in M$ and $\varepsilon > 0$. One constructs a perturbation $S$ of $T$ (using the technique described in the text: joining a point of $U_i$ to a point of $U_j$ by a line segment, choosing nonperiodic points along it, and exploiting the fact that recurrent points and nonperiodic points each form residual sets) such that $\varrho(S, T) < \varepsilon$ and $S \in E_{ij}$. Hence each $E_{ij}$ is dense open, and by the Baire category theorem for topologically complete spaces,

$$\bigcap_{i,j} E_{ij} \neq \emptyset.$$

For any $T$ in this intersection, the sets

$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$

are open and dense in $X$, so $\bigcap_j G_j \neq \emptyset$ (again by Baire category in $X$). Any point $x \in \bigcap_j G_j$ has its positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersecting every $U_j$, hence dense in $X$. Moreover, by construction, $T$ preserves Lebesgue measure. Such a $T$ is called *metrically transitive*. The residual set $\bigcap_{i,j} E_{ij}$ therefore consists of metrically transitive automorphisms, establishing their existence. This method generalizes the earlier result of Oxtoby and Ulam [28].
