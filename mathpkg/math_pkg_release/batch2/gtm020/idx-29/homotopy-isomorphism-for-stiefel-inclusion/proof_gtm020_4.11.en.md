---
role: proof
locale: en
of_concept: homotopy-isomorphism-for-stiefel-inclusion
source_book: gtm020
source_chapter: "4"
source_section: "11"
---

The map $j: V_k(F^n) \to V_{k+1}(F^{n+1})$ is defined by
$$j(v_1, \ldots, v_k) = (v_1, \ldots, v_k, e_{n+1}).$$
Consider the projection $p: V_{k+1}(F^{n+1}) \to V_1(F^{n+1})$ given by $p(v_1, \ldots, v_{k+1}) = v_{k+1}$.
This is a fibration whose fibre over the point $e_{n+1} \in V_1(F^{n+1})$ is precisely $V_k(F^n)$,
and $j$ is exactly the inclusion of this fibre.

From the homotopy exact sequence of this fibration, we have:
$$\pi_{i+1}(V_1(F^{n+1})) \to \pi_i(V_k(F^n)) \xrightarrow{j_*} \pi_i(V_{k+1}(F^n)) \to \pi_i(V_1(F^{n+1})).$$

Now $V_1(F^{n+1})$ is the sphere $S^{c(n+1)-1}$ (where $c = \dim_{\mathbf{R}} F$), and it is well known that
$\pi_q(S^m) = 0$ for $q < m$. Hence $\pi_{i+1}(V_1(F^{n+1})) = 0$ and $\pi_i(V_1(F^{n+1})) = 0$ for
$i \leq c(n+1) - 3$.

Therefore, for $i \leq c(n+1) - 3$, the homotopy exact sequence reduces to
$$0 \to \pi_i(V_k(F^n)) \xrightarrow{j_*} \pi_i(V_{k+1}(F^{n+1})) \to 0,$$
which shows that $j_*$ is an isomorphism in this range.
