---
role: proof
locale: en
of_concept: ramsey-finite-partition-theorem
source_book: gtm054
source_chapter: "VIII"
source_section: "B"
---

Denote $\{1, 2, \ldots, k + 1\}$ by $V$ and let $\mathcal{Q} \in \mathbb{P}_m(\{1, 2, \ldots, k\})$. Define $f: \mathcal{P}_2(V) \to \{1, \ldots, k\}$ by $f(\{a, b\}) = |a - b|$. Since $f$ is clearly surjective, there exists $\mathcal{R} \in \mathbb{P}_m(\mathcal{P}_2(V))$ whose cells are $f^{-1}[Q]$, $Q \in \mathcal{Q}$. Since $k + 1 \geq n(q_1, \ldots, q_m: 2)$ where $q_1 = \cdots = q_m = 3$, there exists a cell $Q \in \mathcal{R}$ and a subset $\{a, b, c\} \in \mathcal{P}_3(V)$ such that $\{a, b\}, \{a, c\}, \{b, c\} \in Q$. Assuming without loss of generality that $a < b < c$, we have $b - a, c - b, c - a \in f[Q]$. But $f[Q]$ is one of the original partition cells, and $(b - a) + (c - b) = c - a$, yielding $x = b-a$, $y = c-b$ with $x, y, x+y$ all in the same partition cell.
