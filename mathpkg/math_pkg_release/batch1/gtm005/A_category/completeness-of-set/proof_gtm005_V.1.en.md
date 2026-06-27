---
role: proof
locale: en
of_concept: completeness-of-set
source_book: gtm005
source_chapter: "V"
source_section: "1. Creation of Limits"
---

Since $J$ is small, $\operatorname{Cone}(*, F)$ is a small set, hence an object of $\mathbf{Set}$. If $u : j \rightarrow k$ is any arrow of $J$, then $F_u \sigma_j = \sigma_k$ because $\sigma$ is a cone. Hence $v$ as defined in (2) is a cone to the base $F$. To show it is universal, let $\tau : X \rightarrow F$ be any other cone from a set $X$ to $F$. For each $x \in X$, the family $\{\tau_j x \mid j \in \operatorname{obj}(J)\}$ is a cone $* \to F$, hence an element of $\operatorname{Cone}(*, F)$. Define $h : X \rightarrow \operatorname{Cone}(*, F)$ by $h(x)_j = \tau_j x$. Then $v_j \circ h = \tau_j$ for all $j$, so $v \circ \Delta h = \tau$. If $h'$ also satisfies $v \circ \Delta h' = \tau$, then for each $x$, $v_j(h'(x)) = \tau_j x$, so $h'(x)_j = \tau_j x = h(x)_j$ for all $j$, hence $h' = h$. Thus $h$ is unique and $v$ is a limiting cone.
