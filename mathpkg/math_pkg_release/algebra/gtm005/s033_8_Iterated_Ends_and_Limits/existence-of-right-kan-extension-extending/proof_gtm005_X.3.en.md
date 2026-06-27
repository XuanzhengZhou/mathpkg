---
role: proof
locale: en
of_concept: existence-of-right-kan-extension-extending
source_book: gtm005
source_chapter: "X"
source_section: "3"
---

Given $K: M \to C$ and $T: M \to A$, if $A$ has all limits of the relevant shape, then $\operatorname{Ran}_K T$ exists and is given pointwise by
$$(\operatorname{Ran}_K T)(c) = \varprojlim_{(c \downarrow K)} T \circ \Pi,$$
where $(c \downarrow K)$ is the comma category of arrows $c \to K(m)$, and $\Pi: (c \downarrow K) \to M$ is the projection $(c \to K(m)) \mapsto m$.

Proof: For each $c$, the limit formula defines an object. For $f: c \to c'$, a morphism between the limits is induced by the functor $(c' \downarrow K) \to (c \downarrow K)$ sending $(c' \to K(m))$ to $(c \to c' \to K(m))$. The universal property follows because a natural transformation $H \circ K \Rightarrow T$ gives, for each $c$, a cone from $H(c)$ over the diagram $(c \downarrow K) \to M \xrightarrow{T} A$, hence a unique map $H(c) \to (\operatorname{Ran}_K T)(c)$.
