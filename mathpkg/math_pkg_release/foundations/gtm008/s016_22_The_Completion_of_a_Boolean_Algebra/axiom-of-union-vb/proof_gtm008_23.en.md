---
role: proof
locale: en
of_concept: axiom-of-union-vb
source_book: gtm008
source_chapter: "23"
source_section: "23. Boolean Algebras That Are Not Sets"
---

We have to show that for a given $u \in V^{(B)}$ or $u \in V^{(\tilde{B})}$,

$$\llbracket (\exists v) (\forall x) [x \in v \leftrightarrow (\exists y \in u) [x \in y]] \rrbracket = 1.$$

Define $v$ by

$$\mathcal{D}(v) = \bigcup_{y \in \mathcal{D}(u)} \mathcal{D}(y)$$

and

$$(\forall x \in \mathcal{D}(v))\, [v(x) = \llbracket (\exists y \in u) [x \in y] \rrbracket].$$

Obviously, $v \in V^{(B)}$ or $v \in V^{(\tilde{B})}$ (use Theorem 23.7) according as $u \in V^{(B)}$ or $u \in V^{(\tilde{B})}$. Since $\llbracket (\forall x \in v) (\exists y \in u) [x \in y] \rrbracket = 1$ by Theorem 23.7, it remains to show that

$$\llbracket (\forall y \in u) (\forall x \in y) [x \in v] \rrbracket = 1,$$

which follows from the definition of $v$.
