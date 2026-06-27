---
role: proof
locale: en
of_concept: open-ball-is-open
source_book: gtm012
source_chapter: "1"
source_section: "5. Metric spaces"
---

# Proof of Theorem: Every Open Ball is an Open Set

Let $(S, d)$ be a metric space, $x \in S$, and $r > 0$. We claim that the ball $B_r(x)$ is an open set.

Suppose $y \in B_r(x)$. We want to show that for some $s > 0$, $B_s(y) \subset B_r(x)$. The triangle inequality makes this easy, for we can choose $s = r - d(y, x)$. (Since $y \in B_r(x)$, $s$ is positive.) If $z \in B_s(y)$, then

$$d(z, x) \leq d(z, y) + d(y, x) < s + d(y, x) = r.$$

Thus $z \in B_r(x)$. Since $y$ was an arbitrary point of $B_r(x)$, each point of $B_r(x)$ has a ball neighborhood contained in $B_r(x)$. Therefore $B_r(x)$ is open. $\square$
