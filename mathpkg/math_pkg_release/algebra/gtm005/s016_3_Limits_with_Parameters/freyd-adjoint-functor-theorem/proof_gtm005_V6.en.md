---
role: proof
locale: en
of_concept: freyd-adjoint-functor-theorem
source_book: gtm005
source_chapter: "V"
source_section: "6. Freyd's Adjoint Functor Theorem"
---

If $G$ has a left adjoint $F$, then $G$ must preserve all limits which exist in its domain $A$ by the theorem on right adjoints preserving limits (V.5). Moreover, the universal arrow $\eta_x : x \rightarrow G F x$ which is the unit of the adjunction satisfies the solution set condition for $x$ with $I$ the one-point set: every arrow $h : x \rightarrow G a$ factors as $h = G(\widehat{h}) \circ \eta_x$, where $\widehat{h} : F x \rightarrow a$ is the transpose of $h$ under the adjunction.

Conversely, assume $G$ preserves all small limits and the solution set condition holds. To construct a left adjoint for $G$, it suffices to construct for each $x \in X$ an initial object in the comma category $(x \downarrow G)$. This comma category has small hom-sets (since $A$ does). We show it is small-complete by proving that the forgetful functor $Q : (x \downarrow G) \rightarrow A$ creates all small limits. Indeed, $Q$ creates products: given a $J$-indexed family of objects $f_j : x \rightarrow G a_j$, take the product $\prod a_j$ in $A$; since $G$ preserves products, $G\prod a_j$ is a product in $X$, yielding a unique $f : x \rightarrow G\prod a_j$ with $G p_j \circ f = f_j$, which is the product in $(x \downarrow G)$. Similarly, $Q$ creates equalizers using preservation of equalizers by $G$.

Thus $(x \downarrow G)$ is small-complete with small hom-sets. The solution set condition for $G$ at $x$ is precisely the solution set condition for an initial object in $(x \downarrow G)$. By Theorem 1 (existence of initial objects), $(x \downarrow G)$ has an initial object $\eta_x : x \rightarrow G F x$. This gives an object function $F : X \rightarrow A$. For each arrow $h : x \rightarrow x'$ in $X$, define $F h$ via the universal property of $\eta_x$ applied to $\eta_{x'} \circ h : x \rightarrow G F x'$. This makes $F$ a functor left adjoint to $G$ with unit $\eta$.
