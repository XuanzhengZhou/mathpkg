---
role: proof
locale: en
of_concept: psl-two-transitive-on-points
source_book: gtm006
source_chapter: "2"
source_section: "5"
---

The linear transformation $\beta$ of the proof of Lemma 2.19 has the following matrix with respect to the basis $e_1, e_2, e_3$ of $V$:
$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{bmatrix}
$$

Since this has determinant one, $\beta$ is in $\operatorname{PSL}(V)$. Given any two lines of $\mathcal{P}(V)$, there is always a point on neither, so by Lemma 2.19, there is an element of $\operatorname{PSL}(V)$ which sends the first to the second. Hence $\operatorname{PSL}(V)$ is transitive on lines.

Now let $W$ be a line of $\mathcal{P}(V)$, and consider the group $\operatorname{PSL}(W)$, which by Theorem 2.15 is three-transitive on its one-dimensional subspaces.

Let $X$ and $Y$ be distinct points, and $U$ and $Z$ be another pair of distinct points. We must show that $\operatorname{PSL}(V)$ contains an element sending $X$ onto $U$ and $Y$ onto $Z$. Since $\operatorname{PSL}(V)$ is transitive on the lines of $\mathcal{P}(V)$, there is a mapping in $\operatorname{PSL}(V)$ which sends the line $X + Y$ onto the line $U + Z$. Under this mapping, $X$ and $Y$ go to points $X_1$ and $Y_1$, respectively, both of which are on $U + Z$. But now there is an element of $\operatorname{PSL}(U + Z) < \operatorname{PSL}(V)$ which sends $X_1$ to $U$ and $Y_1$ to $Z$, and so the product of the two automorphisms sends $X$ and $Y$ onto $U$ and $Z$, respectively. Thus $\operatorname{PSL}(V)$ is two-transitive on points.