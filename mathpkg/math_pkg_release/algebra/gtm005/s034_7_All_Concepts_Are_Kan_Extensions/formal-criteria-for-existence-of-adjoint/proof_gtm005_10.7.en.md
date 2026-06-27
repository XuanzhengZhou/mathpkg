---
role: proof
locale: en
of_concept: formal-criteria-for-existence-of-adjoint
source_book: gtm005
source_chapter: "X"
source_section: "7"
---

**Forward direction.** If $G$ has a left adjoint $F$, with unit $\eta: 1_X \to GF$ and counit $\varepsilon: FG \to 1_A$, then for all functors $H: A \to C$ (in particular, for the identity functor $1_A$) there is a bijection
$$\operatorname{Nat}(S, HF) \cong \operatorname{Nat}(SG, H),$$
natural in $S: X \to C$. This bijection shows that $HF = \operatorname{Ran}_G H$, with unit $H\varepsilon$. In particular, taking $H = 1_A$ gives $F = \operatorname{Ran}_G 1_A$ with counit $\varepsilon$. Taking $H = G$ shows $GF = \operatorname{Ran}_G G$, with unit $G\varepsilon$. Hence $G$ preserves the right Kan extension $\operatorname{Ran}_G 1_A$.

**Reverse direction.** Suppose $1_A$ has a right Kan extension $R$ along $G$, preserved by $G$. We have bijections
$$\varphi = \varphi_S: \operatorname{Nat}(S, R) \cong \operatorname{Nat}(SG, 1_A), \quad \varphi(S \xrightarrow{\varrho} R) = \varepsilon \cdot \varrho G,$$
$$\psi = \psi_H: \operatorname{Nat}(H, GR) \cong \operatorname{Nat}(HG, G), \quad \psi(H \xrightarrow{\sigma} GR) = G\varepsilon \cdot \sigma G,$$
natural in $S: X \to A$ and $H: X \to X$, with counit $\varepsilon = \varphi_R(1_R): RG \to 1_A$ and $G\varepsilon = \psi_{GR}(1_{GR}): GRG \to G$.

Define $\eta: 1_X \to GR$ by $\eta = \psi_{\mathrm{id}}^{-1}(1_G: G \to G)$. Then $\psi(\eta) = 1_G$, which means $G\varepsilon \cdot \eta G = 1_G$. This is one triangular identity. The other triangular identity $\varepsilon R \cdot R\eta = 1_R$ follows from the universal property of the right Kan extension. Thus $(R, \eta, \varepsilon)$ is an adjunction $R \dashv G$.
