---
role: proof
locale: en
of_concept: lambda-mathcal-system-a14
source_book: gtm054
source_chapter: "10"
source_section: "XA"
---

Suppose that $\Lambda$ satisfies conditions (a) and (b), and let $w$ be any weight function. Since $U_1 \subseteq U_2 \subseteq V$ implies $w(U_1) \leq w(U_2)$, it is clear by (a) that the greedy algorithm will always terminate with a set in $\mathcal{B}$. Also, some heaviest set must belong to $\mathcal{B}$.

Suppose the greedy algorithm terminates with the set $B_0 = \{x_0, \ldots, x_k\}$, where $w(x_0) \geq \ldots \geq w(x_k)$. Let $B_1 = \{y_0, \ldots, y_k\}$ be any set in $\mathcal{B}$, and assume $w(y_0) \geq \ldots \geq w(y_k)$. We show that $w(x_i) \geq w(y_i)$ for $i = 0, \ldots, k$, and hence $w(B_0) \geq w

As an application of the greedy algorithm, the reader is referred to the "connector problem" or "minimum tree problem." (See Berge [b.5, p. 470].) In this case one seeks to link together various cities by a single (connected) communications network as cheaply as possible, where to each pair of cities some cost function assigns the cost of joining them. One procedure is to use a weight function which is the reciprocal of the cost function to construct a spanning forest (the cities being the vertices) whose edge set is a heaviest set. Alternatively (though less efficiently if the number of vertices exceeds 4) is to use the given cost function as a weight function to construct a heaviest spanning coforest—then throw it away and use what is left.

XB Matroids

In this section four types of set systems will be presented. It will become evident that they are very closely interrelated. The first three will turn out to be types of exchange systems. The fourth one generally is not, but it is this one that will be given the name of "matroid."

A set system $(V, \mathcal{A})$ is called an independence system if it satisfies conditions B1 and B2:
