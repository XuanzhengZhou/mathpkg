---
role: proof
locale: en
of_concept: crossing-cycles-common-vertex
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

Let $Z_1, \ldots, Z_k$ be a planar imbedding in which $\Delta$ and $\Delta'$ cross at a vertex. We write $Z = \sum_{i=1}^{k} a_i Z_i$, where $Z$ is the cycle of $\Delta$. Each edge of $\Gamma$ is then of one of three types: an edge is of type $j$ ($j = 0, 1, 2$) if it belongs to exactly $j$ cycles $Z_i$ having coefficient $a_i = 1$. Clearly the edges of type $1$ are the edges in $Z$.

By Lemma E21 (concerning the cyclic ordering of edges at a vertex), if a vertex $x$ is not in $\Delta$, then the edges in $f^*(x)$ are either all of type $0$ or all of type $2$.

Now let $\Delta'$ be given by $x_0, e_1, x_1, \ldots, e_n, x_n = x_0$, and suppose $\Delta$ and $\Delta'$ cross at $x_0$. By Lemma E21 we may assume without loss of generality that $e_1$ is of type $0$ and $e_n$ is of type $2$ (since the edges incident with $x_0$ alternate between types as one traverses the cyclic order). Thus there is a first index $i > 1$ such that $e_i$ is not of type $0$. The vertex $x_{i-1} \neq x_0$ is then a vertex common to $\Delta$ and $\Delta'$.
