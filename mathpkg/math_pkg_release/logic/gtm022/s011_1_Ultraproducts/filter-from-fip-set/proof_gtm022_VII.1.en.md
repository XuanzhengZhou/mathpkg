---
role: proof
locale: en
of_concept: filter-from-fip-set
source_book: gtm022
source_chapter: "VII"
source_section: "1"
---

The necessity of the condition is immediate, so we prove its sufficiency. Suppose $S$ has the finite intersection property, and put

$$T = \{ U \subseteq I \mid U = J_1 \cap \cdots \cap J_n \text{ for some } n \text{ and some } J_1, \ldots, J_n \in S \}.$$

Let

$$\mathcal{F} = \{ F \subseteq I \mid F \supseteq U \text{ for some } U \in T \}.$$

We prove that $\mathcal{F}$, which clearly contains $S$, is a filter. By the finite intersection property of $S$, $\varnothing \notin T$ and so $\varnothing \notin \mathcal{F}$. Also, condition (ii) for a filter is clearly satisfied by $\mathcal{F}$. Finally, if $F_1, \ldots, F_n \in \mathcal{F}$, then for $i = 1, \ldots, n$, $F_i \supseteq \bigcap_{j=1}^{m_i} J_{ij}$ for some $m_i$ and $J_{i1}, \ldots, J_{im_i} \in S$. Hence

$$\bigcap_{i=1}^{n} F_i \supseteq \bigcap_{i=1}^{n} \bigcap_{j=1}^{m_i} J_{ij},$$

and so belongs to $\mathcal{F}$. Thus condition (iii) is satisfied and $\mathcal{F}$ is a filter.
