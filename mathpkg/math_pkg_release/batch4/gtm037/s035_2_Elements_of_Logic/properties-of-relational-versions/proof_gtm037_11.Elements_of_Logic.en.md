---
role: proof
locale: en
of_concept: properties-of-relational-versions
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

The statement is truncated in the available source text. The proof proceeds as follows:

**(i)** If $\varphi$ contains no operation symbols, then by inspection of the recursive definition of the translation, every clause that modifies a formula involves an operation symbol. In particular, the special clause for $\mathbf{O}\sigma_0\cdots\sigma_{m-1} = v_i$ is never triggered, and all other clauses ($\neg$, $\lor$, $\land$, $\forall$, atomic relations, equality of variables) leave the formula unchanged. Hence $\varphi' = \varphi$ by a straightforward induction on formula structure.

**(ii)** The semantic equivalence is proved by induction on the structure of $\varphi$. For atomic formulas involving operation symbols, one uses the definition of the relational version $\mathfrak{A}'$ of a structure: for each operation symbol $\mathbf{O}$, the relation $T_{\mathbf{O}}^{\mathfrak{A}'}$ is defined as the graph of $\mathbf{O}^{\mathfrak{A}}$, i.e., $(a_0,\ldots,a_{m-1},b) \in T_{\mathbf{O}}^{\mathfrak{A}'}$ iff $\mathbf{O}^{\mathfrak{A}}(a_0,\ldots,a_{m-1}) = b$. Then the existential formula in the translation precisely captures the condition that the term evaluates to the specified value. The induction steps for Boolean connectives and quantifiers are routine.

[Note: The source text for this proof is incomplete in the stitched section.]