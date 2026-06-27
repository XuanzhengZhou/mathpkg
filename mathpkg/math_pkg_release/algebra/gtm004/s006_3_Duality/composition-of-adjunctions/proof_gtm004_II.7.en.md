---
role: proof
locale: en
of_concept: composition-of-adjunctions
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Composition of Adjunctions

Let $F: \mathfrak{C} \to \mathfrak{D}$, $F': \mathfrak{D} \to \mathfrak{E}$, $G: \mathfrak{D} \to \mathfrak{C}$, $G': \mathfrak{E} \to \mathfrak{D}$ be functors and let $\eta: F \dashv G$, $\eta': F' \dashv G'$ be adjunctions with adjugant equivalences

$$\eta_{XY}: \mathfrak{D}(FX, Y) \xrightarrow{\cong} \mathfrak{C}(X, GY), \qquad \eta'_{YZ}: \mathfrak{E}(F'Y, Z) \xrightarrow{\cong} \mathfrak{D}(Y, G'Z).$$

Define $\eta''_{XZ}: \mathfrak{E}(F'F X, Z) \to \mathfrak{C}(X, GG'Z)$ by the composition

$$\eta''_{XZ} = \eta_{X, G'Z} \circ \eta'_{FX, Z}.$$

Explicitly, for $\varphi: F'F X \to Z$ in $\mathfrak{E}$,

$$\eta''(\varphi) = \eta(\eta'(\varphi)) = G(\eta'(\varphi)) \circ \varepsilon_X,$$

where $\varepsilon$ is the unit of $\eta$. Since $\eta$ and $\eta'$ are both natural equivalences (in each variable separately), their composition $\eta''$ is also a natural equivalence of functors $\mathfrak{C}^{\text{opp}} \times \mathfrak{E} \to \mathfrak{S}$. Hence $\eta'': F'F \dashv GG'$, i.e., the composition of left adjoints is left adjoint to the composition of right adjoints (in reverse order).
