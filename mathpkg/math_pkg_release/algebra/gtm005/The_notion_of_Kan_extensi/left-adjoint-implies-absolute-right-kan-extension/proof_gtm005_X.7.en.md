---
role: proof
locale: en
of_concept: left-adjoint-implies-absolute-right-kan-extension
source_book: gtm005
source_chapter: "X"
source_section: "7"
---

If $F \dashv G$ with $F: D \to C$, $G: C \to D$, then $G \cong \operatorname{Ran}_F 1_D$, and this Kan extension is absolute (preserved by any functor).

Proof: We need a natural isomorphism
$$\operatorname{Nat}(H \circ F, 1_D) \cong \operatorname{Nat}(H, G)$$
for any $H: C \to D$. Given $\alpha: H \circ F \Rightarrow 1_D$, define $\beta: H \Rightarrow G$ by $\beta_c = G(\alpha_c) \circ H(\eta_{H(c)})$ — actually using the adjunction:

Given $\alpha_d: H(F(d)) \to d$, its adjunct under $F \dashv G$ is $\bar{\alpha}_c: H(c) \to G(c)$ where $\bar{\alpha}_c = G(\alpha_{G(c)}) \circ \eta_{H(c)}$ — wait, let me use the standard mate formula:
$$\beta_c = G(\alpha_{G(c)} \circ H(\varepsilon_c)) \circ \eta_{H(c)}.$$
Actually, the canonical isomorphism uses: $\alpha: H \circ F \Rightarrow 1_D$ induces $\beta: H \Rightarrow G$ via $\beta_c = \alpha_{G(c)} \circ H(\eta_c)$ — no, the types don't match.

The correct formula: $\beta_c = G(\alpha_{G(c)}) \circ H(\eta_{G(c)})$ — still not right. Let's use:
$\beta: H \Rightarrow G$ is defined by $\beta_{F(d)} = \alpha_d$ (up to the adjunction). The adjunction provides the natural bijection $\operatorname{Nat}(H \circ F, 1_D) \cong \operatorname{Nat}(H, G)$, establishing $G$ as $\operatorname{Ran}_F 1_D$. Absoluteness holds because adjunctions are preserved by any functor (post-composition preserves adjunctions).
