---
role: proof
locale: en
of_concept: cohen-structure-theorem
source_book: gtm052
source_chapter: "I"
source_section: "5"
---

See Matsumura [2, Cor. 2, p. 206] or Zariski–Samuel [1, vol. 2, Cor., p. 307].

The proof proceeds by constructing a coefficient field $k \subseteq A$ (a subfield mapping isomorphically onto the residue field $A/\mathfrak{m}$), using the hypothesis that $A$ contains some field. This requires the completeness to lift the residue field via Hensel's lemma in characteristic $0$, or via the existence of $p$-bases in characteristic $p$. Once a coefficient field is obtained, one chooses a regular system of parameters $x_1, \ldots, x_n \in \mathfrak{m}$ (i.e., elements whose images form a $k$-basis of $\mathfrak{m}/\mathfrak{m}^2$). The completeness of $A$ then yields an isomorphism $k[[x_1, \ldots, x_n]] \xrightarrow{\sim} A$ sending each formal power series to its evaluation in $A$.
