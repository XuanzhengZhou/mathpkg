---
role: proof
locale: en
of_concept: adjoint-equivalence-properties
source_book: gtm004
source_chapter: "II"
source_section: "7"
---

# Proof of Properties of the Natural Equivalence Between Right Adjoints

Let $F \dashv G$, $F \dashv G'$ with adjugants $\eta, \eta'$ and corresponding units $\varepsilon, \varepsilon'$, counits $\delta, \delta'$. Let $\theta: G \to G'$, $\bar{\theta}: G' \to G$ be defined as in (7.4), (7.5).

**(i)** We prove $\theta F \circ \varepsilon = \varepsilon'$ and $\delta \circ F\bar{\theta} = \delta'$.

$$\begin{aligned}
\theta_{FX} \circ \varepsilon_X &= \eta'(\delta_{FX}) \circ \varepsilon_X \\
&= G'\delta_{FX} \circ \eta'(1_{FG FX}) \circ \varepsilon_X \\
&= G'\delta_{FX} \circ \varepsilon'_{GFX} \circ \varepsilon_X \\
&= G'\delta_{FX} \circ G'F\varepsilon_X \circ \varepsilon'_X \quad (\text{by naturality of } \varepsilon') \\
&= G'(\delta_{FX} \circ F\varepsilon_X) \circ \varepsilon'_X \\
&= G'(1_{FX}) \circ \varepsilon'_X \quad (\text{by (7.2)}) \\
&= \varepsilon'_X.
\end{aligned}$$

And

$$\begin{aligned}
\delta_Y \circ F\bar{\theta}_Y &= \delta_Y \circ F\eta(\delta'_Y) \\
&= \delta_Y \circ FG\delta'_Y \circ F\varepsilon_{G'Y} \\
&= \delta'_Y \circ \delta_{FG'Y} \circ F\varepsilon_{G'Y} \quad (\text{by naturality of } \delta) \\
&= \delta'_Y \circ 1_{FG'Y} \quad (\text{by (7.2)}) \\
&= \delta'_Y.
\end{aligned}$$

**(ii)** For any $\varphi: FX \to Y$,

$$\begin{aligned}
\theta_Y \circ \eta(\varphi) &= \theta_Y \circ G\varphi \circ \varepsilon_X \\
&= G'\varphi \circ \theta_{FX} \circ \varepsilon_X \quad (\text{by naturality of } \theta) \\
&= G'\varphi \circ \varepsilon'_X \quad (\text{by (i)}) \\
&= \eta'(\varphi).
\end{aligned}$$

Conversely, if $\eta: F \dashv G$ and $\theta: G \to G'$ is a natural equivalence, then defining $\eta'(\varphi) = \theta_Y \circ \eta(\varphi)$ gives an adjunction $F \dashv G'$ whose unit and counit satisfy the relations in (i).
