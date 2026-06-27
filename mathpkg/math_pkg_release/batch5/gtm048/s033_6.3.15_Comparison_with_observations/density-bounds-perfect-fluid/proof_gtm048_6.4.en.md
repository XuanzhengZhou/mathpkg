---
role: proof
locale: en
of_concept: density-bounds-perfect-fluid
source_book: gtm048
source_chapter: "6"
source_section: "6.4"
---

$\operatorname{div} \hat{T} = 0$ implies $\operatorname{div} (\rho \partial_4) = -p \operatorname{div} \partial_4$ (Proposition 3.15.3), which is equivalent to $\partial_4 \rho = -(\rho + p) \operatorname{div} \partial_4$.

Now $\operatorname{div} \partial_4 = 3(\dot{R}/R) \circ u^4$ (Lemma 6.2.6c) and $0 < \rho \leq \rho + p \leq (4/3)\rho$ (Definition 3.15.2).

We thus get
$$
-3(\dot{R}/R) \circ u^4 \geq (\partial_4 \rho)/\rho \geq -4(\dot{R}/R) \circ u^4.
$$

Since $\partial_\mu \rho = 0$ for all $\mu = 1, 2, 3$ and $\dot{R} > 0$, an elementary integration gives (a).

(b) follows from the fact that the first (respectively, second) inequality in the derivation is an equality iff $p = 0$ (respectively, $p = \rho/3$). Specifically, $\rho + p = \rho$ when $p = 0$, giving the exponent 3, and $\rho + p = 4\rho/3$ when $p = \rho/3$, giving the exponent 4.
