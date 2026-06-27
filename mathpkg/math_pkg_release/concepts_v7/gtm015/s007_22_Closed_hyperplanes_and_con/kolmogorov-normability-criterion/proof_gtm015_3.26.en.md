---
role: proof
locale: en
of_concept: kolmogorov-normability-criterion
source_book: gtm015
source_chapter: "3"
source_section: "26"
---

# Proof of Kolmogorov normability criterion

If $E$ is normable, and if $x \mapsto \|x\|$ is a norm on $E$ that generates the topology, then $U = \{x : \|x\| \le 1\}$ is a bounded (26.3) and convex (25.2) neighborhood of $\theta$. Obviously $E$ is separated (as is any metrizable space).

Conversely, suppose $E$ is a separated TVS possessing a bounded convex neighborhood $U$ of $\theta$. Let $V$ be a balanced neighborhood of $\theta$ such that $V \subset U$ (17.9). Then $\operatorname{conv} V \subset \operatorname{conv} U = U$, so $W = \operatorname{conv} V$ is a convex, balanced (25.15) neighborhood of $\theta$ contained in $U$. Replacing $U$ by $W$, we can assume $U$ is balanced.

Define the Minkowski functional (also called the gauge) of $U$:

$$\|x\| = \inf \{\lambda > 0 : x \in \lambda U\}.$$

Since $U$ is absorbent (17.11), $\|x\| < \infty$ for all $x$. The properties of $U$ (convex, balanced, bounded) imply that $\|\cdot\|$ is a norm:

- $\|x\| \ge 0$, and $\|x\| = 0$ iff $x = \theta$ (because $U$ is bounded and $E$ is separated);
- $\|\lambda x\| = |\lambda| \|x\|$ (because $U$ is balanced);
- $\|x + y\| \le \|x\| + \|y\|$: Given $\varepsilon > 0$, let $\alpha = \|x\| + \varepsilon$, $\beta = \|y\| + \varepsilon$. Then $x \in \alpha U$, $y \in \beta U$. By convexity and (25.10),
  $$x + y \in \alpha U + \beta U = (\alpha + \beta)U,$$
  so $\|x + y\| \le \alpha + \beta = \|x\| + \|y\| + 2\varepsilon$.

It remains to show the norm topology coincides with the given topology. Since $U$ is bounded, for any neighborhood $V$ of $\theta$, there exists $\lambda > 0$ such that $U \subset \lambda V$. If $\|x\| < |\lambda|^{-1}$, then $x \in \lambda^{-1}U \subset V$. Conversely, for $\varepsilon > 0$, $\{x : \|x\| \le \varepsilon\} = \varepsilon U$ contains the neighborhood $\varepsilon \operatorname{int} U$ of $\theta$. Thus the topologies coincide.
