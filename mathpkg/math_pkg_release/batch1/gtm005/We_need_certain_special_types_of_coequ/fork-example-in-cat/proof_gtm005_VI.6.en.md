---
role: proof
locale: en
of_concept: fork-example-in-cat
source_book: gtm005
source_chapter: "VI"
source_section: "6"
---

In $\mathbf{Cat}$, a split coequalizer (split fork) for parallel functors $F, G: A \rightrightarrows B$ is a functor $H: B \to C$ with $H \circ F = H \circ G$, equipped with:

1. A functor $S: C \to B$ (section) with $H \circ S = 1_C$.
2. A natural transformation $t: 1_B \Rightarrow S \circ H$ with $H t = 1_H$ (i.e., $H(t_b) = 1_{H(b)}$).
3. A functor $T: B \to A$ and a natural transformation $s: 1_B \Rightarrow G \circ T$ with $F \circ T = 1_B$.

These data make the fork an absolute coequalizer (preserved by all functors). Example: For a monad $(T, \eta, \mu)$ on $C$, the diagram
$$T^2 \xrightarrow{\mu T}{T \mu} T \xrightarrow{\mu} T$$
is a split fork (in $C$, not $\mathbf{Cat}$ unless $C$ is a 2-category). The section is $\eta_T: T \Rightarrow T^2$, and the natural transformations encode the monad laws.
