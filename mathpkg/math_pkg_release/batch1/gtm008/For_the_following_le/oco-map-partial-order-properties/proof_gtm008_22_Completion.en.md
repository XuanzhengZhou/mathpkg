---
role: proof
locale: en
of_concept: oco-map-partial-order-properties
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

**1.** Suppose $x \leq_1 y$. Then $x \in [y]_{P_1}$. Since $p$ is continuous and $[y]_{P_1}$ is the smallest open neighborhood of $y$, we have $[y]_{P_1} \subseteq p^{-1}``[p(y)]_{P_0}$. Therefore
$$p(x) \in [p(y)]_{P_0},$$
which means $p(x) \leq_0 p(y)$.

**2.** Since $p$ is an open map, the image of the basic open set $[x]_{P_1}$ is open and contains $p(x)$, hence $p``[x]_{P_1} \supseteq [p(x)]_{P_0}$.

Conversely, since $p$ is order-preserving (by part 1), for any $z \in [x]_{P_1}$ we have $p(z) \leq_0 p(x)$, so $p(z) \in [p(x)]_{P_0}$. Hence $p``[x]_{P_1} \subseteq [p(x)]_{P_0}$.

Therefore $p``[x]_{P_1} = [p(x)]_{P_0}$.
