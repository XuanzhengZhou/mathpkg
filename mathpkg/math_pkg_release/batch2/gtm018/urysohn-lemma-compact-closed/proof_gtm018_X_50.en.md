---
role: proof
locale: en
of_concept: urysohn-lemma-compact-closed
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

Since $X$ is completely regular, corresponding to each point $y$ in $C$ there exists a function $f_y$ in $\mathfrak{F}$ such that $f_y(y) = 0$ and $f_y(x) = 1$ for $x$ in $F$. The class of open sets $\{x: f_y(x) < \frac{1}{2}\}$ is an open covering of $C$, and since $C$ is compact, there exists a finite subset $\{y_1, \cdots, y_n\}$ of $C$ such that $C \subset \bigcup_{i=1}^{n} \{x: f_{y_i}(x) < \frac{1}{2}\}$. If we write $g(x) = \prod_{i=1}^{n} f_{y_i}(x)$, then $g \in \mathfrak{F}$; since $0 \leq f_y(x) \leq 1$ for all $x$ and all $y$, it follows that $g(x) < \frac{1}{2}$ for $x$ in $C$ and $g(x) = 1$ for $x$ in $F$. If $f = (2g - 1) \cup 0$, then $f \in \mathfrak{F}$, $f(x) = 0$ for $x$ in $C$, and $f(x) = 1$ for $x$ in $F$.
