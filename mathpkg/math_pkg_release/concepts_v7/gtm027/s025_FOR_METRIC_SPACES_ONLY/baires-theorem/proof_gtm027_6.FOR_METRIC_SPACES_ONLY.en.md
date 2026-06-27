---
role: proof
locale: en
of_concept: baires-theorem
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC_SPACES ONLY"
---

# Proof of Baire's Theorem

**Theorem 34 (Baire).** Let $X$ be either a complete pseudo-metric space or a locally compact regular space. Then the intersection of a countable family of dense open subsets of $X$ is dense.

**Proof.** Let $\{G_n : n \in \omega\}$ be a countable family of dense open subsets of $X$, and let $U$ be an arbitrary non-void open subset of $X$. We must show that $U \cap \bigcap \{G_n : n \in \omega\}$ is non-void.

We consider two cases.

**Case 1: $X$ is a complete pseudo-metric space.** Let $d$ be a pseudo-metric for $X$ such that $(X, d)$ is complete and the topology is the pseudo-metric topology. Choose $x_0 \in X$ and $r_0 > 0$ such that the open ball $U_{r_0}[x_0] \subset U$. Proceed by induction: having chosen $x_{n-1}$ and $r_{n-1} > 0$, since $G_n$ is dense and open, $U_{r_{n-1}}[x_{n-1}] \cap G_n$ is non-void and open, so we may choose $x_n$ and $r_n$ with $0 < r_n < 1/n$ such that the closed ball $U_{r_n}[x_n]^{-} \subset G_n \cap U_{r_{n-1}}[x_{n-1}]$. This choice is possible because $G_n$ is dense and open.

For $n > m$ we have $x_n \in U_{r_m}[x_m]$, so $d(x_m, x_n) < r_m < 1/m$. Hence $\{x_n\}$ is a Cauchy sequence. Since $X$ is complete, $\{x_n\}$ converges to some point $x \in X$. For each $m$, the tail $\{x_n : n \geq m\}$ is contained in $U_{r_m}[x_m]^{-}$, so $x \in U_{r_m}[x_m]^{-}$. Thus for each $m \geq 1$,

$$x \in U_{r_m}[x_m]^{-} \subset G_m \cap U_{r_{m-1}}[x_{m-1}].$$

In particular, $x \in U_{r_0}[x_0] \subset U$ and $x \in G_m$ for all $m \geq 1$. Therefore $x \in U \cap \bigcap_{n \in \omega} G_n$, as required.

**Case 2: $X$ is a locally compact regular space.** Choose a non-void open set $V_0$ such that $V_0^{-}$ is compact and $V_0^{-} \subset U$ (this is possible by local compactness and regularity). Proceed by induction: for each positive integer $n$, having chosen $V_{n-1}$, choose $V_n$ such that $V_n^{-}$ is a subset of $V_{n-1} \cap G_n$ (and in the metric case, the diameter of $V_n$ is less than $1/n$). This choice is possible because $G_n$ is dense and open.

The family of all sets $V_n^{-}$ for non-negative integers $n$ has the finite intersection property, consists of closed sets, and $V_0^{-}$ is compact (the family contains small sets in the metric case). Hence $\bigcap \{V_n^{-} : n \in \omega\}$ is non-void, and since $V_{n+1}^{-} \subset U \cap G_n$ it follows that $U \cap \bigcap \{G_n : n \in \omega\}$ is non-void.

In either case, we have shown that every non-void open set $U$ intersects $\bigcap_{n} G_n$, which is precisely the statement that $\bigcap_{n} G_n$ is dense in $X$.
