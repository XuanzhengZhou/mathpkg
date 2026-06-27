---
role: proof
locale: en
of_concept: universal-property-of-direct-sum
source_book: gtm023
source_chapter: "I"
source_section: "4. Direct sum of vector spaces"
---

**Proof.** Define linear mappings
$$\sigma: G \to E \oplus F \quad \text{and} \quad \tau: E \oplus F \to G$$
by
$$\sigma z = (\psi_1 z, \psi_2 z), \quad z \in G$$
and
$$\tau(x, y) = \varphi_1 x + \varphi_2 y, \quad x \in E, \; y \in F.$$

Then for every vector $z \in G$,
$$\tau \sigma z = \varphi_1 \psi_1 z + \varphi_2 \psi_2 z = \iota_G z = z,$$
using the given relation $\varphi_1 \circ \psi_1 + \varphi_2 \circ \psi_2 = \iota_G$.

For every vector $(x, y) \in E \oplus F$,
$$\sigma \tau(x, y) = (\psi_1(\varphi_1 x + \varphi_2 y), \psi_2(\varphi_1 x + \varphi_2 y)) = (\psi_1 \varphi_1 x + \psi_1 \varphi_2 y, \psi_2 \varphi_1 x + \psi_2 \varphi_2 y).$$
Using the relations $\psi_1 \circ \varphi_1 = \iota_E$, $\psi_2 \circ \varphi_2 = \iota_F$, $\psi_1 \circ \varphi_2 = 0$, and $\psi_2 \circ \varphi_1 = 0$, we obtain
$$\sigma \tau(x, y) = (x, y).$$

These relations show that $\tau$ and $\sigma$ are inverse isomorphisms.

The compatibility formulas follow directly from the definition of $\tau$:
$$\tau \circ i_1(x) = \tau(x, 0) = \varphi_1 x + \varphi_2 0 = \varphi_1 x,$$
so $\varphi_1 = \tau \circ i_1$. Similarly $\varphi_2 = \tau \circ i_2$.

For the projections, $\pi_1 \circ \tau^{-1}(z) = \pi_1(\sigma z) = \pi_1(\psi_1 z, \psi_2 z) = \psi_1 z$, so $\psi_1 = \pi_1 \circ \tau^{-1}$, and analogously $\psi_2 = \pi_2 \circ \tau^{-1}$. $\square$
