---
role: proof
locale: en
of_concept: locally-convex-characterization
source_book: gtm055
source_chapter: "14"
source_section: "15"
---
If $\sigma$ is a pseudonorm on $\mathcal{E}$ then every ball $\{x \in \mathcal{E} : \sigma(x - x_0) < r\}$ is convex, so (i) implies (ii). Clearly (ii) implies (iii). For (iii) implies (iv): every absolutely convex set is convex. To see (iv) implies (i): let $C$ be a convex neighborhood of $0$, and $V \subset C$ a balanced neighborhood of $0$. Then $W = \bigcap_{|\gamma| = 1} \gamma C$ is an absolutely convex neighborhood of $0$ contained in $C$. Given a neighborhood base $\{V_\gamma\}$ of absolutely convex sets, each $V_\gamma$ is absorbing with Minkowski functional $\sigma_\gamma$, a pseudonorm. Since $\{x : \sigma_\gamma(x) < 1\} \subset V_\gamma \subset \{x : \sigma_\gamma(x) \leq 1\}$, the topology induced by $\{\sigma_\gamma\}$ coincides with the given topology.
