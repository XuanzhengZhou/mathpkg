---
role: proof
source_book: gtm-0073
chapter: X
section: "X.3"
proof_technique: universal-property
locale: en
content_hash: ""
written_against: ""
---
(Uniqueness) If $\{0'_{C,D}\}$ and $\{0_{C,D}\}$ are two families of morphisms with the stated properties, then for each pair $C, D$,
\[
0_{C,D} = 0'_{D,D} \circ 0_{C,D} = 0'_{C,D}.
\]

(Existence) For each object $A$ of $\mathcal{C}$, let $\iota_A : 0 \to A$ and $\pi_A : A \to 0$ be the unique morphisms guaranteed by the initial and terminal properties of $0$. For any $f \in \hom(D, E)$, $f \iota_D = \iota_E : 0 \to E$ by the universality of the initial morphism. For any $g \in \hom(B, C)$, $\pi_C g = \pi_B : B \to 0$ by the couniversality of the terminal morphism. Define $0_{C,D}$ to be the composition $C \xrightarrow{\pi_C} 0 \xrightarrow{\iota_D} D$. Then for $f \in \hom(D, E)$,
\[
f \circ 0_{C,D} = f \iota_D \pi_C = \iota_E \pi_C = 0_{C,E},
\]
and similarly for $g \in \hom(B, C)$,
\[
0_{C,D} \circ g = \iota_D \pi_C g = \iota_D \pi_B = 0_{B,D}.
\]
