---
role: proof
locale: en
of_concept: interchange-law-for-natural-transformations
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

For $\sigma: F \Rightarrow G$, $\tau: G \Rightarrow H$ (vertically composable) and $\sigma': F' \Rightarrow G'$, $\tau': G' \Rightarrow H'$:
$$(\tau' \cdot \sigma') \circ (\tau \cdot \sigma) = (\tau' \circ \tau) \cdot (\sigma' \circ \sigma).$$

Proof: For any object $a$, compute both sides at $a$. Left side (vertical composite, then horizontal):
$$((\tau' \cdot \sigma') \circ (\tau \cdot \sigma))_a = H'((\tau \cdot \sigma)_a) \circ (\tau' \cdot \sigma')_{F(a)}.$$
Right side (horizontal composites, then vertical):
$$((\tau' \circ \tau) \cdot (\sigma' \circ \sigma))_a = (\tau' \circ \tau)_a \circ (\sigma' \circ \sigma)_a.$$
Expanding definitions using horizontal composition formula $(\alpha \circ \beta)_a = \alpha_{G(a)} \circ F(\beta_a)$, both sides evaluate to the same morphism by naturality of $\tau'$ and associativity of composition.
