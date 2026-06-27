---
role: proof
locale: en
of_concept: bose-integer-exists-d12
source_book: gtm054
source_chapter: "9"
source_section: "IXE"
---

Let $\Lambda$ be a finite projective plane of order $n$. Let

$$L_\infty = \{x_0, x_1, \ldots, x_{n-1}, x_\infty\}$$

be a line of $\Lambda$. Let $R_1, \ldots, R_n$ denote the remaining $n$ lines of $\Lambda$ through $x_0$, and let $C_1, \ldots, C_n$ denote the remaining $n$ lines through $x_\infty$. Let $x_{ij}$ be the unique point on $R_i \cap C_j$, by virtue of D3b. By D3a, the set

$$\{x_{ij} : i, j \in \{1, 2,

With each point $x_i$ on $L_\infty$ other than $x_0$ and $x_\infty$ we associate a Latin square $S_h \in \mathbb{L}_n$ as follows. Label the remaining $n$ lines through $x_h$ (other than $L_\infty$) by $L_{h1}, \ldots, L_{hn}$. Denoting the $ij$th entry of $S_h$ by $a_{ij}^h$, we define $a_{ij}^h = q$ if $x_{ij} \in L_{hq}$. Since $L_{hq}$ intersects each $R_i$ and each $C_j$ exactly once, the entry $q$ occurs exactly once in each row and each column of $S_h$. Thus $S_h$ is a Latin square for $h = 1, \ldots, n - 1$.

To see that $\{S_h : h = 1, \ldots, n - 1\}$ is an orthogonal set, observe that $(a_{ij}^h, a_{ij}^k) = (p, q)$ if and only if $x_{ij}$ is the point of intersection of $L_{hp}$ and $L_{kq}$.

Conversely, starting with a set of $n^2 + n + 1$ points and $2n + 1$ lines as in Figure D13 and a complete orthogonal set $\{S_1, \ldots, S_{n-1}\}$ of Latin squares from $\mathbb{L}_n$, we reverse the above construction, using $S_h$ to define the remaining $n$ lines through $x_h$ for each $h = 1, \ldots, n - 1$. The details are left to the reader.

IXE Partially-Balanced Incomplete Block Designs

The object of study in this section is a class of tactical configurations (non-degenerate (1; 1)-designs). This class will be defined by imposing some additional structure, but in general not enough structure, to bring the design-type to anything above (1; 1).

Let $\lambda_1 > \lambda_2 > \ldots > \lambda_m \geq 0$ be integers. For each $i = 1, \ldots, m$

where $x$ is some fixed element of $V$. Subtracting $\lambda_0$ from each side yields

$$\sum_{i=1}^{m} \lambda_i n_i = \sum_{y \in V + \{x\}} \bar{s}(\{x, y\}),$$

and by the definition of $\bar{s}$ we obtain

$$\sum_{i=1}^{m} \lambda_i n_i = \sum_{T \in \mathcal{P}(V)} s(T) \sum_{y \in V + \{x\}} [\{x, y\}, T]$$

$$= \sum_{x \in T \in \mathcal{P}(V)} s(T)(|T| - 1).$$

Since $\Lambda$ has blocksize $k$ and replication number $r$, this becomes

$$\sum_{i=1}^{m} \lambda_i n_i = r(k - 1),$$

the analog for PBIB-designs of C8.

An example of a 2-class PBIB-design is any $\rho$-valent graph which is not complete. Two vertices are first associates if they are incident and second associates otherwise. The parameters are as follows: $v = \nu_0, b = \nu_1, r = \rho, k = 2, \lambda_1 = 1, n_1 = \rho, \lambda_2 = 0,$ and $n_2 = \nu_0 - \rho - 1.$

The cube (Figure IIIF21) provides an example of a 3-class PBIB-design. Let $V$ be the set of the eight vertices of the cube; the blocks are the 4-sets of vertices which lie on a common face. Two vertices will be first associates if they are the end-points of an edge. They will be second associates if they lie on a common face but not on a common edge. Otherwise they are third associates. We have $v = 8, b = 6, r = 3, k = 4, \lambda_1 = 2, n_1 = 3, \lambda_2 = 1, n_2 = 3, \lambda_3 = 0,$ and $n_3 = 1.$ Observe that in this example two
