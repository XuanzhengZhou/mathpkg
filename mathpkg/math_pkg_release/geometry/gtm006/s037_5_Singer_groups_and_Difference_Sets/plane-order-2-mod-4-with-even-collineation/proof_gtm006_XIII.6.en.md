---
role: proof
locale: en
of_concept: plane-order-2-mod-4-with-even-collineation
source_book: gtm006
source_chapter: "XIII"
source_section: "6"
---

*Proof.* If there is a collineation of even order, then there exists one of order two; let it be $\alpha$. Since $n \equiv 2 \pmod{4}$, $n$ cannot be a square, so $\alpha$ is not a Baer collineation. Since $n$ is even, $\alpha$ must be an elation (see Exercise 4.4).

Let $k$ be the axis of $\alpha$ and let $Q \in k$ be its centre. Denote the $n$ other lines on $Q$ by $m_i$ ($i = 1, 2, \ldots, n$), and the $n$ other points on $k$ by $P_i$ ($i = 1, 2, \ldots, n$). The points (other than $Q$) on a line $m_i$ fall into $n/2$ orbits of length $2$ under $\alpha$; represent them by $X_{i1}, X_{i1}^\alpha, X_{i2}, X_{i2}^\alpha, \ldots, X_{it}, X_{it}^\alpha$ where $t = n/2$. Similarly, the $n$ lines other than $k$ through $P_i$ can be represented by $w_{i1}, w_{i1}^\alpha, \ldots, w_{it}, w_{it}^\alpha$.

Construct a square matrix $M$ of order $nt$ as follows: the rows are indexed by pairs $(i, j)$ with $i = 1, \ldots, n$ and $j = 1, \ldots, t$, and the columns by $(u, v)$ similarly. The entry $M_{(i,j),(u,v)}$ is $+1$ if $X_{ij}$ lies on $w_{uv}$, and $-1$ otherwise. From the incidence properties one establishes

$$M M' = n I. \tag{1}$$

Now perform a block-sum operation on $M$ to obtain a new matrix $B$ with $n$ rows and $nt$ columns: add all rows of each block (corresponding to each $i$) to form a single row. Since no two rows of the same block have a non-zero entry in the same column but every line $w_{uv}$ must meet $m_i$ in one orbit, each entry of $B$ is $\pm 1$. The resulting $n \times nt$ matrix $B$ satisfies

$$B B' = n t I. \tag{2}$$

All entries of $B$ are $\pm 1$, and $t = n/2$. By multiplying columns by $-1$ and permuting columns (which preserve (2)), we may assume the first row consists of all $+1$'s, and the second row has $nt/2$ entries $+1$ followed by $nt/2$ entries $-1$.

Now suppose $n > 2$, so $B$ has at least three rows. Arrange the first three rows as:

$$\begin{array}{cc|cc}
+1 & & -1 & \\
\hline
z & nt/2 - z & y & nt/2 - y
\end{array}$$

Taking inner products between the first and third rows gives $2z + 2y - nt = 0$, hence $z + y = nt/2$. Taking inner products between the second and third rows gives $z - (nt/2 - z) - y + (nt/2 - y) = 0$, i.e., $2z - 2y = 0$, so $z = y = nt/4$.

Thus $nt/4 = n^2/8$ must be an integer, which forces $n$ to be divisible by $4$. But $n \equiv 2 \pmod{4}$, a contradiction. Therefore $n \leq 2$, and since a projective plane of order $2$ exists (the Fano plane), we conclude $n = 2$. $\square$
