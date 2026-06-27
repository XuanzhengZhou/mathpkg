---
role: proof
locale: en
of_concept: properties-of-semi-reflexive-spaces
source_book: gtm036
source_chapter: "20"
source_section: "20.2"
---

\textbf{(ii)} Let $F$ be a closed subspace of a semi-reflexive space $E$, let $B$ be the polar of a bounded subset of $F$, let $B^0$ be the polar of $B$ in $F^*$, and let $f \in E^*$. Then the restriction of $f$ to $F$ belongs to $B^0$ if and only if $f$ belongs to the polar $C$ of $B$ in $E$. That is, the inverse of $B^0$ under the canonical map $T$ of $E^*$ onto $F^*$ is the polar of $B$ in $E^*$, and $T$ is therefore continuous relative to the strong topologies. The proof of (ii) now reduces to showing that $T$ is open, for continuity and openness of $T$ implies that the induced map of $E^* / F^0$ onto $F^*$ is topological.

Let $B$ be a bounded closed convex circled subset of $E$; then the polar $C$ of $B \cap F$ in $F^*$ is equal to $T[(B \cap F)^0]$, since any continuous functional on $F$ can be extended to $E$ (14.1). By the computation rule 16.3,
\[
(B \cap F)^0 = (B^0 \cup F^0)^0_0 \subset (B^0 + F^0)^0_0.
\]
The set $(B^0 + F^0)^0_0$ is the $m(E^*, E)$-closure of $B^0 + F^0$, which is also the strong closure because of the semi-reflexivity of $E$ (20.1). Hence
\[
(B^0 + F^0)^0_0 \subset B^0 + F^0 + B^0 \subset F^0 + 2B^0,
\]
and it follows that $C \subset T[F^0 + 2B^0] = 2T[B^0]$, which implies that $T$ is open.

\textbf{(iii)} Part (iii) is a direct consequence of the criterion 20.1 for semi-reflexivity, the description 14.8 of bounded subsets of a direct sum and product, the identification 17.13 of the weak topology of a product, and the Tychonoff theorem 4.1.
