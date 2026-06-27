---
role: proof
locale: en
of_concept: metrization-theorem-bing-nagata-smirnov
source_book: gtm027
source_chapter: "4"
source_section: "Metrization"
---

# Proof of Bing-Nagata-Smirnov Metrization Theorem

**Bing-Nagata-Smirnov Metrization Theorem.** The following three conditions on a topological space are equivalent.

(a) The space is metrizable.
(b) The space is $T_1$ and regular, and the topology has a $\sigma$-locally finite base.
(c) The space is $T_1$ and regular, and the topology has a $\sigma$-discrete base.

*Proof.* $(c) \Rightarrow (b)$: A $\sigma$-discrete family is $\sigma$-locally finite, since each discrete family is locally finite. This implication is immediate.

$(b) \Rightarrow (a)$: This is the content of Lemmas 19 and 20. Lemma 19 shows that a regular space with a $\sigma$-locally finite base is normal. Lemma 20 then shows that a regular $T_1$-space with a $\sigma$-locally finite base is metrizable, by constructing a countable family of continuous pseudo-metrics that distinguishes points and closed sets and applying the embedding lemma together with Theorem 14.

$(a) \Rightarrow (c)$: By Theorem 21, each open cover of a pseudo-metric space has an open $\sigma$-discrete refinement. In a metric space, for each $n$, the open cover consisting of all $1/n$-spheres has an open $\sigma$-discrete refinement $\mathcal{U}_n$. The union $\bigcup_n \mathcal{U}_n$ is then a $\sigma$-discrete base for the topology. Hence a metrizable space has a $\sigma$-discrete base.

