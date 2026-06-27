---
role: proof
locale: en
of_concept: greens-formulae-riemannian
source_book: gtm051
source_chapter: "5"
source_section: "5.7"
---

**Proof.** First, establish the product rule for divergence:
$$\operatorname{div}(\psi X) = \frac{1}{\sqrt{g}} \sum_i \frac{\partial}{\partial u^i}(\sqrt{g} \, \psi \xi^i) = \psi \frac{1}{\sqrt{g}} \sum_i \frac{\partial}{\partial u^i}(\sqrt{g} \xi^i) + \sum_i \xi^i \frac{\partial \psi}{\partial u^i} = \psi \operatorname{div} X + d\psi(X).$$

In particular, for $X = \operatorname{grad} \psi_2$:
$$\operatorname{div}(\psi_1 \operatorname{grad} \psi_2) = \psi_1 \Delta\psi_2 + d\psi_1(\operatorname{grad} \psi_2) = \psi_1 \Delta\psi_2 + g(\operatorname{grad} \psi_1, \operatorname{grad} \psi_2).$$

Apply Gauss's theorem (5.6.9) to the vector field $\psi_1 \operatorname{grad} \psi_2$:
$$\iint_P \operatorname{div}(\psi_1 \operatorname{grad} \psi_2) \, dM = \int_{\partial P} i_{\psi_1 \operatorname{grad} \psi_2} dM.$$

The left side equals $\iint_P \psi_1 \Delta\psi_2 + g(\operatorname{grad} \psi_1, \operatorname{grad} \psi_2) \, dM$.

For the right side, using the physical interpretation of the line integral from the remark after (5.6.9): on $\partial P$, parameterized by arc length $c(t)$ with Frenet frame $\{e_1 = \dot{c}, e_2 = n\}$ (where $n$ is the inward normal), we have $i_X dM(\dot{c}) = -X \cdot e_2$. Identifying the outward normal as $-e_2$, we obtain
$$i_{\psi_1 \operatorname{grad} \psi_2} dM(\dot{c}) = \psi_1 g(\operatorname{grad} \psi_2, n) = \psi_1 d\psi_2(n) = \psi_1 \frac{\partial\psi_2}{\partial n}.$$
Thus the right side equals $\int_{\partial P} \psi_1 \frac{\partial\psi_2}{\partial n} ds$, proving Green's first identity.

Green's second identity follows by subtracting the first identity with $\psi_1$ and $\psi_2$ swapped from the original. $\square$
