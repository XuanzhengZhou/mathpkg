---
role: proof
locale: en
of_concept: unit-counit-adjunction
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Unit-Counit Characterization of Adjunctions

Suppose given functors $F: \mathfrak{C} \to \mathfrak{D}$, $G: \mathfrak{D} \to \mathfrak{C}$ and natural transformations $\varepsilon: 1_{\mathfrak{C}} \to GF$, $\delta: FG \to 1_{\mathfrak{D}}$ satisfying the triangular identities

$$\delta F \circ F\varepsilon = 1_F, \qquad G\delta \circ \varepsilon G = 1_G. \tag{7.2}$$

Define $\eta(\varphi) = G\varphi \circ \varepsilon_X$ for $\varphi: FX \to Y$. We show $\eta$ is an adjugant.

**Naturality of $\eta$.** For $\alpha: X' \to X$, $\beta: Y \to Y'$, $\varphi: FX \to Y$,

$$\begin{aligned}
\eta(\beta \circ \varphi \circ F\alpha) &= G(\beta \circ \varphi \circ F\alpha) \circ \varepsilon_{X'} \\
&= G\beta \circ G\varphi \circ GF\alpha \circ \varepsilon_{X'} \\
&= G\beta \circ G\varphi \circ \varepsilon_X \circ \alpha \quad (\text{since } \varepsilon \text{ is natural}) \\
&= G\beta \circ \eta(\varphi) \circ \alpha.
\end{aligned}$$

**Inverse.** Define $\xi(\psi) = \delta_Y \circ F\psi$ for $\psi: X \to GY$. Then $\xi$ is natural, and for $\varphi: FX \to Y$,

$$\begin{aligned}
\xi\eta(\varphi) &= \delta_Y \circ F\eta(\varphi) \\
&= \delta_Y \circ FG\varphi \circ F\varepsilon_X \\
&= \varphi \circ \delta_{FX} \circ F\varepsilon_X \quad (\text{since } \delta \text{ is natural}) \\
&= \varphi \quad (\text{by (7.2)}).
\end{aligned}$$

Thus $\xi\eta = 1$ and similarly $\eta\xi = 1$, so $\eta$ is a natural equivalence.

**Unit and counit.** If $\varepsilon', \delta'$ are the unit and counit of $\eta$, then

$$\varepsilon'_X = \eta(1_{FX}) = G(1_{FX}) \circ \varepsilon_X = \varepsilon_X,$$

$$\delta'_Y = \xi(1_{GY}) = \delta_Y \circ F(1_{GY}) = \delta_Y.$$

Hence $\eta: F \dashv G$ with unit $\varepsilon$ and counit $\delta$.

Conversely, given an adjunction $\eta: F \dashv G$, define $\varepsilon_X = \eta(1_{FX})$ and $\delta_Y = \eta^{-1}(1_{GY})$. Then $\varepsilon: 1 \to GF$ and $\delta: FG \to 1$ are natural and satisfy (7.2).
