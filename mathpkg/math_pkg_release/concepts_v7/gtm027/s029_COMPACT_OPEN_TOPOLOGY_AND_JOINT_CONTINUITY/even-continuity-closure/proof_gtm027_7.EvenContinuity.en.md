---
role: proof
locale: en
of_concept: even-continuity-closure
source_book: gtm027
source_chapter: "7"
source_section: "Even Continuity"
---

# Proof of Theorem 7.19 — Even Continuity and Pointwise Closure

Let $F$ be an evenly continuous family of functions on a topological space $X$ to a regular space $Y$, and let $\wp$ be the topology of pointwise convergence. Then:

**(1) $\wp$ is jointly continuous on the closure $F^-$.** From the reformulation of even continuity: for each $x \in X$, $y \in Y$, and neighborhood $U$ of $y$, there exist neighborhoods $V$ of $x$ and $W$ of $y$ such that

$$\{f \in F : f(x) \in W\} \times V \subset P^{-1}[U].$$

The set $\{f : f(x) \in W\}$ is $\wp$-open whenever $W$ is open in $Y$ (it is a subbasic pointwise-open set). Hence the same inclusion holds for the $\wp$-closure $F^-$, establishing joint continuity of $\wp$ on $F^-$.

**(2) $F^-$ is evenly continuous.** Let $x \in X$, $y \in Y$, and let $U$ be a neighborhood of $y$. Since $Y$ is regular, choose an open neighborhood $U'$ of $y$ with $\overline{U'} \subset U$. By even continuity of $F$, there exist neighborhoods $V$ of $x$ and $W$ of $y$ such that for all $f \in F$, if $f(x) \in W$ then $f[V] \subset U'$.

Now for any $g \in F^-$ with $g(x) \in W$, the pointwise convergence of a net $\{f_\alpha\} \subset F$ to $g$ implies that eventually $f_\alpha(x) \in W$, so $f_\alpha[V] \subset U'$. Taking limits, for any $v \in V$, we have $g(v) = \lim f_\alpha(v) \in \overline{U'} \subset U$. Thus $F^-$ satisfies the definition of even continuity.
