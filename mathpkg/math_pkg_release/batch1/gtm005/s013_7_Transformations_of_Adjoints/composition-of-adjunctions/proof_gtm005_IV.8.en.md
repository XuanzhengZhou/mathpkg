---
role: proof
locale: en
of_concept: composition-of-adjunctions
source_book: gtm005
source_chapter: "IV"
source_section: "8. Composition of Adjoints"
---

The proof is a straightforward verification of the triangular identities for the composite adjunction. We have:

$$\bar{F}F : X \to D, \quad G\bar{G} : D \to X.$$

Define the unit $\eta'' = G\bar{\eta}F \cdot \eta : 1_X \to G\bar{G}\bar{F}F$ and the counit $\varepsilon'' = \bar{\varepsilon} \cdot \bar{F}\varepsilon\bar{G} : \bar{F}F G\bar{G} \to 1_D$.

First triangular identity: We need $(\varepsilon'' \bar{F}F) \circ (\bar{F}F \eta'') = 1_{\bar{F}F}$.
Compute:
$$\bar{F}F \xrightarrow{\bar{F}F\eta} \bar{F}FGF \xrightarrow{\bar{F}F G \bar{\eta} F} \bar{F}F G \bar{G} \bar{F} F \xrightarrow{\bar{F}\varepsilon\bar{G}\bar{F}F} \bar{F}\bar{G}\bar{F}F \xrightarrow{\bar{\varepsilon}\bar{F}F} \bar{F}F.$$

By naturality and the triangular identities for the individual adjunctions, this composite reduces to the identity.

Second triangular identity: $(G\bar{G} \varepsilon'') \circ (\eta'' G\bar{G}) = 1_{G\bar{G}}$ is verified similarly using the triangular identities for the component adjunctions.
