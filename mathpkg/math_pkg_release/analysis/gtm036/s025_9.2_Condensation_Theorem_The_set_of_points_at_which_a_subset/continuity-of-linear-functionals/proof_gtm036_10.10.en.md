---
role: proof
locale: en
of_concept: continuity-of-linear-functionals
source_book: gtm036
source_chapter: "10"
source_section: "10.10"
---

For the first statement, suppose $r$ is bounded from above on $A$. Let $A_n = \{x \in A : r(x) \leq n\}$. Then $A_n$ has the Baire property and $A = \bigcup_n A_n$. Since $A$ is of the second category, some $A_n$ is of the second category. Then $A_n - A_n$, by the difference theorem, is a neighborhood of $0$. Hence $r$ is bounded on a neighborhood of $0$, so $r$ is continuous and therefore $f$ is continuous.

For the second statement, suppose $r$ is upper semi-continuous on $A$. For each positive integer $n$ let $A_n = \{x : x \in A \text{ and } r(x) < n\}$. Then $A_n$ is open in $A$, and therefore, being the intersection of $A$ and an open set, $A_n$ satisfies the condition of Baire. Finally, since $A$ is of the second category, $A_n$ is of the second category for some $n$, and the result of the first part implies that $f$ is continuous.
