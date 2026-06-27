---
role: proof
locale: en
of_concept: extension-of-linear-functionals
source_book: gtm036
source_chapter: "0"
source_section: "E"
---

Let $B_F$ be a Hamel basis for the subspace $F$. Since $F \subseteq E$, the linearly independent set $B_F$ can be extended to a Hamel basis $B_E$ for $E$ (this requires the Axiom of Choice / Zorn's Lemma). Write $B_E = B_F \cup B'$ where $B'$ is disjoint from $B_F$.

Define $\tilde{f} : E \to K$ as follows. Every $x \in E$ has a unique representation as a finite linear combination of basis vectors:
$$
x = \sum_{b \in B_F} \lambda_b b + \sum_{b' \in B'} \mu_{b'} b',
$$
with only finitely many non-zero coefficients. Set
$$
\tilde{f}(x) = \sum_{b \in B_F} \lambda_b f(b) + \sum_{b' \in B'} \mu_{b'} \cdot 0 = \sum_{b \in B_F} \lambda_b f(b).
$$

When $x \in F$, the $B'$ coefficients are all zero, so $\tilde{f}(x) = f(x)$. Linearity of $\tilde{f}$ follows from the uniqueness of the basis representation: for $x, y \in E$ and $\alpha \in K$,
$$
\tilde{f}(x + y) = \tilde{f}(x) + \tilde{f}(y), \quad \tilde{f}(\alpha x) = \alpha \tilde{f}(x).
$$

Thus $\tilde{f}$ is a linear functional on $E$ extending $f$.
