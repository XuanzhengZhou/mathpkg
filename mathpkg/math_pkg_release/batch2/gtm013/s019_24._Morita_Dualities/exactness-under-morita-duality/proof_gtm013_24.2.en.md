---
role: proof
locale: en
of_concept: exactness-under-morita-duality
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---

Since ${}_R U_S$ defines a Morita duality, ${}_R U$ is an injective cogenerator by Theorem 24.1. Hence the functor $(\cdot)^* = \operatorname{Hom}_R(-, U)$ is exact. Applying $(\cdot)^*$ to the sequence $M_1 \xrightarrow{f} M_2 \xrightarrow{g} M_3$ yields the dual sequence $M_3^* \xrightarrow{g^*} M_2^* \xrightarrow{f^*} M_1^*$, and exactness is preserved by the exactness of the functor.

Conversely, if $M_3^* \xrightarrow{g^*} M_2^* \xrightarrow{f^*} M_1^*$ is exact, then applying $(\cdot)^*$ again and using that $\sigma$ is a natural isomorphism (since every module is $U$-reflexive under a Morita duality) gives back the original sequence $M_1 \to M_2 \to M_3$ as exact. The reflection of exactness follows from the fact that $U$ cogenerates, so $\sigma$ is monic; since $(\cdot)^*$ is exact, the double dual sequence is exact, and the naturality of $\sigma$ forces the original sequence to be exact.

For the particular case: $f$ is epic means $M_2 \xrightarrow{f} M_3 \to 0$ is exact, which dualizes to $0 \to M_3^* \xrightarrow{f^*} M_2^*$ exact, i.e., $f^*$ is monic. Similarly, $f$ is monic if and only if $f^*$ is epic.

The symmetric statement for $S$-homomorphisms also holds.
