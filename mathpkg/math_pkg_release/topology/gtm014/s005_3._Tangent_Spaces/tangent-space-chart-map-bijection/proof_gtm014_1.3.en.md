---
role: proof
locale: en
of_concept: tangent-space-chart-map-bijection
source_book: gtm014
source_chapter: "1"
source_section: "3"
---

**Proof.**

(a) $\lambda_\phi^p$ is injective. Suppose $\lambda_\phi^p(v_1) = \lambda_\phi^p(v_2)$, i.e., $[c_{v_1}] = [c_{v_2}]$ in $T_p X$. By definition of tangency, for every chart $\psi$ at $p$, we have $(d\psi \cdot c_{v_1})_0 = (d\psi \cdot c_{v_2})_0$. In particular, take $\psi = \phi$:
$$
(d\phi \cdot c_{v_1})_0 = (d\phi \cdot c_{v_2})_0.
$$
Now $c_{v_i}(t) = \phi^{-1}(\phi(p) + t v_i)$, so $\phi \cdot c_{v_i}(t) = \phi(p) + t v_i$, hence
$$
(d\phi \cdot c_{v_i})_0 = \frac{d}{dt}\Big|_{t=0} (\phi(p) + t v_i) = v_i.
$$
Therefore $v_1 = v_2$.

(b) $\lambda_\phi^p$ is surjective. Let $\alpha \in T_p X$ and let $c$ be a curve representing the equivalence class $\alpha$. Set $v = (d\phi \cdot c)_0 \in \mathbf{R}^n$. Consider the curve $c_v(t) = \phi^{-1}(\phi(p) + t v)$. By the calculation in part (a),
$$
(d\phi \cdot c_v)_0 = v.
$$
Thus $(d\phi \cdot c_v)_0 = v = (d\phi \cdot c)_0$, which means $c$ and $c_v$ are tangent at $p$. Consequently,
$$
\lambda_\phi^p(v) = [c_v] = [c] = \alpha.
$$
Hence $\lambda_\phi^p$ is onto.
