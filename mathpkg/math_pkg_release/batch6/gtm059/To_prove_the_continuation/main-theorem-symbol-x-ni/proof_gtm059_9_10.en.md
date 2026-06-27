---
role: proof
locale: en
of_concept: main-theorem-symbol-x-ni
source_book: gtm059
source_chapter: "9"
source_section: "10"
---

By Lemma 4 of Section 5 in the preceding chapter, we have for $m \ge n$:
$$(x, n_i) = (3^i - 1)n_i.$$

This shifts the burden of the proof to level $n_i$, and we observe that $[3^i - 1]$ is compatible with the statement of the main lemma of the preceding section. To apply that main lemma, we require $m$ sufficiently large (implicitly $m \ge n = \kappa(n_i)$ for the main lemma) so that
$$\text{ord}_{\kappa}(3^i - 1) \ge n[2i] + 1 + 2e.$$

Since
$$[n^i]_{\kappa}(d_i) < p^i \quad \text{and} \quad [n^i]_{\kappa} \in n^{i+1}p^i,$$
it suffices to take $m \ge 4n + 1 + 4e$.

Setting $y = 3^{i+1}n^i$, we apply the main lemma of the preceding section to the level $n$ and an appropriate level to coordinate the symbols, yielding the desired equality under both conditions (i) and (ii).
