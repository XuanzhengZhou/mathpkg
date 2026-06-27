---
role: proof
locale: en
of_concept: category-measure-regularity
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

By Theorem 4.6, any set $E$ having the property of Baire can be written as $E = G \triangle P$, where $G$ is regular open and $P$ is of first category. If we write $G = \phi(E)$, then $\phi$ is a function that selects a representative element from each equivalence class of $S$ modulo sets of first category.

Since $P$ is of first category, $\mu(P) = 0$ by the definition of a category measure. By Theorem 22.2, $P$ is nowhere dense. Therefore $\overline{E} = \overline{G}$, and since $G$ is regular open, $\operatorname{int}(\overline{E}) = G$. Consequently $\mu(E) = \mu(G) = \mu(\overline{E}) = \mu(\operatorname{int}(E))$.

The regularity equalities follow from Theorem 22.1, which provides the approximation of sets by open and closed sets with respect to the category measure. Specifically, for any $\varepsilon > 0$ there exists a closed $F \subset E$ with $\mu(F) > \mu(E) - \varepsilon$ and an open $G \supset E$ with $\mu(G) < \mu(E) + \varepsilon$.
