---
role: proof
locale: en
of_concept: strong-monoidal-functor-endofunctor-category
source_book: gtm005
source_chapter: "XI"
source_section: "1"
---

$\operatorname{End}(C) = C^C$ is a strict monoidal category under composition ($F \otimes G = F \circ G$, unit $1_C$). A strong monoidal functor $\Phi: M \to \operatorname{End}(C)$ consists of a functor with coherent natural isomorphisms $\phi_{m,n}: \Phi(m \otimes n) \cong \Phi(m) \circ \Phi(n)$ and $\phi_0: \Phi(I) \cong 1_C$.

Coherence axioms (associativity and unit): The diagrams
$$\begin{CD} \Phi((m \otimes n) \otimes p) @>>> \Phi(m \otimes n) \circ \Phi(p) @>>> (\Phi(m) \circ \Phi(n)) \circ \Phi(p) \\ @VVV @. @VV{=}V \\ \Phi(m \otimes (n \otimes p)) @>>> \Phi(m) \circ \Phi(n \otimes p) @>>> \Phi(m) \circ (\Phi(n) \circ \Phi(p)) \end{CD}$$
and similar for unit commute. This is precisely the definition of an action (actegory) of the monoidal category $M$ on $C$.
