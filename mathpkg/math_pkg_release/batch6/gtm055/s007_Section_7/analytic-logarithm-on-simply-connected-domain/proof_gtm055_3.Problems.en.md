---
role: proof
locale: en
of_concept: analytic-logarithm-on-simply-connected-domain
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

Since $f$ has no zeros in $\Delta$, the function $f'(\lambda)/f(\lambda)$ is analytic on $\Delta$. As $\Delta$ is simply connected, Problem P(ii) provides a primitive $g(\lambda)$ on $\Delta$ such that $g'(\lambda) = f'(\lambda)/f(\lambda)$.

Adjusting $g$ by an additive constant so that $\exp(g(\lambda_0)) = f(\lambda_0)$ for some fixed $\lambda_0 \in \Delta$, one verifies that the function $h(\lambda) = f(\lambda) \exp(-g(\lambda))$ satisfies $h'(\lambda) \equiv 0$ and $h(\lambda_0) = 1$, hence $h \equiv 1$ on $\Delta$. Therefore $\exp(g(\lambda)) = f(\lambda)$ for all $\lambda \in \Delta$, and $g$ is the desired analytic logarithm.

For the special case $f(\lambda) = \lambda$ when $0 \notin \Delta$, the argument function $\arg \lambda = \operatorname{Im}(\log \lambda)$ is harmonic as the imaginary part of an analytic function.
