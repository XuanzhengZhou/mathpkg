---
role: proof
locale: en
of_concept: abstract-curve-functor-is-faithful
source_book: gtm052
source_chapter: "I"
source_section: "6"
---

**Proof.** Let $K$ be the function field of $Y$. Then each local ring $\mathcal{O}_P$ of a point $P \in Y$ is a discrete valuation ring of $K/k$, by (5.1) and (6.2A). Furthermore, by (6.4), distinct points give rise to distinct subrings of $K$. So let $U \subseteq C_K$ be the set of local rings of $Y$, and let $\varphi: Y \to U$ be the bijective map defined by $\varphi(P) = \mathcal{O}_P$.

First, we need to show that $U$ is an open subset of $C_K$. Because open sets are complements of finite sets, it is sufficient to show that $U$ contains a nonempty open set. Thus, by (4.3), we may assume $Y$ is affine, with affine coordinate ring $A$. Then $A$ is a finitely generated $k$-algebra, and by (3.2), $K$ is the quotient field of $A$, and $U$ is the set of localizations of $A$ at its maximal ideals. Since these local rings are all discrete valuation rings, $U$ consists in fact of all discrete valuation rings of $K/k$ containing $A$.

Now let $x_1, \ldots, x_n$ be a set of generators of $A$ over $k$. Then $A \subseteq R_P$ if and only if $x_1, \ldots, x_n \in R_P$. Thus $U = \bigcap U_i$, where $U_i = \{P \in C_K \mid x_i \in R_P\}$. But by (6.5), $\{P \in C_K \mid x_i \notin R_P\}$ is a finite set. Therefore each $U_i$ and hence also $U$ is open.

So we have shown that the $U$ defined above is an abstract nonsingular curve. To show that $\varphi$ is an isomorphism, we need only check that the regular functions on any open set are the same. But this follows from the definition of the regular functions on $U$ and the fact that for any open set $V \subseteq Y$, $\mathcal{O}(V) = \bigcap_{P \in V} \mathcal{O}_P$.
