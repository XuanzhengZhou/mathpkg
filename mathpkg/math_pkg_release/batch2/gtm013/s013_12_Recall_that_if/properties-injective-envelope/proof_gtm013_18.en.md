---
role: proof
locale: en
of_concept: properties-injective-envelope
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

(1) Immediate from the definition: if $M$ is injective, then $1_M: M \to M$ is an injective envelope.

(2) Since $N \trianglelefteq E(N)$, if $M \trianglelefteq N$, then $M \trianglelefteq E(N)$ by transitivity of essential extensions. Since $E(N)$ is injective, the inclusion $M \to E(N)$ is an injective envelope of $M$, so $E(M) \cong E(N)$ (in fact they are equal up to isomorphism over $M$).

(3) Apply (18.11)(b) to the inclusion $f: M \to Q$; the resulting monomorphism $g: E(M) \to Q$ splits by injectivity of $E(M)$, giving $Q = \operatorname{Im} g \oplus E \cong E(M) \oplus E$.

(4) Let $f: \bigoplus_A M_\alpha \to \bigoplus_A E(M_\alpha)$ be the direct sum of the injective envelopes $M_\alpha \to E(M_\alpha)$. Since $f$ is monic (6.25), it suffices to show it is essential. This follows from (6.17.2): the direct sum of essential monomorphisms is essential.
