---
role: proof
locale: en
of_concept: characterization-of-spectrum-by-resolvent-norm
source_book: gtm003
source_chapter: "Appendix"
source_section: "1. Elementary Properties of the Resolvent"
---

The condition is clearly sufficient for $\lambda \in \sigma(u)$. To prove its necessity, suppose there exists a subsequence $\{\mu_n\}$ of $\{\lambda_n\}$ such that $\{R(\mu_n) : n \in \mathbb{N}\}$ is bounded. By the resolvent equation
$$R(\mu) - R(\nu) = (\mu - \nu) R(\mu) R(\nu)$$
the family $\{R(\mu_n)\}$ is a Cauchy sequence in $\mathcal{L}(E)$ and hence convergent to some $v \in \mathcal{L}(E)$. This implies
$$\lim_n R(\mu_n)(\mu_n e - u) = v(\lambda e - u) = e$$
and, similarly, $(\lambda e - u)v = e$. Hence we obtain $\lambda \in \rho(u)$, which is contradictory.
