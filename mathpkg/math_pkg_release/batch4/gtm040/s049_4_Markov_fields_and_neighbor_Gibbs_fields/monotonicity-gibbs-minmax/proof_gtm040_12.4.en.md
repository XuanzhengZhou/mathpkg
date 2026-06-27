---
role: proof
locale: en
of_concept: monotonicity-gibbs-minmax
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** Fix $n \geq 1$ and consider $\mu_{n+1}^-$. For any $\kappa^{n+1} \in S^{K(n+1)}$, let $\kappa^n$ denote its restriction to $K(n)$. By the consistency of conditional probabilities (the local characteristics satisfy the Dobrushin-Lanford-Ruelle equations),

$$
\mu^{\kappa^{n+1}}([\kappa^0, \ldots, \kappa^m])
= \sum_{\tilde{\kappa}^{n+1}} \mu^{\tilde{\kappa}^{n+1}}([\kappa^0, \ldots, \kappa^m]) \cdot \nu^{\Lambda(n)}(\kappa^{n+1} \mid \tilde{\kappa}^{n+1}),
$$

where the sum runs over extensions of $\kappa^n$ to $K(n+1)$. Hence each $\mu^{\kappa^{n+1}}([\kappa^0, \ldots, \kappa^m])$ is a convex combination of the values $\mu^{\tilde{\kappa}^{n+1}}([\kappa^0, \ldots, \kappa^m])$ for $\tilde{\kappa}^{n+1}$ extending $\kappa^n$. Consequently,

$$
\min_{\kappa^{n+1}} \mu^{\kappa^{n+1}}([\kappa^0, \ldots, \kappa^m])
\geq \min_{\kappa^n} \mu^{\kappa^n}([\kappa^0, \ldots, \kappa^m]),
$$

which shows that $\mu_n^-$ is non-decreasing with $n$.

A similar estimate proves that $\mu_n^+$ is non-increasing with $n$. Since both sequences are bounded between $0$ and $1$, the limits exist.
