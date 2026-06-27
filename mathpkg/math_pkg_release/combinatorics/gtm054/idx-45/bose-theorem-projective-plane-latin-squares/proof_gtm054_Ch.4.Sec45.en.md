---
role: proof
locale: en
of_concept: bose-theorem-projective-plane-latin-squares
source_book: gtm054
source_chapter: "IV"
source_section: "45"
---

**Proof.**

Let $\Lambda$ be a finite projective plane of order $n$. Let

$$L_\infty = \{x_0, x_1, \ldots, x_{n-1}, x_\infty\}$$

be a line of $\Lambda$. Let $R_1, \ldots, R_n$ denote the remaining $n$ lines of $\Lambda$ through $x_0$, and let $C_1, \ldots, C_n$ denote the remaining $n$ lines through $x_\infty$. Let $x_{ij}$ be the unique point on $R_i \cap C_j$, by virtue of D3b. By D3a, the set

$$\{x_{ij} : i, j \in \{1, 2, \ldots, n\}\}$$

comprises all $n^2$ points of $\Lambda$ not on $L_\infty$.

With each point $x_h$ on $L_\infty$ other than $x_0$ and $x_\infty$ (so $h = 1, \ldots, n-1$) we associate a Latin square $S_h \in \mathbb{L}_n$ as follows. Label the remaining $n$ lines through $x_h$ (other than $L_\infty$) by $L_{h1}, \ldots, L_{hn}$. Denoting the $ij$th entry of $S_h$ by $a_{ij}^h$, we define $a_{ij}^h = q$ if $x_{ij} \in L_{hq}$. Since $L_{hq}$ intersects each $R_i$ and each $C_j$ exactly once, the entry $q$ occurs exactly once in each row and each column of $S_h$. Thus $S_h$ is a Latin square for $h = 1, \ldots, n - 1$.

To see that $\{S_h : h = 1, \ldots, n - 1\}$ is an orthogonal set, observe that $(a_{ij}^h, a_{ij}^k) = (p, q)$ if and only if $x_{ij}$ is the point of intersection of $L_{hp}$ and $L_{kq}$. Since two distinct lines $L_{hp}$ and $L_{kq}$ (with $h \neq k$) intersect in exactly one point (by D3b), each ordered pair $(p, q)$ occurs exactly once among the superimposed entries of $S_h$ and $S_k$. Hence $S_h$ and $S_k$ are orthogonal. This holds for all $h \neq k$, giving a complete orthogonal set of size $n-1$.

Conversely, starting with a set of $n^2 + n + 1$ points and $2n + 1$ lines as in Figure D13 and a complete orthogonal set $\{S_1, \ldots, S_{n-1}\}$ of Latin squares from $\mathbb{L}_n$, we reverse the above construction, using $S_h$ to define the remaining $n$ lines through $x_h$ for each $h = 1, \ldots, n - 1$. The details are left to the reader.
