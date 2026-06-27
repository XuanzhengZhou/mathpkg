---
role: proof
locale: en
of_concept: functor-restriction-to-bimodule-categories
source_book: gtm013
source_chapter: "20"
source_section: "20.4"
---

The proof follows from Lemma 20.3 and the properties of the canonical bimodule structure. Recall that for an additive covariant functor $F: {}_R\mathcal{C} \to {}_S\mathcal{D}$ and a bimodule ${}_R U_T$, the canonical right $T$-module structure on $F(U)$ is given by $xt = F(\rho(t))(x)$ where $\rho(t): U \to U$ is right multiplication by $t \in T$. Similarly for contravariant $H$, the left $T$-module structure on $H(U)$ is given by $ty = H(\rho(t))(y)$.

(1) Since $f: {}_R U_T \to {}_R V_T$ is a bimodule homomorphism, it is an $R$-homomorphism and $f(ut) = f(u)t$ for all $u \in U$, $t \in T$. The $R$-linearity gives $F(f) \in \operatorname{Hom}_S(F(U), F(V))$. For the $T$-linearity: for $x \in F(U)$ and $t \in T$,

$$F(f)(xt) = F(f)(F(\rho_U(t))(x)) = F(f \circ \rho_U(t))(x) = F(\rho_V(t) \circ f)(x) = F(\rho_V(t))(F(f)(x)) = F(f)(x)t.$$

Thus $F(f)$ is an $(S,T)$-bimodule homomorphism.

(2) For $\eta_U: F(U) \to F'(U)$, naturality gives $\eta_U \circ F(\rho_U(t)) = F'(\rho_U(t)) \circ \eta_U$, which means $\eta_U(xt) = \eta_U(x)t$, so $\eta_U$ is $T$-linear, hence an $(S,T)$-bimodule homomorphism.

Parts (3) and (4) for contravariant functors follow by analogous arguments, reversing the appropriate arrows.
