---
role: proof
locale: en
of_concept: braid-group-action-on-tensor-products
source_book: gtm005
source_chapter: "XI"
source_section: "6"
---

In a braided monoidal category $(C, \otimes, I, \gamma)$, the braid group $B_n$ acts on $A^{\otimes n}$ for any object $A$. The generator $\sigma_i$ acts as
$$1_{A^{\otimes (i-1)}} \otimes \gamma_{A, A} \otimes 1_{A^{\otimes (n-i-1)}}: A^{\otimes n} \to A^{\otimes n},$$
braiding the $i$-th and $(i+1)$-st tensor factors.

The relations hold because:
- Far commutativity: when $|i-j| > 1$, the braidings act on disjoint pairs of tensor factors, and $\gamma$ is natural, so the compositions commute.
- Braid relation: applying $\sigma_i$, $\sigma_{i+1}$, $\sigma_i$ to the $(i, i+1, i+2)$ factors corresponds to the Yang-Baxter hexagon for $\gamma$, which holds identically:
$$(1 \otimes \gamma) \circ (\gamma \otimes 1) \circ (1 \otimes \gamma) = (\gamma \otimes 1) \circ (1 \otimes \gamma) \circ (\gamma \otimes 1),$$
acting on $A \otimes A \otimes A$. This gives a group homomorphism $B_n \to \operatorname{Aut}_C(A^{\otimes n})$.
