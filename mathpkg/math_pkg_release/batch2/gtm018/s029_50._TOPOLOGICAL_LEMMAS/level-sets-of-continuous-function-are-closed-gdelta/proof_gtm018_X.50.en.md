---
role: proof
locale: en
of_concept: level-sets-of-continuous-function-are-closed-gdelta
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

For the forward direction, since $f$ is continuous, the sets $\{x: f(x) \geq c\}$ and $\{x: f(x) \leq c\}$ are closed. Moreover,

$$\{x: f(x) \geq c\} = \bigcap_{n=1}^{\infty} \{x: f(x) > c - \tfrac{1}{n}\},$$

$$\{x: f(x) \leq c\} = \bigcap_{n=1}^{\infty} \{x: f(x) < c + \tfrac{1}{n}\},$$

and each set in the intersections is open, so both are $G_\delta$. The set $\{x: f(x) = c\}$ is the intersection of the two, hence also a closed $G_\delta$.

For the converse, suppose $C$ is a compact $G_\delta$ and write $C = \bigcap_{n=1}^{\infty} U_n$ where each $U_n$ is open. By Theorem B, for each $n$ there exists a function $f_n$ in $\mathfrak{F}$ such that $f_n(x) = 0$ for $x$ in $C$ and $f_n(x) = 1$ for $x$ in $X - U_n$. Define

$$f(x) = \sum_{n=1}^{\infty} \frac{1}{2^n} f_n(x).$$

Then $f \in \mathfrak{F}$. For $x \in C$, each $f_n(x) = 0$ so $f(x) = 0$. For $x \notin C$, there exists some $n$ such that $x \in X - U_n$, hence $f_n(x) = 1$, so $f(x) \geq \frac{1}{2^n} > 0$. Therefore $C = \{x: f(x) = 0\}$.
