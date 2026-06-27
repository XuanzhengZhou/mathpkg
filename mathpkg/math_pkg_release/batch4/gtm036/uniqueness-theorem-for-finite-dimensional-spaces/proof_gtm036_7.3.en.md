---
role: proof
locale: en
of_concept: uniqueness-theorem-for-finite-dimensional-spaces
source_book: gtm036
source_chapter: "7"
source_section: "7.3"
---

Let $x_i, i = 1, \cdots, n$, be a (Hamel) base for $F$, and let $T$ be the linear transformation from the product of $n$ scalar fields $\times \{K: i = 1, \cdots, n\}$ onto $F$ defined by $T(a_1, a_2, \cdots, a_n) = \sum \{a_i x_i: i = 1, \cdots, n\}$. Then $T$ is clearly one-to-one, and since $E$ is a linear topological space, $T$ is continuous. It will be shown by induction on $n$ that $T^{-1}$ is continuous and that $T$ is consequently a topological isomorphism. If the dimension of $F$ is one, and $\{x_1\}$ is a base for $F$ (that is, $x_1 \neq 0$), then the function $T$, where $T(a) = ax_1$, is a continuous one-to-one map of the scalar field onto $F$. Since $T^{-1}$ is a linear functional with the closed null space $\{0\}$, it follows that $T^{-1}$ is continuous. If the dimension of $F$ is $n + 1$, then, by the induction hypothesis, every maximal linear subspace $H$ in $F$ is topologically isomorphic to a Euclidean space, is therefore complete and closed in $E$, and hence every linear functional on $H$ is continuous. In particular the functions $x \rightarrow a_i(x)$ are continuous; thus $T^{-1}$ is continuous.
