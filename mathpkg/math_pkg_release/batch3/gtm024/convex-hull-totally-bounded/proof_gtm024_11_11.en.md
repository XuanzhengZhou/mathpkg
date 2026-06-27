---
role: proof
locale: en
of_concept: convex-hull-totally-bounded
source_book: gtm024
source_chapter: "§11"
source_section: "11.B"
---

Given $\varepsilon > 0$ and continuous seminorm $\rho$, let $\{x_1,\ldots,x_n\} \subset A$ be an $(\varepsilon/2,\rho)$-net. Let $B = \operatorname{co}(\{x_1,\ldots,x_n\})$; $B$ is totally bounded (actually compact by 9E). Let $\{y_1,\ldots,y_m\}$ be an $(\varepsilon/2,\rho)$-net in $B$. For any $x = \sum \alpha_i a_i \in \operatorname{co}(A)$, approximate each $a_i$ by some $x_{k(i)}$, set $y = \sum \alpha_i x_{k(i)} \in B$, and find $y_j$ with $\rho(y - y_j) < \varepsilon/2$. Then $\rho(x - y_j) < \varepsilon$.