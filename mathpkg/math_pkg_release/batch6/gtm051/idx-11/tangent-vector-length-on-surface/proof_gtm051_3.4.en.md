---
role: proof
locale: en
of_concept: tangent-vector-length-on-surface
source_book: gtm051
source_chapter: "3"
source_section: "3.4"
---

\textbf{Proof.} By the chain rule,
$$\dot{c}(t) = dc_t(1) = df_{u(t)} \circ du_t(1) = df_{u(t)}\!\left(\sum_i \dot{u}^i(t) \, e_i\right) = \sum_i \dot{u}^i(t) \, (f_{u^i} \circ u)(t),$$
where $e_i$ are the standard basis vectors of $\mathbb{R}^2$. This shows $\dot{c}(t)$ lies in the image of $df_{u(t)}$, hence it is a tangent vector to $f$ at $u(t)$.

The squared length follows directly from the definition of the inner product:
$$|\dot{c}(t)|^2 = \langle \dot{c}(t), \dot{c}(t) \rangle = \left\langle \sum_i \dot{u}^i \, f_{u^i}, \sum_j \dot{u}^j \, f_{u^j} \right\rangle = \sum_{i,j} \langle f_{u^i}, f_{u^j} \rangle \, \dot{u}^i \dot{u}^j = \sum_{i,j} g_{ij}(u(t)) \, \dot{u}^i(t) \, \dot{u}^j(t).$$
The last equality uses the definition $g_{ij} = \langle f_{u^i}, f_{u^j} \rangle$ of the coefficients of the first fundamental form. $\square$
