---
role: proof
locale: en
of_concept: completeness-of-set
source_book: gtm005
source_chapter: "V"
source_section: "1"
---

Since $J$ is small, $\operatorname{Cone}(*, F)$ is a small set, hence an object of $\mathbf{Set}$. If $u : j \to k$ is any arrow of $J$, then $F_u \sigma_j = \sigma_k$ because $\sigma$ is a cone. Hence $v$ as defined in (2) is a cone, i.e., $F_u \circ v_j = v_k$ for all arrows $u$. Now let $\tau : M \to F$ be any other cone from a set $M$. For each $m \in M$, the collection $\{\tau_j(m)\}_{j \in \operatorname{obj}(J)}$ defines a cone $* \to F$ (since each $\tau$ is a cone), hence an element of $\operatorname{Cone}(*, F)$. Define $g : M \to \operatorname{Cone}(*, F)$ by $g(m) = \{\tau_j(m)\}_{j}$. Then $v_j(g(m)) = \tau_j(m)$, so $v \circ g = \tau$. If $g'$ is another such function, then $v_j(g'(m)) = \tau_j(m)$ forces $g'(m) = \{\tau_j(m)\}_{j} = g(m)$, so $g$ is unique. Thus $v$ is a universal cone, and $\operatorname{Cone}(*, F)$ is the limit.
