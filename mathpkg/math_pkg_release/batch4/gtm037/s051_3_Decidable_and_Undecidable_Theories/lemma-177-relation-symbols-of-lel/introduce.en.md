---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Lemma 17.7 is an immediate corollary of Lemma 17.6 that extends the representation result from operation symbols to the relation symbols $R_{\mathbf{O}}$ of $\mathcal{L}_{\text{el}}$. Recall from Definition 17.4 that each operation symbol $\mathbf{O}$ has an associated relation symbol $R_{\mathbf{O}}$ defined by the axiom $R_{\mathbf{O}}(v_0, \ldots, v_{m-1}) \leftrightarrow \mathbf{O}(v_0, \ldots, v_{m-1}) = \Delta 1$. The lemma states that the number-theoretic relation $\#R_{\mathbf{O}}$ (defined as the set of tuples on which $\#\mathbf{O}$ evaluates to $1$) is faithfully represented by the formal relation symbol $R_{\mathbf{O}}$: membership in $\#R_{\mathbf{O}}$ is provable in $\mathcal{P}$ when true, and its negation is provable when false. Together, Lemmas 17.6 and 17.7 ensure that all syntactic operations and predicates used in the formalization of first-order logic are correctly captured within the theory $\mathcal{P}$, a prerequisite for constructing a provability predicate satisfying the Hilbert-Bernays conditions.
