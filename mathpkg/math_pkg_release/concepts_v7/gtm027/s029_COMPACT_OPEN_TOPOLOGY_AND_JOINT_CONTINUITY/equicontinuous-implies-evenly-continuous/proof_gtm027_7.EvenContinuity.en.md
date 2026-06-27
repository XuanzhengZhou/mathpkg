---
role: proof
locale: en
of_concept: equicontinuous-implies-evenly-continuous
source_book: gtm027
source_chapter: "7"
source_section: "Even Continuity"
---

# Proof of Theorem 7.22 — Equicontinuity Implies Even Continuity

Let $F$ be an equicontinuous family of functions on a topological space $X$ to a uniform space $Y$. We show $F$ is evenly continuous.

Let $x \in X$, $y \in Y$, and let $U$ be a neighborhood of $y$. Without loss of generality, assume $U$ is the sphere of $d$-radius $r$ about $y$, where $d$ is a pseudo-metric belonging to the gage of $Y$ and $r > 0$. (The gage generates the uniformity, so neighborhoods of this form are cofinal.)

Since $F$ is equicontinuous at $x$, there exists a neighborhood $V$ of $x$ such that for all $v \in V$ and all $f \in F$,

$$d(f(x), f(v)) < r/2.$$

Let $W$ be the sphere of $d$-radius $r/2$ about $y$, i.e., $W = \{z \in Y : d(y, z) < r/2\}$. If $f(x) \in W$, then $d(y, f(x)) < r/2$. For any $v \in V$, the triangle inequality gives

$$d(y, f(v)) \leq d(y, f(x)) + d(f(x), f(v)) < r/2 + r/2 = r.$$

Thus $f(v) \in U$ whenever $f(x) \in W$ and $v \in V$. This establishes even continuity of $F$.
