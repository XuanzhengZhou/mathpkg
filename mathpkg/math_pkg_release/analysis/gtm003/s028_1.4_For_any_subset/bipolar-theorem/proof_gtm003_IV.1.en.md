---
role: proof
locale: en
of_concept: bipolar-theorem
source_book: gtm003
source_chapter: "IV"
source_section: "1.5"
---

It follows from (1.4) that $M^{\circ\circ}$ is $\sigma(F, G)$-closed, convex, and contains $0$; obviously it also contains $M$. Thus $M_1 \subset M^{\circ\circ}$ if $M_1$ is the closed, convex hull of $M \cup \{0\}$; the assertion will be proved when we show that $x \notin M_1$ implies $x \notin M^{\circ\circ}$.

Suppose that $x_0 \notin M_1$. By the second separation theorem (II, 9.2), there exists a closed real hyperplane separating $M_1$ and $\{x_0\}$ strictly. Since $0 \in M_1$, $H$ is of the form $H = \{ x \in F : f(x) = 1 \}$ for a suitable $\sigma(F, G)$-continuous real linear form $f$ on $F$. It follows from (1.2) and (I, 7.2) that $f(x) = \langle x, y \rangle$ for some $y \in G$. Since the hyperplane $H$ strictly separates $M_1$ and $\{x_0\}$, and $0 \in M_1$ with $f(0) = 0 < 1$, we have $\langle x, y \rangle \leq 1$ for all $x \in M_1$, while $\langle x_0, y \rangle > 1$. In particular, $\langle x, y \rangle \leq 1$ for all $x \in M$, whence $y \in M^\circ$. But $\langle x_0, y \rangle > 1$ implies $x_0 \notin M^{\circ\circ}$, which completes the proof.
