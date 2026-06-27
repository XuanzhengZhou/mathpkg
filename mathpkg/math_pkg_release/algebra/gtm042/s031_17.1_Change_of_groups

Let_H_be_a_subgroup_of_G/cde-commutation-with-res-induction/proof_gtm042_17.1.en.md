---
role: proof
locale: en
of_concept: cde-commutation-with-res-induction
source_book: gtm042
source_chapter: "17"
source_section: "17.1"
---

The homomorphisms $c: R_K(G) \to R_k(G)$, $d: R_K(G) \to R_k(G)$, and $e: P_k(G) \to R_k(G)$ are defined by $c(E) = \widehat{E} \otimes_k k$, $d(E) = \widehat{E} \otimes_A k$, and $e(P) = P$ (viewing a projective $k[G]$-module as an element of $R_k(G)$), where $A$ is a complete discrete valuation ring with residue field $k$ and fraction field $K$ of characteristic zero.

For restriction: $\text{Res}_H^G$ simply views a $k[G]$-module as a $k[H]$-module (or a $K[G]$-module as a $K[H]$-module). Since the constructions $c, d, e$ are defined purely in terms of the underlying module structure (reduction modulo the maximal ideal, or viewing a projective module as an element of the Grothendieck group), they are unaffected by whether we view the module over $G$ or over $H$. Thus $c \circ \text{Res}_H^G = \text{Res}_H^G \circ c$, and similarly for $d$ and $e$.

For induction: $\text{Ind}_H^G E = k[G] \otimes_{k[H]} E$. Since $c, d, e$ are additive functors (or the identity on underlying modules in the case of $e$), and tensor product commutes with reduction modulo the maximal ideal (for $c$ and $d$), we have $\text{Ind}_H^G(c(E)) = c(\text{Ind}_H^G(E))$, and similarly for $d$ and $e$. The essential point is that the operations defining $c, d, e$ commute with the tensor product $k[G] \otimes_{k[H]} -$ used to define induction.
