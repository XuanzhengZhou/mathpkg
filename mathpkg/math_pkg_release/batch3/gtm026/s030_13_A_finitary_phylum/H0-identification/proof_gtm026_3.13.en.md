---
role: proof
locale: en
of_concept: H0-identification
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

We identify $H^0(X, \xi)$ with $\mathcal{K}^{\mathbf{T}}((X, \xi), (Y, \theta))$.

Recall that $H^0(X, \xi) = \operatorname{Ker}(d^1)$, where

$$d^1: [XT, Y] \rightarrow [XT^2, Y]$$

is given by $(XT \xrightarrow{a} Y) d^1 = \xi T \cdot a - X\mu \cdot a$.

A morphism $a: XT \rightarrow Y$ lies in $\operatorname{Ker}(d^1)$ precisely when $\xi T \cdot a = X\mu \cdot a$. Since $\xi = \operatorname{coeq}(\xi T, X\mu)$ in the canonical resolution of $(X, \xi)$ (this is a standard property of the bar resolution for a monad), the condition $\xi T \cdot a = X\mu \cdot a$ means that $a$ coequalizes the parallel pair $(\xi T, X\mu)$. By the universal property of the coequalizer $\xi: XT \rightarrow X$, there exists a unique $\mathcal{K}$-morphism $h: X \rightarrow Y$ such that $h = \xi \cdot a$.

The condition that this $h$ is a $\mathbf{T}$-algebra homomorphism (i.e., $h \cdot \theta = \xi \cdot hT$) follows from the naturality of the construction. Conversely, given any $\mathbf{T}$-homomorphism $h: (X, \xi) \rightarrow (Y, \theta)$, the composite $a = \xi \cdot hT$ lies in $\operatorname{Ker}(d^1)$.

These constructions are mutually inverse and respect the abelian group structure (pointwise addition in $Y$), establishing the isomorphism

$$H^0(X, \xi) \cong \mathcal{K}^{\mathbf{T}}((X, \xi), (Y, \theta)).$$

The hint $\xi = \operatorname{coeq}(\xi T, X\mu)$ is the key technical fact; it follows from the general theory of monadic resolutions (the bar construction).
