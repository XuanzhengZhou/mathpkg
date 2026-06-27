---
role: proof
locale: en
of_concept: theorem-9-25
source_book: gtm008
source_chapter: "5"
source_section: "5 For each formula"
---
We take the Axiom of Replacement in the following form:

$$(\exists b)(\forall x \in a)(\exists y \in b)[(\exists y')\varphi(x, y') \rightarrow \varphi(x, y)].$$

We wish to prove

$$(\forall a \in M)[[(\exists b)(\forall x \in a)(\exists y \in b)\varphi'(x, y)] = 1],$$

where we abbreviate $(\exists y')\varphi(x, y') \rightarrow \varphi(x, y)$ by $\varphi'(x, y)$. First we note that

$$(\forall x \in M)[[(\exists y)\varphi'(x, y)] = 1]$$

If $a \in M$ then $(\exists \alpha)[a \in M_{\alpha}]$ and since $\sum_{y \in M} [\varphi'(x, y)] = 1$.

$$(\exists \beta)(\forall x \in M_{\alpha})\left[\sum_{y \in M_{\beta}} [\varphi'(x, y)] = 1\right],$$

by Corollary 9.15. Then, for this $\beta$

$$(\exists b)(\forall y \in M_{\beta})[[y \in b]] = 1],$$

by Theorem 9.23. Hence

$$\sum_{y \in M} [y \in b][\varphi'(x, y)] \geq \sum_{y \in M_{\beta}} [y \in b][\varphi'(x, y)]$$
$$= \sum_{y \in M_{\beta}} [\varphi'(x, y)].$$

Therefore

$$(\forall x \in M_{\alpha})\

Therefore

$$\llbracket x \in a \rrbracket \leq \llbracket (\exists y \in b) \varphi'(x, y) \rrbracket$$

hence

$$\llbracket (\forall x \in a) (\exists y \in b) \varphi'(x, y) \rrbracket = 1.$$

Remark. We have now proved the following.
