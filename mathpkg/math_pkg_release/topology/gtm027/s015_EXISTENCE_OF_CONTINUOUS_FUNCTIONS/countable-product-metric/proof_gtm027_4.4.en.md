---
role: proof
locale: en
of_concept: countable-product-metric
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Countable Product Metric

**Theorem 14.** Let $\{(X_n, d_n), n \in \omega\}$ be a sequence of pseudo-metric spaces, each of diameter at most one, and define $d$ by

$$d(x, y) = \sum_{n=0}^{\infty} 2^{-n} d_n(x_n, y_n).$$

Then $d$ is a pseudo-metric for the cartesian product, and the pseudo-metric topology is the product topology.

*Proof.* The simple proof that $d$ is a pseudo-metric is omitted (Problem 2.G on summability contains the necessary machinery).

To show the two topologies are identical, first observe that if $V$ is a $2^{-p}$-sphere about a point $x$ of the product and

$$U = \{y : d_n(x_n, y_n) < 2^{-p-n-2} \text{ for } n \leq p+2\},$$

then $U \subset V$, for if $y \in U$, then

$$d(x, y) < \sum_{n=0}^{p+2} 2^{-p-n-2} + \sum_{n=p+3}^{\infty} 2^{-n} < 2^{-p-1} + 2^{-p-1} = 2^{-p}.$$

But $U$ is a neighborhood of $x$ in the product topology and it follows that each set which is open relative to the pseudo-metric topology is open in the product topology.

Conversely, if $U$ is a neighborhood of $x$ in the product topology, then $U$ contains a set of the form $\{y: d_n(x_n, y_n) < r_n \text{ for } n \leq m\}$ for some positive numbers $r_n$ and integer $m$. Choose $p$ so that $2^{-p} < \min\{2^{-n} r_n : n \leq m\}$. Then the $2^{-p}$-sphere about $x$ is contained in $U$. Hence the product topology and the pseudo-metric topology coincide.

