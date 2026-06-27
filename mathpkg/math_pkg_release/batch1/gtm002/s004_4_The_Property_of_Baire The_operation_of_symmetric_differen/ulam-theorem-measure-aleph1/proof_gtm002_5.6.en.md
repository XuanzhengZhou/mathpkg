---
role: proof
locale: en
of_concept: ulam-theorem-measure-aleph1
source_book: gtm002
source_chapter: "5"
source_section: "Non-Measurable Sets"
---

**Proof.** By hypothesis, there exists a well-ordering of $X$ such that for each $y \in X$, the set $\{x : x < y\}$ is countable. Let $f(x, y)$ be a one-to-one mapping of this set onto a subset of the positive integers, defined for all pairs $(x, y)$ with $x < y$. Then $f$ has the property:

$$x < x' < y \quad \text{implies} \quad f(x, y) \neq f(x', y).$$

For each $x \in X$ and each positive integer $n$, define

$$F_x^n = \{y : x < y, \; f(x, y) = n\}.$$

Arrange these sets in a matrix with $\aleph_0$ rows and $\aleph_1$ columns. For each fixed $y$, the sets $\{F_x^n : x < y\}$ are disjoint for different $n$. Since the rows correspond to a countable partition of the set $\{y : x < y\}$ for a fixed $x$, each column has the property that for any fixed $n$, the sets $F_x^n$ ($x \in X$) are disjoint.

Since there are only $\aleph_0$ rows and $\mu(X) < \infty$, there must be a row $n$ for which the sum of $\mu(F_x^n)$ over all $x$ does not diverge. Fixing this $n$, and since the sets $F_x^n$ are disjoint for different $x$, there can be only countably many $x$ with $\mu(F_x^n) > 0$. Since there are $\aleph_1$ columns, there exists $x \in X$ such that $\mu(F_x^n) = 0$ for every $n$. The union of the sets in this column has measure zero, and the complementary countable set also has measure zero. Therefore $\mu(X) = 0$, and $\mu$ is identically zero. $\square$
