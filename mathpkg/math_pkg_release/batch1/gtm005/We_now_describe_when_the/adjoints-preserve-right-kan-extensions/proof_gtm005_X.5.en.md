---
role: proof
locale: en
of_concept: adjoints-preserve-right-kan-extensions
source_book: gtm005
source_chapter: "X"
source_section: "5. Kan Extensions as Coends"
---

Assume the adjunction $F \dashv G$ and the right Kan extension $\langle R, \varepsilon: RK \to T \rangle$. For any functor $H: C \to X$, we have the following chain of natural bijections:

$$\mathrm{Nat}(H, G \circ R) \cong \mathrm{Nat}(FH, R) \cong \mathrm{Nat}(FHK, T) \cong \mathrm{Nat}(HK, GT).$$

The first and third bijections are instances of the adjunction applied pointwise: $\mathrm{Nat}(FH, L) \cong \mathrm{Nat}(H, GL)$ for any $L: C \to A$. The second is the definition of the right Kan extension. The composite natural bijection shows that $G \circ R$ satisfies the universal property of $\mathrm{Ran}_K(GT)$. The counit is obtained by setting $H = G \circ R$ and taking the image of the identity: this yields $G\varepsilon$, where $\varepsilon: RK \to T$ is the counit of the original Kan extension.
