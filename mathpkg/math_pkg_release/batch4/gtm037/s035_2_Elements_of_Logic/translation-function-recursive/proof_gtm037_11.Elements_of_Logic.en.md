---
role: proof
locale: en
of_concept: translation-function-recursive
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

The proof follows by weak Church's thesis. The translation $\varphi \mapsto \varphi'$ is defined by recursion on the structure of $\varphi$, as given in Definition 11.26. At each step, the translation depends only on the outermost syntactic constructor and the translations of immediate subformulas.

Since the language $\mathcal{L}$ is effectivized, the Gödel numbering functions $g^+$ and $g'^+$ are recursive, and the arity functions and symbol sets are recursive. The translation is a primitive recursive definition over the formula tree:

- For atomic formulas of the form $\sigma = v_i$, the computation reduces to translating the term $\sigma$ and constructing the appropriate existential prefix.
- For Boolean connectives, the translation commutes: $(\neg\varphi)' = \neg\varphi'$, $(\varphi \lor \psi)' = \varphi' \lor \psi'$, etc.
- For quantifiers, $(\forall v_i\varphi)' = \forall v_i\varphi'$.

The term translation, in turn, is defined by recursion on term structure. By the standard closure properties of recursive (indeed primitive recursive) functions under definition by cases and course-of-values recursion, the mapping $m \mapsto f(m)$ defined as $g'^+\varphi'$ when $m = g^+\varphi$, and $0$ otherwise, is recursive.
