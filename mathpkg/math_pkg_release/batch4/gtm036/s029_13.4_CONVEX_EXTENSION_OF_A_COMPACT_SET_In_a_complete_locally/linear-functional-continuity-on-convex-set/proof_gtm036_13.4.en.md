---
role: proof
locale: en
of_concept: linear-functional-continuity-on-convex-set
source_book: gtm036
source_chapter: "13"
source_section: "13.4"
---

\textbf{(i)} The necessity of the condition is obvious. For the sufficiency, it is enough to prove that a set of the form $\{x: f(x) \leq a\} \cap A$ or $\{x: f(x) \geq a\} \cap A$ is closed in $A$. Put $B = \{x: f(x) \leq a\} \cap A$ and let $y$ be a point in $A \setminus B$. Then $f(y) > a$ and there is a circled neighborhood $U$ of $0$ such that $(y + U) \cap f^{-1}[a] \cap A$ is empty. Then $(y + U) \cap B$ is also empty since, if $x \in y + U$, then $[x: y] \subset y + U$. Hence $B$ is closed in $A$. Similarly, a set of the form $\{x: f(x) \geq a\} \cap A$ is closed in $A$.

\textbf{(ii)} Let $a$ be a real number for which $f^{-1}[a] \cap A$ is not empty. Then there is $y$ in $A$ such that $f(y) = -a$. Consider the map $h$ on $A$ into $A$ defined by $h(x) = (x + y)/2$. The map $h$ is continuous and the set $f^{-1}[a] \cap A$ is the inverse image of $f^{-1}[0] \cap A$ under $h$. Assertion (ii) now follows in view of (i).

\textbf{(iii)} Assume that $f^{-1}[0] \cap A$ is closed in $A$. Let $r$ be the real part of $f$, and let $B$ be the convex symmetric subset $\{x: f(x) \text{ is real}\}$ of $E$. Then $f^{-1}[0] \cap A \cap B = r^{-1}[0] \cap A \cap B$. Hence by (ii) [the reasoning extends to show $r^{-1}[0] \cap A \cap B$ is closed in $A$].

\textbf{(iv)} This is a consequence of the equation $g(x) - g(y) = 2g((x - y)/2)$ and the fact that $(x - y)/2$ belongs to $A$ whenever $x$ and $y$ belong to $A$.
