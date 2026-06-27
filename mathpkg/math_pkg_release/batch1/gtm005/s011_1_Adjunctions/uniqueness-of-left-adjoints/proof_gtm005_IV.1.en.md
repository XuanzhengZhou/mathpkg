---
role: proof
locale: en
of_concept: uniqueness-of-left-adjoints
source_book: gtm005
source_chapter: "IV"
source_section: "1"
---

If $F, F': D \to C$ are both left adjoint to $G: C \to D$, then $F \cong F'$.

Proof: Let $(\eta, \varepsilon)$ and $(\eta', \varepsilon')$ be the respective unit/counit pairs. Define $\alpha: F \Rightarrow F'$ by $\alpha_d = \varepsilon'_{F(d)} \circ F'(\eta_d): F(d) \to F'(G(F(d))) \to F'(d)$ — actually:
$$\alpha_d = \psi^{-1}_{d, F'(d)}(\eta'_d),$$
where $\psi$ comes from $F \dashv G$. Equivalently, $\alpha_d$ is the unique morphism with $G(\alpha_d) \circ \eta_d = \eta'_d$. 

Define $\beta: F' \Rightarrow F$ similarly with $G(\beta_d) \circ \eta'_d = \eta_d$. Then $G(\beta_d \circ \alpha_d) \circ \eta_d = \eta_d$, so by uniqueness $\beta_d \circ \alpha_d = 1_{F(d)}$. Similarly $\alpha_d \circ \beta_d = 1_{F'(d)}$. Thus $\alpha$ is a natural isomorphism.
