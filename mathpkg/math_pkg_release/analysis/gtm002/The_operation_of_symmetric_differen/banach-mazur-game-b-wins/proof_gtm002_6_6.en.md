---
role: proof
locale: en
of_concept: banach-mazur-game-b-wins
source_book: gtm002
source_chapter: "6"
source_section: "6. The Banach-Mazur Game"
---
Let $f_1, f_2, \ldots$ be a winning strategy for $(B)$. Let $I^0$ denote the interior of any interval $I$. Given $f_1$, it is possible to define a sequence of closed intervals $J_i$ ($i = 1, 2, \ldots$) contained in $I^0$ such that (i) the intervals $K_i = f_1(I_0, J_i)$ are disjoint, and (ii) the union of their interiors is dense in $I^0$. One way to do this is as follows. Let $S$ be a sequence consisting of all closed intervals that have rational endpoints and are contained in $I^0$. Let $J_1$ be the first term of $S$. Having defined $J_1, \ldots, J_i$, let $J_{i+1}$ be the first term of $S$ contained in $I_0 - K_1 - K_2 - \cdots - K_i$. It is easy to verify, using the fact that $f_1(I_0, I_1) \subset I_1^0$, that this construction defines inductively a sequence $J_i$ having the required properties.

Similarly, for each $i$, let $J_{ij}$ ($j = 1, 2, \ldots$) be a sequence of closed intervals contained in $K_i^0$ such that the intervals $K_{ij} = f_2(I_0, J_i, K_i, J_{ij})$ are disjoint and the union of their interiors is dense in $K_i$. Then the union of all the intervals $K_{ij}^0$ is dense in $I^0$.

Proceeding inductively, we can define two families of intervals $J_{i_1\ldots i_{2n-1}}$ and $K_{i_1\ldots i_{2n}}$ indexed by finite sequences of positive integers, with the property that for each $n$, the union of the interiors of the intervals $K_{i_1\ldots i_{2n}}$ is dense in $I^0$.

For each infinite sequence $i_1, i_2, \ldots$, the nested sequence of intervals
$$I_0, J_{i_1}, K_{i_1}, J_{i_1 i_2}, K_{i_1 i_2}, \ldots$$
is a play consistent with the strategy $f_1, f_2, \ldots$, and therefore its intersection is contained in $B$. Define $G_n$ to be the union of the interiors of all intervals $K_{i_1\ldots i_{2n}}$. Then each $G_n$ is open and dense in $I_0$, and $\bigcap G_n \subset B$. Hence $A = I_0 - B \subset \bigcup (I_0 - G_n)$.

Since each of the sets $I_0 - G_n$ is nowhere dense, $A$ must be of first category.

Conversely, if $A$ is of first category, write $A = \bigcup A_n$ with each $A_n$ nowhere dense. Then $(B)$ can simply choose $I_{2n} \subset I_{2n-1} - A_n$ for each $n$, ensuring $\bigcap I_n \subset B$ regardless of how $(A)$ plays.
