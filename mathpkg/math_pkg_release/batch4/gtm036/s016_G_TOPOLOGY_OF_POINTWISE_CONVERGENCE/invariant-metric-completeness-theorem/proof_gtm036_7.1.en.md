---
role: proof
locale: en
of_concept: invariant-metric-completeness-theorem
source_book: gtm036
source_chapter: "7"
source_section: "7.1"
---

($\Rightarrow$) If $E$ is a complete linear topological space and $d$ is an invariant pseudo-metric inducing the topology, let $\{x_n\}$ be a $d$-Cauchy sequence. Then $\{x_n\}$ is also a Cauchy net in the topological sense. By completeness of $E$, $\{x_n\}$ converges topologically, hence converges relative to $d$. Thus $E$ is complete relative to $d$.

($\Leftarrow$) Suppose $E$ is complete relative to $d$ and let $\{x_\alpha\}_{\alpha \in A}$ be a Cauchy net in $E$. By invariance, $d(x_\alpha - x_\beta, 0) = d(x_\alpha, x_\beta) \to 0$. Consider the filter of sections of this net. Since $E$ is complete relative to $d$, one can show that the net clusters at some point, and by Cauchy property, converges. More precisely, the invariance implies $d(x_\alpha, x_\beta) \to 0$ iff the net is $d$-Cauchy, and $d$-completeness ensures convergence in the metric topology, which equals the given topology. Therefore $E$ is complete.

For the necessity of invariance: consider $\mathbb{R}$ with $d(x,y) = |\arctan x - \arctan y|$. This metric induces the usual topology of $\mathbb{R}$, and $\mathbb{R}$ is a complete LTS under the usual topology. However, the sequence $x_n = n$ is $d$-Cauchy (since $\arctan n \to \pi/2$) but does not converge in $\mathbb{R}$, so $\mathbb{R}$ is not complete relative to $d$. Here $d$ is not invariant.
