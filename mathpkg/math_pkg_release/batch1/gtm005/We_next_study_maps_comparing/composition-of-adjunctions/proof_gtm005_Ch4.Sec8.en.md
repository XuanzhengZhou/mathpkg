---
role: proof
locale: en
of_concept: composition-of-adjunctions
source_book: gtm005
source_chapter: "IV"
source_section: "8"
---

**Proof.** We verify that the composite functors $\bar{F}F : X \to D$ and $G\bar{G} : D \to X$ with the specified unit $\eta_{\text{comp}} = G\bar{\eta}F \cdot \eta$ and counit $\varepsilon_{\text{comp}} = \bar{\varepsilon} \cdot \bar{F}\varepsilon\bar{G}$ satisfy the triangle identities.

For any $x \in X$, the first triangle identity requires
$$\bar{F}F \xrightarrow{\bar{F}F \eta_{\text{comp}}} \bar{F}F G\bar{G} \bar{F}F \xrightarrow{\varepsilon_{\text{comp}} \bar{F}F} \bar{F}F$$
to be the identity. Computing componentwise:
$$\varepsilon_{\text{comp}, \bar{F}Fx} \circ \bar{F}F(\eta_{\text{comp}, x}) = \bar{\varepsilon}_{\bar{F}Fx} \cdot \bar{F}\varepsilon_{\bar{G}\bar{F}Fx} \cdot \bar{F}F G\bar{\eta}_{Fx} \cdot \bar{F}F\eta_x.$$
By naturality, this reduces to $\bar{\varepsilon}_{\bar{F}Fx} \cdot \bar{F}\eta_{\bar{F}Fx} \cdot \bar{F}\varepsilon_{Fx} \cdot \bar{F}F\eta_x$. The first pair gives $\text{id}_{\bar{F}Fx}$ by the triangle identity for $\langle \bar{F}, \bar{G}, \bar{\eta}, \bar{\varepsilon} \rangle$, and the second pair gives $\bar{F}(\text{id}_{Fx})$ by the triangle identity for $\langle F, G, \eta, \varepsilon \rangle$. Hence the composite is the identity.

The second triangle identity is verified dually. Therefore $\langle \bar{F}F, G\bar{G}, \eta_{\text{comp}}, \varepsilon_{\text{comp}} \rangle$ is indeed an adjunction.
