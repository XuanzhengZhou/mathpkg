---
role: proof
locale: en
of_concept: products-of-pseudo-metrizable-spaces
source_book: gtm036
source_chapter: "6"
source_section: "6.10"
---

Observe that, if the product is pseudo-metrizable, then, since each $E_t$ is isomorphic to a subspace of the product, each coordinate space is pseudo-metrizable. Suppose that $A$ is uncountable. Each neighborhood of $0$ in the product contains a finite intersection of neighborhoods of the form $\{x : x(t) \in U\}$, where $U$ is a neighborhood of $0$ in a coordinate space $E_t$. Hence, if $N$ is the intersection of countably many neighborhoods of $0$ in the product, then there is a countable set $B$ of indices and a neighborhood $U_t$ of $0$ in $E_t$ for each $t$ in $B$ such that $N$ contains $\{x : x(t) \in U_t \text{ for all } t \in B\}$. Since $A$ is uncountable and each $E_t$ is non-trivial, this set cannot be contained in any neighborhood of $0$ of the form $\{x : x(t_0) \in V\}$ for $t_0 \notin B$. Therefore no countable family of neighborhoods of $0$ can form a local base. By the Metrization Theorem (6.7), the product is not pseudo-metrizable. This proves necessity.

For sufficiency, if each $E_t$ is pseudo-metrizable and $A$ is countable, then each $E_t$ has a countable local base, and one can construct a countable local base for the product using finite intersections of cylinder sets formed from these bases. By the Metrization Theorem (6.7), the product is pseudo-metrizable.
