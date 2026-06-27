---
role: proof
locale: en
of_concept: normalized-kernel-a-e
source_book: gtm040
source_chapter: "10"
source_section: "6"
---

For each $i$, $K(i, x)$ is continuous, hence Borel measurable. Therefore $\pi K(\cdot, x)$ is Borel measurable, and the set where it equals $1$ is a Borel set.

By Corollary 10-22, $\int_{S^*} K(i, x) d\mu(x) = 1$. By Fubini's theorem,
$$1 = \pi 1 = \pi \int_{S^*} K(\cdot, x) d\mu(x) = \int_{S^*} \pi K(\cdot, x) d\mu(x).$$
But $\int_{S^*} 1 d\mu(x) = 1$ also, and since $1 - \pi K(\cdot, x) \geq 0$, we conclude $\pi K(\cdot, x) = 1$ a.e. $[\mu]$.
