---
role: proof
locale: en
of_concept: banach-mazur-game-b-winning-strategy
source_book: gtm002
source_chapter: "6"
source_section: "The Banach-Mazur Game"
---

**Proof.** If $A = \bigcup_{n=1}^{\infty} A_n$ with each $A_n$ nowhere dense, then player $(B)$ has the following simple winning strategy: at his $n$-th move, choose $I_{2n} \subset I_{2n-1} - A_n$. This is possible because $A_n$ is nowhere dense. Then $\bigcap I_n \subset I_0 - A = B$, so $(B)$ wins.

Conversely, suppose $(B)$ has a winning strategy $f_1, f_2, \ldots$. Let $I^0$ denote the interior of an interval $I$. Define a sequence of closed intervals $J_i \subset I^0$ such that (i) the intervals $K_i = f_1(I_0, J_i)$ are disjoint, and (ii) the union of their interiors is dense in $I^0$. This can be done by taking an enumeration $S$ of all closed intervals with rational endpoints contained in $I^0$, and inductively choosing $J_{i+1}$ as the first term of $S$ contained in $I_0 - \bigcup_{j=1}^{i} K_j$.

Similarly, for each $i$, choose $J_{ij} \subset K_i^0$ such that $K_{ij} = f_2(I_0, J_i, K_i, J_{ij})$ are disjoint with dense union of interiors in $K_i$.

Proceeding inductively, for each set of indices $i_1, \ldots, i_n$, define intervals $I(i_1), I(i_1, i_2), \ldots, I(i_1, \ldots, i_n)$ corresponding to the moves. Define
$$G_n = \bigcup_{i_1, \ldots, i_n} (I(i_1, \ldots, i_n))^0.$$
Then $G_n$ is a dense open set and $A \subset I_0 - \bigcap G_n$. Hence $A$ is of first category. $\square$
