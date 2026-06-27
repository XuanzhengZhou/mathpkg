---
role: proof
locale: en
of_concept: uniqueness-of-right-adjoint
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Uniqueness of Right Adjoint up to Natural Equivalence

Suppose $F \dashv G$ and $F \dashv G'$ with adjugants $\eta: \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, GY)$ and $\eta': \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, G'Y)$. Let $\varepsilon, \varepsilon'$ be the corresponding units and $\delta, \delta'$ the counits.

Define natural transformations $\theta: G \to G'$ and $\bar{\theta}: G' \to G$ by

$$\theta_Y = \eta'(\delta_Y): GY \to G'Y, \qquad \bar{\theta}_Y = \eta(\delta'_Y): G'Y \to GY. \tag{7.4, 7.5}$$

We claim $\theta$ and $\bar{\theta}$ are mutual inverses. Compute for any $Y \in \mathfrak{D}$:

$$\begin{aligned}
\bar{\theta}_Y \circ \theta_Y &= \eta(\delta'_Y) \circ \eta'(\delta_Y) \\
&= \eta(\delta'_Y \circ F\eta'(\delta_Y)) \\
&= \eta(\delta'_Y \circ \delta_Y) \quad (\text{since } F\eta' \text{ inverts } \delta') \\
&= \eta(1_{FGY}) \\
&= 1_{GY}.
\end{aligned}$$

Similarly $\theta_Y \circ \bar{\theta}_Y = 1_{G'Y}$. Thus $\theta: G \cong G'$ is a natural equivalence. Hence $F$ determines its right adjoint uniquely up to natural equivalence.
