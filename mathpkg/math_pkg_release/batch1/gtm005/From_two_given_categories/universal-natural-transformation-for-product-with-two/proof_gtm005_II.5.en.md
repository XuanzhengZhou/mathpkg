---
role: proof
locale: en
of_concept: universal-natural-transformation-for-product-with-two
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

The pair $(C^{\mathbf{2}}, \varepsilon)$ is universal among categories equipped with a natural transformation between two functors from $C$. Here $\varepsilon: \partial_0 \Rightarrow \partial_1$ where $\partial_j: C^{\mathbf{2}} \to C$ are the domain and codomain functors.

Given natural transformations $\tau: F \Rightarrow G$ with $F, G: D \to C$, there is a unique functor $H: D \to C^{\mathbf{2}}$ with $\partial_0 \circ H = F$, $\partial_1 \circ H = G$, and $\varepsilon H = \tau$.

Define $H(d) = \tau_d: F(d) \to G(d)$ (an object of $C^{\mathbf{2}}$). For $f: d \to d'$, $H(f)$ is the commutative square $(F(f), G(f))$ from $\tau_d$ to $\tau_{d'}$. Naturality of $\tau$ ensures this is a valid morphism in $C^{\mathbf{2}}$.
