---
role: proof
locale: en
of_concept: fundamental-lemma-equivalence
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

Define $\phi(\gamma) = \eta_M \circ G(\gamma)$ for $\gamma \in \operatorname{Hom}_S(N, F(M))$, and define $\theta(\delta) = G(\delta) \circ \eta_M^{-1}$ for $\delta \in \operatorname{Hom}_S(F(M), N)$. Since $\eta_M$ is an isomorphism and $G$ is an additive functor, both $\phi$ and $\theta$ are group homomorphisms.

**Bijectivity of $\phi$**: Define $\phi^{-1}(\bar{\gamma}) = \zeta_{F(M)} \circ F(\bar{\gamma})$ for $\bar{\gamma} \in \operatorname{Hom}_R(G(N), M)$. Then

$$\phi(\phi^{-1}(\bar{\gamma})) = \eta_M \circ G(\zeta_{F(M)} \circ F(\bar{\gamma})) = \eta_M \circ G\zeta_{F(M)} \circ GF(\bar{\gamma}).$$

Using naturality, $\eta_M \circ G\zeta_{F(M)} \circ GF(\bar{\gamma}) = \bar{\gamma}$, so $\phi \circ \phi^{-1} = 1$. Similarly, $\phi^{-1} \circ \phi = 1$.

**Naturality (1)**: For $\gamma: N_1 \to F(M_1)$, $h: M_1 \to M_2$, $k: N_2 \to N_1$:

$$\phi(F(h)\gamma k) = \eta_{M_2} \circ G(F(h)\gamma k) = \eta_{M_2} \circ GF(h) \circ G(\gamma) \circ G(k).$$

By naturality of $\eta$, $\eta_{M_2} \circ GF(h) = h \circ \eta_{M_1}$, so

$$\phi(F(h)\gamma k) = h \circ \eta_{M_1} \circ G(\gamma) \circ G(k) = h \phi(\gamma) G(k).$$

The formulas (2)-(4) follow by similar computations using the naturality of $\eta$ and $\zeta$.

**Preservation of monics/epics**: $\phi(\gamma) = \eta_M \circ G(\gamma)$. Since $\eta_M$ is an isomorphism, $\phi(\gamma)$ is monic (epic) iff $G(\gamma)$ is monic (epic). By (21.2), $G(\gamma)$ is monic (epic) iff $\gamma$ is monic (epic). The same reasoning applies to $\theta$.

**Adjoint relationship**: This shows that $(G, F)$ and $(F, G)$ are both adjoint pairs. The maps $\phi$ and $\theta$ provide the natural isomorphisms

$$\operatorname{Hom}_S(N, F(M)) \cong \operatorname{Hom}_R(G(N), M), \quad \operatorname{Hom}_S(F(M), N) \cong \operatorname{Hom}_R(M, G(N)).$$
