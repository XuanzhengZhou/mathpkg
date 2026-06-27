---
role: proof
locale: en
of_concept: bilinear-forms-to-linear-maps
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

Given a linear map $f: V \to V^*$, define a bilinear form $\sigma$ by $\sigma(a, b) = (af)(b)$ for all $a, b \in V$. The bilinearity of $\sigma$ follows from the linearity of $f$ and the fact that $af$ is a linear form on $V$.

Conversely, given $\sigma \in \mathcal{B}(V)$, define $\varrho: V \to V^*$ by $(a\varrho)(b) = \sigma(a, b)$. Then $a\varrho$ is a linear form on $V$ because $\sigma$ is linear in the second variable, and $\varrho$ is linear because $\sigma$ is linear in the first variable.

The mapping $f \mapsto \sigma$ constructed above is the inverse of $\sigma \mapsto \varrho$, hence $\sigma \mapsto \varrho$ is one-to-one and onto $\mathcal{L}(V, V^*)$.

The linearity follows immediately from the definitions of $\sigma + \tau$ and $x\sigma$: for any $a, b \in V$,
$$(a(\varrho_\sigma + \varrho_\tau))(b) = \sigma(a, b) + \tau(a, b) = (a\varrho_\sigma)(b) + (a\varrho_\tau)(b),$$
$$(a(x\varrho_\sigma))(b) = x\sigma(a, b) = x(a\varrho_\sigma)(b).$$

Thus $\sigma \mapsto \varrho$ is a linear isomorphism.
