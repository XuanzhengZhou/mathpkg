---
role: proof
locale: en
of_concept: dense-positive-semiorbit-is-residual
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $\{U_i\}$ be a countable base for $X$. For each $j = 1, 2, \ldots$, define

$$G_j = \bigcup_{n=0}^{\infty} T^{-n} U_j.$$

Then $G_j$ is open (as a union of open sets, since $T$ is a homeomorphism) and we claim each $G_j$ is dense. To see this, fix $i$ and $j$. Since $T$ is transitive, there exists a point $x_0$ whose orbit $\{T^n x_0 : n \in \mathbb{Z}\}$ is dense in $X$. For any two positive integers $i$ and $j$, the dense orbit intersects both $U_i$ and $U_j$ infinitely often. Hence there exist integers $m > n \geq 0$ such that $T^n x_0 \in U_i$ and $T^m x_0 \in U_j$. But then $T^m x_0 = T^{m-n}(T^n x_0) \in U_j$, so $T^n x_0 \in T^{-(m-n)} U_j \subseteq G_j$. Thus $T^n x_0 \in U_i \cap G_j$, showing $U_i \cap G_j \neq \emptyset$. Since $\{U_i\}$ is a base, this implies $G_j$ is dense.

Now define

$$E = \bigcap_{j=1}^{\infty} G_j.$$

Then $E$ is a countable intersection of dense open sets, hence residual in $X$ (by the Baire category theorem). For any $x \in E$, we have $x \in G_j$ for all $j$, so there exists $n \geq 0$ with $T^n x \in U_j$ for every $j$. Since $\{U_j\}$ is a base, the positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersects every nonempty open set, hence is dense in $X$. Therefore the set of points with dense positive semiorbit is residual.
