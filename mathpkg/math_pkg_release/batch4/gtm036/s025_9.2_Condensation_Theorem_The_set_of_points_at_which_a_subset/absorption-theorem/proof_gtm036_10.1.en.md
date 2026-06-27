---
role: proof
locale: en
of_concept: absorption-theorem
source_book: gtm036
source_chapter: "10"
source_section: "10.1"
---

By the hypotheses, there is some positive integer $N$ such that $\bigcap \{nA \cap B : n \geq N\}$ is somewhere dense in $B$. Consequently there is a point $y$ of $B$ and a neighborhood $U$ of $0$ in $E$ such that $nA = (nA)^{-} \supset (U + y) \cap B$ for $n \geq N$.

Since $B$ is bounded, so is $B - B$; thus there is a real number $b$, $0 < b < 1$, such that $U \supset b(B - B)$ and hence $nA \supset (y + b(B - B)) \cap B$ for $n \geq N$. The set $y(1 - b) + bB$ is contained in $y + b(B - B)$ and, since $B$ is convex, it is also contained in $B$; therefore, $nA \supset y(1 - b) + bB$ for $n \geq N$.

The set $A$ absorbs each point of $-B$, and consequently there is an integer $m$, which may be supposed to be larger than $N$, such that $-y(1 - b) \in rA$ for $r \geq m$. Then
$$rA \supset \frac{1}{2}[y(1 - b) + bB] + \frac{1}{2}[-y(1 - b)] = \frac{1}{2}bB,$$
and $(2r/b)A \supset B$ for all $r \geq m$.
