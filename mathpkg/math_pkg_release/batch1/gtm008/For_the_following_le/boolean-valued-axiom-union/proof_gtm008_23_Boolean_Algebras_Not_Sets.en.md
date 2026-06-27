---
role: proof
locale: en
of_concept: boolean-valued-axiom-union
source_book: gtm008
source_chapter: "23"
source_section: "Boolean Algebras That Are Not Sets"
---

We must show that for any $u \in V^{(B)}$ (or $V^{(\tilde{B})}$),
$$\llbracket (\exists v)(\forall x)[x \in v \leftrightarrow (\exists y \in u)[x \in y]] \rrbracket = 1.$$

Define $v$ by
$$\mathcal{D}(v) = \bigcup_{y \in \mathcal{D}(u)} \mathcal{D}(y)$$
and for each $x \in \mathcal{D}(v)$,
$$v(x) = \llbracket (\exists y \in u)[x \in y] \rrbracket.$$

For $V^{(B)}$, one must verify that $v \in V^{(B)}$, which follows from the fact that $\mathcal{D}(v)$ is a set and $v(x) \in B$ for each $x$ (using Theorem 23.7 and the closure properties of $B$). For $V^{(\tilde{B})}$, the construction is direct.

The Boolean truth value $\llbracket (\forall x \in v)(\exists y \in u)[x \in y] \rrbracket = 1$ follows directly from the definition of $v$ and Theorem 23.7. It remains to show that $\llbracket (\forall y \in u)(\forall x \in y)[x \in v] \rrbracket = 1$. For any $y \in \mathcal{D}(u)$ and $x \in \mathcal{D}(y)$, we have $x \in \mathcal{D}(v)$ and need to verify $u(y) \cdot y(x) \leq v(x)$. This holds because $v(x)$ is defined as the supremum of $u(z) \cdot z(x)$ over all $z \in \mathcal{D}(u)$, and this supremum is at least $u(y) \cdot y(x)$. Hence the Boolean truth value evaluates to 1.
