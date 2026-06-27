---
role: proof
locale: en
of_concept: particle-orbit-ode
source_book: gtm048
source_chapter: "7"
source_section: "7.4"
---

Write $\gamma_* = a_1 \partial + a_2 (\partial/\partial r) \circ \gamma + \delta_*$, where each $a_i \in \mathbb{R}$ and $\partial = (\partial/\partial t) \circ \gamma$ as in Proposition 7.3.7 and $Q_* \delta_* = 0$. Then $a_2 = dr(\gamma_*) = (r \circ \gamma)'$ and Proposition 7.3.7a implies that $a_1 = E(1 - 2\Delta \circ \gamma)^{-1}$. Hence,

$$
-m^2 = g(\gamma_*, \gamma_*) = -a_1^2(1 - 2\Delta \circ \gamma) + a_2^2(1 - 2\Delta \circ \gamma)^{-1} + \frac{J^2}{(r \circ \gamma)^2},
$$

where the last term follows from Proposition 7.3.7c. Substituting the values of $a_1$ and $a_2$ and simplifying algebraically,

$$
-m^2 = (1 - 2\Delta \circ \gamma)^{-1}\bigl(-E^2 + [(r \circ \gamma)']^2\bigr) + \frac{J^2}{(r \circ \gamma)^2}.
$$

Composing both sides on the right with $\kappa$ and rearranging yields

$$
[(r \circ \gamma)' \circ \kappa]^2 = E^2 - \left(1 - \frac{2\mu}{\tilde{\gamma}}\right)\left(m^2 + \frac{J^2}{\tilde{\gamma}^2}\right).
$$

It remains to identify the left side with $(f')^2$. By the definition of $\kappa$, $P \circ \gamma \circ \kappa$ is a unit-speed curve in $(S^2, h)$. This means

$$
1 = [h(\delta_*, \delta_*) \circ \kappa] \cdot (\kappa')^2 = \frac{(J\kappa')^2}{\tilde{\gamma}^4}.
$$

Moreover, $\tilde{\gamma}' = [(r \circ \gamma)' \circ \kappa] \cdot \kappa'$. Hence

$$
[(r \circ \gamma)' \circ \kappa]^2 \left(\frac{\mu}{J}\right)^2 = \left(\frac{\mu \tilde{\gamma}'}{\tilde{\gamma}^2}\right)^2 = (f')^2.
$$

Multiplying the rearranged equation by $(\mu/J)^2$ and substituting the definitions of $f$, $a$, and $b$ gives the desired result:

$$
(f')^2 = b + 2a f - f^2 + 2f^3.
$$
