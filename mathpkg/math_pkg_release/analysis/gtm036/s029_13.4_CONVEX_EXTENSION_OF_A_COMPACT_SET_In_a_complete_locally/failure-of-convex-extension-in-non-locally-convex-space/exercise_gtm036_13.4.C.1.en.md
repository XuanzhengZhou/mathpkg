---
role: exercise
locale: en
chapter: "13"
section: "13.4"
exercise_number: 1
---

\textbf{C. Convex Extension of Bounded and Totally Bounded Sets.}

In a linear topological space which is not locally convex, the convex extension of a bounded or totally bounded set may fail to have the same property.

In the space $l^{1/2}$ (6N), the set $\{x: \|x\|_{1/2} < 1\}$ is bounded but its convex extension is not bounded.

Let $x_{11} = (1,0,0,\dots)$, $x_{12} = (0,1/2,0,\dots)$, $x_{22} = (0,0,1/2,0,\dots)$, $x_{13} = (0,0,0,1/3,0,\dots)$ and in general let $x_{mn}$ with $1 \le m \le n$ be the sequence with all terms zero except the $(\frac{1}{2}n(n-1) + m)$-th, which is $1/n$. Then
$$A = \{x_{mn}: 1 \le m \le n,\; n = 1,2,\dots\}$$
is totally bounded, but $\langle A \rangle$, which contains all the points
$$y_n = \frac{1}{n}\sum\{x_{mn}: 1 \le m \le n\},$$
is not totally bounded.
