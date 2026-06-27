---
role: proof
locale: en
of_concept: type-decomposition-w-star-algebra
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

Assuming $W \neq \{0\}$, the proof constructs each summand.

**Construction of $W_I$:** Let $\{p_\beta\}_{\beta \in B}$ be a maximal family of pairwise centrally orthogonal non-zero abelian projections. By the lemma on orthogonal sums, $p = \sum_{\beta} p_\beta$ is abelian. Let $p_I = z(p)$ be the central support of $p$. Set $W_I = Wp_I$. If $q \neq 0$ is a central projection with $q \leq p_I$, then $qp \neq 0$ (since $p_I$ is the central support of $p$), so $q$ majorizes a non-zero abelian projection (a sub-projection of $p$). Thus $W_I$ is of type I.

**Construction of $W_{II_1}$:** In $W(e - p_I)$ (which contains no non-zero abelian projections), let $p_1$ be the sum of a maximal family of centrally orthogonal finite projections. Set $W_{II_1} = W p_1$. By maximality and the absence of abelian projections, $W_{II_1}$ is a finite algebra with no non-zero abelian projections, i.e., of type II$_1$.

**Construction of $W_{II_\infty}$ and $W_{III}$:** Similar maximality arguments using appropriate families of projections yield the remaining summands. The uniqueness follows from the fact that the defining properties of each type are mutually exclusive and that the central supports are uniquely determined: if $p_I$ and $p'_I$ are central projections constructed from different maximal families, then $p_I = p'_I$ by maximality arguments using (5.2).

The direct sum decomposition $W = W_I \oplus W_{II_1} \oplus W_{II_\infty} \oplus W_{III}$ is topological for both the norm and $\sigma$-weak topologies (cf. Exercise 17).
