---
role: proof
locale: en
of_concept: proposition-10-35
source_book: gtm040
source_chapter: "10"
source_section: "35"
---

**Proof:** First let $x \in S$. Then $h$ is certainly normalized, and hence the $h$-process is defined. Suppose we can prove that the $h$-process disappears with probability one. Then by definition of $\mu^h$, $\mu^h(S^h) = 1$. Hence by Theorem 10-26,

$$K(\cdot, x) = \int_{S^*} K(\cdot, y) d\mu^h(y) = \int_S K(\cdot, y) d\mu^h(y) = \sum_j N_{ij} \left( \frac{\mu^h(\{j\})}{N_{\pi j}} \right).$$

But $K(\cdot, x) = N_{ix}/N_{\pi x} = \sum_j N_{ij} (\delta_{jx}/N_{\pi j})$. By Theorem 8-4,
