---
role: proof
locale: en
of_concept: dense-positive-semiorbit-residual
source_book: gtm002
source_chapter: "18"
source_section: "Transitive Transformations"
---

Let $\{U_j\}$ be a countable base for $X$. For each $j$, define

$$G_j = \bigcup_{n=0}^{\infty} T^{-n} U_j,$$

and set

$$E = \bigcap_{j=1}^{\infty} G_j.$$

If $x \in E$, then for each $j$ there exists $n \geq 0$ such that $T^n x \in U_j$. Since $\{U_j\}$ is a base, this means the positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersects every non-empty open set, i.e., it is dense in $X$. Conversely, if the positive semiorbit of $x$ is dense, then $x \in E$ by definition.

We now show each $G_j$ is dense and open in $X$. Openness is immediate since $G_j$ is a union of open sets (each $T^{-n}U_j$ is open by continuity of $T$). For density, fix $i$ and $j$. Since $T$ is transitive, there exists a point $x_0$ with dense orbit. For any two positive integers $i$ and $j$, either $T^n U_i \cap U_j \neq \emptyset$ or $T^n U_j \cap U_i \neq \emptyset$ for some integer $n \geq 0$. In the latter case, both a point $x$ and some iterate $T^m x$ (with $m > n$) belong to $T^n U_j \cap U_i$, because every non-empty open set contains infinitely many points of any dense orbit. In either case, $U_i \cap G_j \neq \emptyset$. Since this holds for every basic open set $U_i$, $G_j$ is dense in $X$.

Thus each $G_j$ is a dense open set, and $E = \bigcap_{j=1}^{\infty} G_j$ is a countable intersection of dense open sets. Since $X$ is a complete metric space, the Baire category theorem implies $E$ is residual in $X$.
