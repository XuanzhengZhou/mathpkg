---
role: proof
locale: en
of_concept: colimit-iff-left-kan-extension-along-terminal-functor
source_book: gtm005
source_chapter: "X"
source_section: "3"
---

Let $t: J \to \mathbf{1}$ be the unique functor to the terminal category. For $F: J \to C$, a left Kan extension $\operatorname{Lan}_t F: \mathbf{1} \to C$ is precisely the colimit of $F$.

$\mathbf{1}$ has one object $*$, so $\operatorname{Lan}_t F$ is determined by the object $L = \operatorname{Lan}_t F(*) \in C$. The universal natural transformation $\eta: F \Rightarrow \operatorname{Lan}_t F \circ t$ is a cocone $\eta_j: F(j) \to L$. The universal property: for any $G: \mathbf{1} \to C$ (i.e., object $c = G(*)$) and $\alpha: F \Rightarrow G \circ t$ (a cocone with vertex $c$), there is a unique $\beta: \operatorname{Lan}_t F \Rightarrow G$ (morphism $L \to c$) with $\alpha = (\beta t) \circ \eta$. This is exactly the colimit universal property.
