---
role: proof
locale: en
of_concept: interchange-law-natural-transformations
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

For functors $F, G, H: A \to B$ with $\sigma: F \Rightarrow G$, $\tau: G \Rightarrow H$, and $F', G', H': B \to C$ with $\sigma': F' \Rightarrow G'$, $\tau': G' \Rightarrow H'$:
$$(\tau' \circ \tau) \cdot (\sigma' \circ \sigma) = (\tau' \cdot \sigma') \circ (\tau \cdot \sigma).$$

The left side has components $a \mapsto (\tau' \circ \tau)_a \circ (\sigma' \circ \sigma)_a$, where horizontal composition gives $(\sigma' \circ \sigma)_a = \sigma'_{G(a)} \circ F'(\sigma_a)$ and $(\tau' \circ \tau)_a = \tau'_{H(a)} \circ F'(\tau_a)$.

The right side is the horizontal composite of $(\tau' \cdot \sigma'): F' \Rightarrow H'$ and $(\tau \cdot \sigma): F \Rightarrow H$, whose component at $a$ expands using the horizontal composition formula, yielding the same morphism by naturality of $\tau'$ applied to $\sigma_a$ and $\tau_a$.
