---
role: proof
locale: en
of_concept: residual-set-dense-positive-semiorbit
source_book: gtm002
source_chapter: "18"
source_section: "18"
---
Let $\{U_i\}$ be a countable base for $X$. For each $j = 1, 2, \ldots$, define
$$G_j = \bigcup_{n=0}^{\infty} T^{-n} U_j.$$
Set $E = \bigcap_{j=1}^{\infty} G_j$. Then $x \in E$ if and only if the positive semiorbit of $x$ meets every $U_j$, which is equivalent to the positive semiorbit of $x$ being dense in $X$.

We claim each $G_j$ is a dense open set. Openness is clear, since each $T^{-n} U_j$ is open and $G_j$ is a union of open sets. To show density, fix any two positive integers $i$ and $j$. Let $x_0$ be a point whose full orbit is dense. Since the orbit of $x_0$ is dense, it meets every nonempty open set infinitely often. In particular, there exist integers $n \geq 0$ and $m > n$ such that $x \in T^n U_j \cap U_i$ for some $x$. (Or the symmetric situation with $U_i$ and $U_j$ swapped.) In either case, $U_i \cap G_j \neq \emptyset$. Since $i$ was arbitrary, $G_j$ intersects every basic open set, hence $G_j$ is dense.

Therefore each $G_j$ is a dense open set and $E = \bigcap_j G_j$ is a countable intersection of dense open sets, i.e., a residual set in $X$. Hence the set of points with dense positive semiorbit is residual.
