---
role: proof
locale: en
of_concept: extreme-points-characterization
source_book: gtm040
source_chapter: "10"
source_section: "6"
---

First, if $x \in S$, then $h$ is normalized, so the $h$-process is defined. The $h$-process disappears with probability one, so $\mu^h(S^h) = 1$. By Theorem 10-26,
$$K(\cdot, x) = \int_{S^*} K(\cdot, y) d\mu^h(y) = \sum_j N_{\cdot j} (\mu^h(\{j\}) / N_{\pi j}).$$
But $K(\cdot, x) = N_{\cdot x} / N_{\pi x} = \sum_j N_{\cdot j} (\delta_{jx} / N_{\pi j})$. By uniqueness of charges (Theorem 8-4), $\mu^h(\{j\}) = \delta_{jx}$, so $\mu^h(\{x\}) = 1$.

Conversely, if $\mu^h(\{x\}) = 1$, then $h = \int K(\cdot, y) d\mu^h(y) = K(\cdot, x)$, so $x$ represents $h$. Since $h$ is normalized, $x$ satisfies the normalization condition. And since $\mu^h$ is a point mass, $K(\cdot, x)$ is minimal by Lemma 10-33, so $x$ is extreme.
