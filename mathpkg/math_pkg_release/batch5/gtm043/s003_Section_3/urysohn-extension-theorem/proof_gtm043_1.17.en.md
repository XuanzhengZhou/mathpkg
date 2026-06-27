---
role: proof
locale: en
of_concept: urysohn-extension-theorem
source_book: gtm043
source_chapter: "1"
source_section: "1.17"
---

**Necessity.** If $A$ and $B$ are completely separated sets in $S$, there exists a function $f$ in $C^*(S)$ that is equal to $0$ on $A$ and $1$ on $B$. By hypothesis, $f$ has an extension to a function $g$ in $C^*(X)$. Since $g$ is $0$ on $A$ and $1$ on $B$, these sets are completely separated in $X$.

**Sufficiency.** Let $f_1$ be a given function in $C^*(S)$. Then $|f_1| \leq m$ for some $m \in \mathbf{N}$. One constructs by induction a sequence of functions $g_n \in C^*(X)$ and $f_n \in C^*(S)$ such that $|g_n| \leq \frac{2}{3} m \left(\frac{2}{3}\right)^{n-1}$, the sets $\{x \in S : f_n(x) \leq -m(\frac{2}{3})^{n}\}$ and $\{x \in S : f_n(x) \geq m(\frac{2}{3})^{n}\}$ are completely separated in $X$, and $g_n$ extends $f_n$ on the region where $f_n$ is small, with the remaining function $f_{n+1} = f_n - g_n|S$ satisfying the induction hypothesis.

Because the series $\sum g_n$ converges uniformly, $g(x) = \sum_{n \in \mathbb{N}} g_n(x)$ defines a continuous function on $X$. Moreover,
$$(g_1 + \cdots + g_n) | S = (f_1 - f_2) + \cdots + (f_n - f_{n+1}) = f_1 - f_{n+1}.$$
Since the sequence $f_{n+1}(s)$ approaches $0$ at every point $s$ of $S$, we have $g(s) = f_1(s)$. Thus $g$ is an extension of $f_1$ to $X$.
