---
role: proof
locale: en
of_concept: ehrenfeucht-fraisse-criterion
source_book: gtm053
source_chapter: "3"
source_section: "3.15"
---

The proof is an adjustment of the back-and-forth construction used in the proof of the uniqueness of saturated models (Theorem 3.12(ii)).

If there exists a back-and-forth system $I$ between $\mathbf{A}$ and $\mathbf{B}$, then one can show by induction on formula complexity that $\mathbf{A}$ and $\mathbf{B}$ satisfy the same sentences, using the back-and-forth properties to extend any winning strategy in the Ehrenfeucht–Fraïssé game. Conversely, if $\mathbf{A} \equiv \mathbf{B}$ and both are $\aleph_0$-saturated, the set of all finite partial elementary maps between $\mathbf{A}$ and $\mathbf{B}$ forms a back-and-forth system. More precisely, define $I$ to be the set of all finite partial maps $f : \bar{a} \mapsto \bar{b}$ such that $\text{tp}(\bar{a}) = \text{tp}(\bar{b})$. Then $I$ is nonempty (it contains the empty map), and the saturation condition guarantees both the forth and back properties: given $f \in I$ mapping $\bar{a}$ to $\bar{b}$ and any $a \in A$, the type $\text{tp}(\bar{a}, a)$ is realized in $\mathbf{B}$ by $\aleph_0$-saturation, yielding an extension $g \supseteq f$ with $a \in \text{Dom}(g)$. The back property is symmetric.
