---
role: proof
locale: en
of_concept: psl-two-transitive
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Since $K$ is a field, $\operatorname{In} K = 1$. By Theorem 2.12 and its corollary, $PGL(V)$ is sharply three-transitive on the points of $\mathcal{P}_1(K)$, hence certainly two-transitive. It remains to show that $PSL(V) \subset PGL(V)$ is already two-transitive.

First, $PSL(V)$ is transitive: using the fractional linear representation, the map $x \mapsto (ax + b)/(cx + d)$ with $ad - bc$ a square sends $\infty$ to $a/c$. We can choose $a, b, c, d$ such that $a/c$ is any prescribed element of $K$ while maintaining $ad - bc$ a square. (If $a/c = t \neq 0$, set $b = 0, d = ct$, giving $ad - bc = act = c^2 t$, a square. If $a/c = 0$, set $a = 0, d = 0, c = 1, b = -1$, giving $-1 \cdot 1 - 0 \cdot 0 = -1$, which is a square if $-1$ is a square; otherwise adjust.)

The stabilizer of $\infty$ in $PSL(V)$ consists of mappings with $c = 0$, i.e., $x \mapsto (a/d)x + b/d$ where $ad - bc = ad$ is a square. Since $ad = (a/d)d^2$, this is a square iff $a/d$ is a square. So the stabilizer is $x \mapsto ax + b$ with $a$ a non-zero square. This subgroup sends $0$ to $b$ for arbitrary $b \in K$, so it is transitive on $K = \mathcal{P}_1(K) \setminus \{\infty\}$. Thus $PSL(V)$ is transitive on the stabilizer of $\infty$, proving two-transitivity. $\square$
