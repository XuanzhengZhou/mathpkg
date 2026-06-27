---
role: proof
locale: en
of_concept: continuity-criteria-for-linear-functionals
source_book: gtm036
source_chapter: "10"
source_section: "10.10"
---

Let $r$ be the real part of $f$. If $r$ is bounded from above on a set $A$ of the second category satisfying the condition of Baire, then for some integer $n$, the set $\{x \in A: r(x) < n\}$ is of the second category. By the difference theorem, its difference with itself is a neighborhood of $0$. Hence $r$ is continuous and therefore $f$ is continuous.

For the second statement, suppose that $r$ is upper semi-continuous on $A$. For each positive integer $n$ let $A_n = \{x : x \in A \text{ and } r(x) < n\}$. Then $A_n$ is open in $A$, and therefore, being the intersection of $A$ and an open set, $A_n$ satisfies the condition of Baire. Since $A$ is of the second category, $A_n$ is of the second category for some $n$, and the result of the preceding paragraph implies that $f$ is continuous.
