---
role: proof
locale: en
of_concept: exponential-convergence-markov
source_book: gtm046
source_chapter: "VIII-IX"
source_section: "30-31"
---

For, if $H$ is a Hahn set for the difference of probabilities in $\Delta_h$, then $$P^h(x, S') - P^h(y, S') \leq 1 - \{P^h(x, H^c) + P^h(y, H)\} \leq 1 - \{P^h(x, H^c S) + P^h(y, HS)\} \leq 1 - \left\{ \int_{H^c S} p^h(x, y) \mu(dy) + \int_{HS} p^h(y, z) \mu(dz) \right\} \leq 1 - \delta \mu(S) < 1.$$ Hence $\Delta_h < 1$ and exponential convergence follows.
