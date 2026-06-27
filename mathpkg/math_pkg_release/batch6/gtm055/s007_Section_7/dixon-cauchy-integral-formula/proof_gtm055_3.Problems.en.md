---
role: proof
locale: en
of_concept: dixon-cauchy-integral-formula
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

The two definitions agree on $U \cap V$ since for $\lambda \in U \cap V$, the integrands differ by $f(\lambda)/(\zeta - \lambda)$, and $\int_{\gamma} f(\lambda)/(\zeta - \lambda) d\zeta = f(\lambda) w_{\gamma}(\lambda) \cdot 2\pi i = 0$ because $w_{\gamma}(\lambda) = 0$ on $V$. Thus $h$ is well-defined on $U \cup V$. By Problem G, $h$ is differentiable at each point of $V$. Using Problem L for continuity and the interchange of iterated integrals, together with Morera's theorem (Exercise L), $h$ is also differentiable on $U$. Hence $h$ is locally analytic on $U \cup V$.
