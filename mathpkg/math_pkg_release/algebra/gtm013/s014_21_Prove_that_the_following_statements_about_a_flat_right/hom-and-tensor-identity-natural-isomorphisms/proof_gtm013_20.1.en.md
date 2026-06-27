---
role: proof
locale: en
of_concept: hom-and-tensor-identity-natural-isomorphisms
source_book: gtm013
source_chapter: "20"
source_section: "20.1"
---

It is easy to prove the naturality of $\rho$. For (1), the map $\rho_M: M \to \operatorname{Hom}_R(R, M)$ defined by $\rho_M(m)(r) = rm$ is an $R$-homomorphism because $\rho_M(rm)(s) = s(rm) = (sr)m = \rho_M(m)(sr) = [r \cdot \rho_M(m)](s)$. Its inverse is given by evaluation at $1$: $\gamma \mapsto \gamma(1)$, which gives $M \cong \operatorname{Hom}_R(R, M)$ as in (4.5). For naturality, if $f: M \to N$ is an $R$-homomorphism, then for all $m \in M$ and $r \in R$:

$$\operatorname{Hom}_R(R, f)(\rho_M(m))(r) = f(\rho_M(m)(r)) = f(rm) = r f(m) = \rho_N(f(m))(r),$$

so the naturality square commutes. For (2), the isomorphism $R \otimes_R M \cong M$ from (19.6) is given by $r \otimes m \mapsto rm$, with inverse $m \mapsto 1 \otimes m$. Naturality follows similarly: for $f: M \to N$,

$$f(\tau_M(r \otimes m)) = f(rm) = r f(m) = \tau_N(r \otimes f(m)) = \tau_N((1 \otimes f)(r \otimes m)).$$

Thus both $\rho$ and $\tau$ are natural isomorphisms.
