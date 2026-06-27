---
role: proof
locale: en
of_concept: topologies-for-subspaces-and-quotients
source_book: gtm036
source_chapter: "16"
source_section: "16.11"
---

The family of polars in $H$ of finite subsets $\{f_1 + H^\circ, \cdots, f_n + H^\circ\}$ of $F/H^\circ$ is a local base for the topology $w(H, F/H^\circ)$. But the polar in $H$ of such a subset is simply the set $\{x: x \in H \text{ and } |\langle x, f_i \rangle| \leq 1 \text{ for } i = 1, \cdots, n\}$, and this is the intersection with $H$ of the polar of $\{f_1, \cdots, f_n\}$ in $E$. It follows that $w(H, F/H^\circ)$ is the relativization of $w(E,F)$, establishing (i).

To establish (ii), observe that the quotient topology for $E/H$ has a local base consisting of all collections of the form $\{x + H: x \in X_0\}$, where $X$ is a finite subset of $F$ and $X_0$ is the polar of $X$ in $E$. On the other hand, the topology $w(E/H, H^\circ)$ has a local base consisting of collections $\{y + H: y \in Y_0\}$ where $Y$ is a finite subset of $H^\circ$. Clearly the latter topology is weaker than the quotient topology. Conversely, every finite subset of $H^\circ$ is a finite subset of $F$, so every $w(E/H, H^\circ)$-basic neighborhood is also a basic neighborhood for the quotient topology. Hence the two topologies coincide.
