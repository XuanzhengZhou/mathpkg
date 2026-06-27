---
role: proof
locale: en
of_concept: continuous-separation-of-compact-and-closed
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

Since $X$ is completely regular, corresponding to each point $y$ in $C$ there exists a function $f_y$ in $\mathfrak{F}$ such that $f_y(y) = 0$ and $f_y(x) = 1$ for $x$ in $F$. The family of open sets

$$\{x: f_y(x) < \tfrac{1}{2}\}, \quad y \in C,$$

is an open covering of $C$, and since $C$ is compact, there exists a finite subset $\{y_1, \dots, y_n\}$ of $C$ such that

$$C \subset \bigcup_{i=1}^{n} \{x: f_{y_i}(x) < \tfrac{1}{2}\}.$$

Define $g(x) = \prod_{i=1}^{n} f_{y_i}(x)$. Then $g \in \mathfrak{F}$. Since $0 \leq f_y(x) \leq 1$ for all $x$ in $X$ and all $y$ in $C$, it follows that $g(x) < \frac{1}{2}$ for $x$ in $C$ and $g(x) = 1$ for $x$ in $F$. Let $f = (2g - 1) \vee 0$, i.e., $f(x) = \max\{2g(x) - 1, 0\}$. Then $f \in \mathfrak{F}$, $f(x) = 0$ for $x$ in $C$, and $f(x) = 1$ for $x$ in $F$.
