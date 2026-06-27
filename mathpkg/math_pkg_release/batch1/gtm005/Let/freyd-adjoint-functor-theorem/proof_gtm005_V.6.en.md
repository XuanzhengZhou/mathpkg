---
role: proof
locale: en
of_concept: freyd-adjoint-functor-theorem
source_book: gtm005
source_chapter: "V"
source_section: "6. Freyd's Adjoint Functor Theorem"
---

**Proof.** If $G$ has a left adjoint $F$, then by Theorem V.5, $G$ (as a right adjoint) preserves all limits; in particular, all small limits. Moreover, the universal arrow $\eta_x : x \rightarrow GFx$ (the unit of the adjunction) satisfies the solution set condition for $x$ with $I$ the one-point set: every arrow $h : x \rightarrow Ga$ factors as $h = Gt \circ \eta_x$ where $t : Fx \rightarrow a$ is the adjunct of $h$.

Conversely, assume $G$ preserves all small limits and the solution set condition holds. For each $x \in X$, consider the comma category $(x \downarrow G)$, whose objects are arrows $f : x \rightarrow Ga$ and whose morphisms $t : f \rightarrow f'$ are arrows $t : a \rightarrow a'$ in $A$ with $Gt \circ f = f'$. We show $(x \downarrow G)$ satisfies the hypotheses of the Initial Object Existence Theorem.

The forgetful functor $Q : (x \downarrow G) \rightarrow A$ (sending $f : x \rightarrow Ga$ to $a$) creates all small limits, because $G$ preserves them. Explicitly:
- For products: given a $J$-indexed family $f_j : x \rightarrow Ga_j$, let $p_j : \prod a_j \rightarrow a_j$ be the product in $A$. Since $G$ preserves products, $Gp_j : G\prod a_j \rightarrow Ga_j$ is a product diagram. The universal property yields a unique $f : x \rightarrow G\prod a_j$ with $Gp_j \circ f = f_j$, giving the product in $(x \downarrow G)$.
- For equalizers: given $s, t : f \rightarrow g$ in $(x \downarrow G)$, let $e : a \rightarrow b$ be the equalizer of $s, t$ in $A$. Since $G$ preserves equalizers, $Ge$ equalizes $Gs, Gt$. From $Gs \circ f = g = Gt \circ f$, there is a unique $h : x \rightarrow Ga$ with $Ge \circ h = f$, giving the equalizer.

Thus $(x \downarrow G)$ is small-complete with small hom-sets. The solution set condition for $G$ translates directly to the solution set condition for $(x \downarrow G)$. Therefore, by the Initial Object Existence Theorem (Theorem V.6.1), $(x \downarrow G)$ has an initial object $\eta_x : x \rightarrow GFx$. This initial object is precisely a universal arrow from $x$ to $G$, which by Proposition III.2.2 defines a left adjoint $F$ to $G$. $\square$
