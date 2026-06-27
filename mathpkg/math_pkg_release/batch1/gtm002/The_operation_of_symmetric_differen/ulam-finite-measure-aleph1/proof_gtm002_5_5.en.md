---
role: proof
locale: en
of_concept: ulam-finite-measure-aleph1
source_book: gtm002
source_chapter: "5"
source_section: "5. Non-Measurable Sets"
---
By hypothesis, there exists a well ordering of $X$ such that for each $y$ in $X$ the set $\{x : x < y\}$ is countable. Let $f(x, y)$ be a one-to-one mapping of this set onto a subset of the positive integers. Then $f$ is an integer-valued function defined for all pairs $(x, y)$ of elements of $X$ for which $x < y$. It has the property:
$$x < x' < y \implies f(x, y) \neq f(x', y).$$

For each $x$ in $X$ and each positive integer $n$, define
$$F_x^n = \{y : x < y,\; f(x, y) = n\}.$$

These sets can be pictured as an array with $\aleph_0$ rows and $\aleph_1$ columns, where each column is indexed by $x$ and each row by $n$.

For each fixed $n$, the sets $F_x^n$ are disjoint for different $x$ (by property (1)). Since $\mu$ is a finite measure, only countably many of them can have positive measure. Hence, for each $n$, all but countably many of the $F_x^n$ have measure zero. Since there are only countably many $n$'s, it follows that there exists an element $x$ in $X$ such that $\mu(F_x^n) = 0$ for every $n$.

The union of the sets in this column (over all $n$) has measure zero. The set $\{y : y \leq x\}$ is countable; since $\mu(\{z\}) = 0$ for each singleton, this set also has measure zero. The complement of the union of the column and $\{y : y \leq x\}$ is empty (every $y > x$ belongs to some $F_x^n$ by definition of $f$). Therefore $\mu(X) = 0$, and so $\mu$ is identically zero.
