---
role: proof
locale: en
of_concept: hilbert-right-invertible
source_book: gtm015
source_chapter: "57"
source_section: "57.20"
---

# Proof of Right invertibility in Hilbert space

(57.20) Corollary. If $H$ is a Hilbert space and $T \in \mathcal{L}(H)$, the following conditions on $T$ are equivalent:

(a) $T$ is right-invertible in $\mathcal{L}(H)$;
(b) $T$ is surjective;
(c) $T$ is not a right TDZ in $\mathcal{L}(H)$.

Proof. It is obvious from the properties of adjunction that $T$ is a left [right] divisor of zero iff $T^*$ is a right [left] divisor of zero, and similarly for TDZ's. Thus (a) and (c) are equivalent by the parallel assertion of (57.19).

The equivalence of (b) and (c) requires only that $H$ be a Banach space (57.17); but the following argument that (a) and (b) are equivalent in the Hilbert space setting is simpler.

(a) implies (b): Obvious.

(b) implies (a): Let $N$ be the null space of $T$, and let $T_0$ be the restriction of $T$ to $N^\perp$. Since $H = N \oplus N^\perp$, it is clear that $T_0: N^\perp \rightarrow H$ is a continuous vector space isomorphism; by the open mapping theorem, it is bicontinuous (48.1). The formula $Sx = T_0^{-1}x$ ($x \in H$) defines an element of $\mathcal{L}(H)$ such that $TS = I$.

The following result is a useful characterization of invertibility in the Hilbert space setting; it is a special case of a number of the earlier results in the section (cf. 43.8), but the elementary indigenous proof is clearer:
