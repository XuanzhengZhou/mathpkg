---
role: proof
locale: en
of_concept: "let-be-a-complete-metric-space-and-let"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.65"
---

We will construct a one-to-one mapping of $\{0, 1\}^N$ into $A$. Since $A$ is nonvoid, it has a limit point and therefore $A$ is infinite (6.26). Let $x_0 \neq x_1$ in $A$. Let $\varepsilon_1 = \min \left\{\frac{1}{2}, \frac{1}{3} \varrho(x_0, x_1)\right\}$ and define $A(0) = \{x \in A : \varrho(x_0, x) \leq \varepsilon_1\}$ and $A(1) = \{x \in A : \varrho(x_1, x) \leq \varepsilon_1\}$. Then $A(0)$ and $A(1)$ are disjoint infinite closed sets each of diameter $\leq 1$. Suppose that $n$ is a positive integer and for each $n$-tuple $(a_1, \ldots, a_n) \in \{0, 1\}^n$ we have an infinite closed subset $A(a_1, \ldots, a_n)$ of $A$ having diameter $\leq \frac{1}{n}$ and such that no two of these sets have a common point. For $(a_1, \ldots, a_n) \in \{0, 1\}^n$, choose $x(a_1, \ldots, a_n, 0) \neq x(a_1, \ldots, a_n, 1)$ in $A(a_1, \ldots, a_n)$ and let $\varepsilon_{n+1} = \min \left\{\frac{1}{2(n+1)}, \frac{1}{3} \varrho(x(a_1, \ldots, a_n, 0), x(a_1, \ldots, a_n, 1))\right\}$. Define $A(a_1, \ldots, a_n, j) = \{x \in A(a_1, \ldots, a

borhood of $y$ and $y$ is a condensation point of $A$, so $V \cap A$ is uncountable. It follows that $V \cap P = \varnothing$, so that $x$ is not a limit point of $P$. Therefore $P$ contains all of its limit points, i.e., $P$ is closed. We conclude that $P$ is perfect.

(6.67) Remark. In view of (6.21) and (6.23), every Euclidean space satisfies the hypothesis of (6.66).

We now make a brief study of continuity.
