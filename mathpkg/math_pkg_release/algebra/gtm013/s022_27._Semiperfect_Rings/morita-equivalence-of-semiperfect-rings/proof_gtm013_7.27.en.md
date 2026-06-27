---
role: proof
locale: en
of_concept: morita-equivalence-of-semiperfect-rings
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

Let $R$ be semiperfect with basic idempotent $e$. By (27.10) and (17.9), $R e$ is a progenerator for ${}_R \mathbf{M}$. Thus by (22.4), $R$ and $e R e \cong \operatorname{End}({}_R R e)$ are Morita equivalent; that is, $R$ and its basic ring are Morita equivalent. From this we deduce that if $R$ and $S$ are semiperfect with isomorphic basic rings, then $R$ and $S$ are equivalent.

Conversely, suppose $R$ and $S$ are equivalent semiperfect rings via an equivalence $F: {}_R \mathbf{M} \rightarrow {}_S \mathbf{M}$. If $e = e_1 + \cdots + e_m$ is a basic idempotent for $R$, then it follows from (27.10) and the results of Section 21 that

$$F(R e) \cong F(R e_1) \oplus \cdots \oplus F(R e_m),$$

where $F(R e_1), \ldots, F(R e_m)$ is an irredundant set of representatives of the indecomposable projective left $S$-modules. Thus by (27.10), if $f$ is a basic idempotent for $S$, then $F(R e) \cong S f$ and we have (see (21.2))

$$e R e \cong \operatorname{End}({}_R R e) \cong \operatorname{End}({}_S F(R e)) \cong f S f.$$

So the basic rings of $R$ and $S$ are isomorphic.
