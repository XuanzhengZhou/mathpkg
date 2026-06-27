---
role: proof
locale: en
of_concept: adjunction-characterizations
source_book: gtm005
source_chapter: "IV"
source_section: "1"
---

Theorem: For functors $F: D \to C$, $G: C \to D$, the following are equivalent:

(1) **Hom-set adjunction**: $\varphi_{d,c}: C(F(d), c) \cong D(d, G(c))$, natural in $d$ and $c$.

(2) **Unit-counit adjunction**: Natural transformations $\eta: 1_D \Rightarrow G \circ F$ and $\varepsilon: F \circ G \Rightarrow 1_C$ satisfying triangle identities $(\varepsilon F) \circ (F \eta) = 1_F$ and $(G \varepsilon) \circ (\eta G) = 1_G$.

Proof (1) $\Rightarrow$ (2): Define $\eta_d = \varphi_{d, F(d)}(1_{F(d)})$ and $\varepsilon_c = \varphi_{G(c), c}^{-1}(1_{G(c)})$. Naturality of $\varphi$ implies naturality of $\eta$ and $\varepsilon$. For the first triangle identity, apply $\varphi$ to $1_{F(d)}$ and use naturality.

(2) $\Rightarrow$ (1): Define $\varphi_{d,c}(f) = G(f) \circ \eta_d$ and $\psi_{d,c}(g) = \varepsilon_c \circ F(g)$. The triangle identities show these are inverses. Naturality follows from naturality of $\eta$ and $\varepsilon$.
