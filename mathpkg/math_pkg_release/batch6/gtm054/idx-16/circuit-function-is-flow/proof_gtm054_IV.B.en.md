---
role: proof
locale: en
of_concept: circuit-function-is-flow
source_book: gtm054
source_chapter: "IV"
source_section: "B"
---

Represent the circuit $D$ by the list: $x_0, e_1, x_1, e_2, \ldots, e_m, x_m = x_0$ and let $\{I, J\}$ be a $2$-partition of $\{1, \ldots, m\}$ where
$$I = \{i : e_i = (x_{i-1}, x_i)\} \quad \text{and} \quad J = \{i : e_i = (x_i, x_{i-1})\}.$$

By definition, $h_D = \sum_{i \in I} c_{e_i} - \sum_{i \in J} c_{e_i}$. Hence,
$$\partial(h_D) = \sum_{i \in I} \partial(c_{e_i}) - \sum_{i \in J} \partial(c_{e_i})
= \sum_{i \in I} (c_{x_i} - c_{x_{i-1}}) - \sum_{i \in J} (c_{x_{i-1}} - c_{x_i}).$$

Since every vertex $x_k$ appears once as $c_{x_i}$ with $e_i = (x_{i-1}, x_i)$ and once as $c_{x_{i-1}}$ with $e_{i+1} = (x_i, x_{i+1})$ (or with opposite orientations via $J$), the alternating sum telescopes to zero. Thus $\partial(h_D) = 0$, which means $h_D \in \ker \partial = F(V)$.
