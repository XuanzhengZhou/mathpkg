---
role: proof
locale: en
of_concept: final-functor-preserves-colimits
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Let $L : J' \to J$ be final and $F : J \to X$ a functor with colimit $\mu : F \Rightarrow \varinjlim F$. The restriction $\mu \circ L : F \circ L \Rightarrow \varinjlim F$ is a cone. Let $\lambda : F \circ L \Rightarrow x$ be any other cone. We need a unique arrow $f : \varinjlim F \to x$ with $f \circ \mu = \lambda$ (after restriction).

Define $\tau_k : F(k) \to x$ for each $k \in J$ as follows. Since $(k \downarrow L)$ is nonempty, choose $j' \in J'$ and $u : k \to L j'$. Set $\tau_k = \lambda_{j'} \circ F(u)$. We must verify this is independent of the choices. If $u' : k \to L j''$ is another choice, finality gives a commutative diagram connecting $u$ and $u'$. The connectedness condition implies $L j'$ and $L j''$ are linked through arrows in the image of $L$, and the cone property of $\lambda$ forces $\lambda_{j'} \circ F(u) = \lambda_{j''} \circ F(u')$.

Thus $\tau : F \Rightarrow x$ is a well-defined cone. By universality of $\mu$, there is a unique $f : \varinjlim F \to x$ with $f \circ \mu = \tau$. In particular, for $j' \in J'$, taking $k = L j'$ and $u = 1_{L j'}$ gives $\tau_{L j'} = \lambda_{j'}$, so $f \circ \mu L = \lambda$. Therefore $\mu L$ is a colimiting cone, and the canonical map $h$ is an isomorphism.
