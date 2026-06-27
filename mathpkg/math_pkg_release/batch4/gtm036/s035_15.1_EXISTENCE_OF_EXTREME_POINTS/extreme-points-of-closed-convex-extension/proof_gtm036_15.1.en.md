---
role: proof
locale: en
of_concept: extreme-points-of-closed-convex-extension
source_book: gtm036
source_chapter: "15"
source_section: "15.1"
---
Let $U$ be a convex circled closed neighborhood of $0$ in $E$. Then, since $A$ is compact, there exists a finite number of points $x_1, \cdots, x_n$ in $A$ such that $\bigcup \{(U + x_i): i = 1, \cdots, n\} \supset A$. Let $A_i = A \cap (U + x_i)$; then $\langle A \rangle^-$ is contained in the convex extension of $\bigcup \{\langle A_i \rangle^-: i = 1, \cdots, n\}$, since the latter is closed by theorem 13.1. Then each point $y$ of $\langle A \rangle^-$ can be expressed as

$$y = \sum \{a_i y_i: i = 1, \cdots, n\},$$

where the $a_i$'s are non-negative real numbers such that $\sum \{a_i: i = 1, \cdots, n\} = 1$, and $y_i \in \langle A_i \rangle^- \subset U + x_i$.

If $y$ is an extreme point of $\langle A \rangle^-$, then for some $i$, $y = y_i$. Therefore,

$$y \in U + x_i \subset A + U.$$

Since $U$ is an arbitrary convex circled closed neighborhood of $0$ and $A$ is closed, it follows that $y \in A$.
