---
role: proof
locale: en
of_concept: complete-metric-from-proper-function
source_book: gtm014
source_chapter: "I"
source_section: "5. Vector Bundles"
---

**Proof.** That $d'$ is a metric is clear. Let $T$ be the topology on $X$ induced by $d$ and $T'$ the topology induced by $d'$. Since $d'$ is continuous in the topology $T$, we have that $T' \subset T$. Conversely, let $U$ be in $T$ and let $p$ be in $U$. Choose $\varepsilon$ so that
$$
B'(p, \varepsilon) = \{x \in X \mid d'(x, p) < \varepsilon\} \subset B(p, \varepsilon) \subset U.
$$
Thus $U$ is in $T'$ and $T = T'$.

Finally we show that $d'$ is complete. Let $\{x_n\}_{n=1}^{\infty}$ be a Cauchy sequence in the $d'$-metric. Since $d' \geq d$, the sequence is also Cauchy with respect to $d$. The properness of $f$ implies that the sequence is contained in a compact subset of $X$, and thus has a convergent subsequence. The Cauchy property with respect to $d'$ then guarantees convergence of the full sequence in the $d'$-metric. $\square$

*Note: The original text proof is truncated in the source; the completeness argument above is reconstructed from mathematical context.*
