---
role: proof
locale: en
of_concept: absolute-right-kan-extension-from-adjoint
source_book: gtm005
source_chapter: "X"
source_section: "7"
---

Let $G: A \to X$ have a left adjoint $F$ with unit $\eta: 1_X \to GF$ and counit $\varepsilon: FG \to 1_A$. For any functor $H: A \to C$, the adjunction provides a natural bijection
$$\operatorname{Nat}(S, HF) \cong \operatorname{Nat}(SG, H)$$
for all $S: X \to C$, natural in $S$. This bijection is given by precomposition with $G$ and postcomposition with $H\varepsilon$. Specifically, a natural transformation $\sigma: SG \to H$ corresponds to $H\varepsilon \cdot \sigma F: S = S1_X \xrightarrow{S\eta} SGF \xrightarrow{\sigma F} HF$.

The naturality of this bijection in $S$ is precisely the universal property defining $\operatorname{Ran}_G H$, with counit $H\varepsilon: HFG \to H$. Thus $HF = \operatorname{Ran}_G H$ with unit $H\varepsilon$.

Since a right Kan extension is preserved by a functor $K$ precisely when $K \circ \operatorname{Ran}_G H \cong \operatorname{Ran}_G (K \circ H)$ via the canonical map, and the above identification holds for any $H$, composing both sides with any functor $K: C \to D$ gives $KHF = \operatorname{Ran}_G (KH)$. Hence the Kan extension is absolute -- preserved by any functor.

Taking $H = 1_A$ yields the special case: $F = \operatorname{Ran}_G 1_A$ with counit $\varepsilon$, and this Kan extension is absolute.
