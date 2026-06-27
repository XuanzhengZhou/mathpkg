---
role: proof
locale: en
of_concept: finite-state-gibbs-existence-phase-criterion
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** The limits $\mu^+$ and $\mu^-$ are well-defined by the monotonicity established in Lemma 12-31.

We now show that for any given configuration $(\kappa^0, \ldots, \kappa^m)$ on $\Lambda(m)$, there is a random field $\mu \in \mathcal{G}_V$ such that $\mu([\kappa^0, \ldots, \kappa^m]) = \mu^-([\kappa^0, \ldots, \kappa^m])$. Let $\bar{\kappa}^n$ denote the configuration on $K(n)$ for which the minimum value $\mu_n^-$ is attained, and define measures $\mu_n$, $n \geq 1$, on $\Omega$ by

$$
\mu_n:
\begin{cases}
\mu_n([\iota_{\Lambda}]) = \mu^{\bar{\kappa}^n}([\iota_{\Lambda}]) & \text{whenever } \Lambda \subset \Lambda(n-1), \\[4pt]
\mu_n([\bar{\kappa}^n]) = 1, \\[4pt]
\mu_n(\{\omega : x_t = 0\}) = 1 & \text{whenever } t \notin \Lambda(n).
\end{cases}
$$

These specifications are clearly consistent, so each $\mu_n$ is well-defined. Now by the finiteness of $S$, we can use a diagonal argument to choose a subsequence $\{\mu_{n'}\}$ such that $\mu_{n'}([\iota_{\Lambda}]) \to \mu([\iota_{\Lambda}])$ for all possible configurations on every finite $\Lambda \subset T$. By the extension theorem, these cylinder limits give rise to a unique $\mu$ on $\Omega$.

Now observe that

$$
\mu([\kappa^0, \ldots, \kappa^m]) = \lim_{n' \to \infty} \mu_{n'}([\kappa^0, \ldots, \kappa^m]) = \mu^-([\kappa^0, \ldots, \kappa^m]).
$$

One verifies that $\mu \in \mathcal{G}_V$. A symmetric construction with $\mu_n^+$ yields another field in $\mathcal{G}_V$ whose marginals equal $\mu^+$. If $\mu^+ \neq \mu^-$, then $|\mathcal{G}_V| \geq 2$. Since $\mathcal{G}_V$ is convex and contains two distinct measures, it must contain infinitely many (take convex combinations). Hence $|\mathcal{G}_V| = \infty$, i.e., phase multiplicity. Conversely, if $\mu^+ = \mu^-$ for all cylinder sets, then any $\mu \in \mathcal{G}_V$ must have cylinder probabilities squeezed between the same limits, forcing a unique Gibbs field.
