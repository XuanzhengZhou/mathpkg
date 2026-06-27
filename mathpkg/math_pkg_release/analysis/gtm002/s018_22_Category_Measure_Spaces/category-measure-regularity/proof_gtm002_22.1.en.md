---
role: proof
locale: en
of_concept: category-measure-regularity
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

Let $G$ be an open set in $X$. Since $X$ is a regular Baire space, $G$ can be expressed as the union of a family $\{U_i\}$ of open sets whose closures are contained in $G$: $\overline{U}_i \subset G$ for each $i$. The category measure $\mu$ is defined on the $\sigma$-algebra of sets having the property of Baire, and open sets have the property of Baire, so each $U_i$ is measurable and $\mu(U_i) \leq \mu(\overline{U}_i) \leq \mu(G)$.

Since $\mu$ is finite and countably additive, and $\{U_i\}$ is an open cover of $G$, we have $\mu(G) = \mu(\bigcup_i U_i)$. By countable additivity and the fact that the family is directed under inclusion, we can select a countable subfamily (still denoting it $\{U_i\}_{i=1}^{\infty}$) such that $\mu(G) = \sum_{i=1}^{\infty} \mu(U_i)$. Choose $n$ sufficiently large so that $\sum_{i=1}^{n} \mu(U_i) > \mu(G) - \varepsilon$. Then setting $F = \bigcup_{i=1}^{n} \overline{U}_i$, we have $F$ is a closed subset of $G$ and
$$\mu(F) \geq \mu\left(\bigcup_{i=1}^{n} U_i\right) = \sum_{i=1}^{n} \mu(U_i) > \mu(G) - \varepsilon.$$
This proves the first assertion (inner regularity for open sets).

The second assertion (outer regularity for closed sets) follows by complementation: if $F$ is closed, then $X \setminus F$ is open, so by the first part there exists a closed set $C \subset X \setminus F$ with $\mu(C) > \mu(X \setminus F) - \varepsilon$. Then $G = X \setminus C$ is an open superset of $F$ and $\mu(G) = \mu(X) - \mu(C) < \mu(X) - [\mu(X \setminus F) - \varepsilon] = \mu(F) + \varepsilon$.
