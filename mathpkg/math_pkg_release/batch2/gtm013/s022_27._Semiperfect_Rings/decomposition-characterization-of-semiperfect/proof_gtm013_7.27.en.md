---
role: proof
locale: en
of_concept: decomposition-characterization-of-semiperfect
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

$(a) \Rightarrow (b)$. This follows from (27.11) and Azumaya's Theorem (12.6) since in (27.6.b) each $e_i R e_i \cong \operatorname{End}({}_R R e_i)$ is local.

$(b) \Rightarrow (c)$. Assume (b), and let $P$ be a finitely generated projective $R$-module. Then every direct summand of $P$ is a finite direct sum of indecomposable modules. Thus a decomposition of $P$ that complements maximal direct summands must complement all direct summands (see (12.2)).

$(c) \Rightarrow (d)$. This is clear.

$(d) \Rightarrow (a)$. Assume (d). Then by (12.3) each direct summand of $R^{(2)}$ has a decomposition that complements direct summands. In particular, ${}_R R$ has such a decomposition, say $R = R e_1 \oplus \ldots \oplus R e_n$, where each $e_i$ is primitive and each $\operatorname{End}({}_R R e_i) \cong e_i R e_i$ is local (by (12.6)). Thus $R$ satisfies (27.6.b), so $R$ is semiperfect.
