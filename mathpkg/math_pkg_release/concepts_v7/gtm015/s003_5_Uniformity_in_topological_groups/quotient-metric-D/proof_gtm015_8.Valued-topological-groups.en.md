---
role: proof
locale: en
of_concept: quotient-metric-D
source_book: gtm015
source_chapter: "8"
source_section: "Valued topological groups"
---

# Proof of Quotient metric and value on $G/N$ from a left-invariant metric

Let $G$ be a metrizable topological group with a left-invariant compatible metric $d$, and let $N$ be a closed normal subgroup. Define $|x| = d(e, x)$ and for $u \in G/N$,

$$|u| = \inf \{|x| : x \in u\}.$$

Define a metric on the quotient by

$$D(u, v) = \inf \{d(x, y) : x \in u, y \in v\}.$$

By (8.5), $x \mapsto |x|$ is a value on $G$, and since $|x^{-1}y| = d(e, x^{-1}y) = d(x, y)$, the left value topology on $G$ is precisely the topology derived from $d$ (8.4). By (8.13), $u \mapsto |u|$ is a value on $G/N$ whose left value topology coincides with the quotient topology.

The left value topology on $G/N$ is, by definition, the topology derived from the left-invariant metric $(u, v) \mapsto |u^{-1}v|$. We complete the proof by showing $D(u, v) = |u^{-1}v|$.

Let $u, v \in G/N$. If $x \in u$ and $y \in v$, then $x^{-1}y \in u^{-1}v$, so

$$|u^{-1}v| \leq |x^{-1}y| = d(x, y).$$

Varying $x$ and $y$, we obtain $|u^{-1}v| \leq D(u, v)$.

Conversely, suppose $z \in u^{-1}v$. Write $z = x^{-1}y$ with $x \in u$, $y \in v$. Then

$$D(u, v) \leq d(x, y) = |x^{-1}y| = |z|.$$

Varying $z$, we obtain $D(u, v) \leq |u^{-1}v|$.

Thus $D(u, v) = |u^{-1}v|$, which establishes (i)-(iv). In particular, $D$ is a left-invariant metric on $G/N$ whose topology coincides with the quotient topology, and $u \mapsto |u|$ is the corresponding value.
