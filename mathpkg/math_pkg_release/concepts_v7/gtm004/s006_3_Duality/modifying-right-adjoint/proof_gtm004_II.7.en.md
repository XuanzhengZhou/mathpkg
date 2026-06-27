---
role: proof
locale: en
of_concept: modifying-right-adjoint
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Modifying the Right Adjoint to Obtain Strict Adjunction

Suppose $F \dashv G$ with unit $\varepsilon: 1 \to GF$ and counit $\delta: FG \to 1$, and assume $F$ is injective on objects (so we may regard $\mathfrak{C}$ as a subcategory of $\mathfrak{D}$ via $F$). Define a new functor $G': \mathfrak{D} \to \mathfrak{C}$ as follows.

For $Y \in \mathfrak{D}$, set

$$G'(Y) = \begin{cases} X & \text{if } Y = FX \text{ for some } X \in \mathfrak{C}, \\ GY & \text{otherwise}. \end{cases}$$

For $\beta: Y_1 \to Y_2$, define

$$G'(\beta) = \begin{cases}
G(\beta) & \text{if } Y_1, Y_2 \notin \operatorname{Im} F, \\
F^{-1}(\beta) & \text{if } Y_1, Y_2 \in \operatorname{Im} F, \\
G(\beta) \circ \varepsilon_X & \text{if } Y_1 = FX \in \operatorname{Im} F, Y_2 \notin \operatorname{Im} F, \\
\varrho_X \circ G(\beta) & \text{if } Y_1 \notin \operatorname{Im} F, Y_2 = FX \in \operatorname{Im} F,
\end{cases}$$

where $\varrho_X = \varepsilon_X^{-1} = \delta_{FX}$ (since $\varepsilon_X: X \to GFX$ and $\delta_{FX}: FGFX \to FX$ satisfy $\delta_{FX} \circ F\varepsilon_X = 1_{FX}$ and $G\delta_{FX} \circ \varepsilon_{GFX} = 1_{GFX}$ via the triangular identities; when $F$ is injective on objects, $\varepsilon_X$ becomes an isomorphism on the $G$-side). A straightforward verification shows $G'$ is a functor.

Define $\theta: G \to G'$ and $\bar{\theta}: G' \to G$ by

$$\theta_Y = \begin{cases} 1_{GY} & \text{if } Y \notin \operatorname{Im} F, \\ \varrho_X & \text{if } Y = FX, \end{cases} \qquad
\bar{\theta}_Y = \begin{cases} 1_{GY} & \text{if } Y \notin \operatorname{Im} F, \\ \varepsilon_X & \text{if } Y = FX. \end{cases}$$

These are natural and mutual inverses. By Proposition 7.4, $F \dashv G'$ with unit $\varepsilon'_X = \theta_{FX} \circ \varepsilon_X = \varrho_X \circ \varepsilon_X = 1_X$ and counit $\delta'$ given analogously. Thus $G'F = 1_{\mathfrak{C}}$ and $\varepsilon' = 1$, yielding a **strict** adjunction where the left adjoint is fully faithful.
