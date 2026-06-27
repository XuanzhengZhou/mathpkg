---
role: proof
locale: en
of_concept: every-two-cantor-sets-are-homeomorphic
source_book: gtm047
source_chapter: "12"
source_section: "17"
---

Let the sets be $C$ and $C'$. By Theorem 4, $C$ is the union of a collection $G_1 = \{g_{1,1}, \ldots, g_{1,k_1}\}$ of disjoint open-and-closed sets of diameter less than $1$, and similarly $C'$ is the union of a collection $G'_1 = \{g'_{1,1}, \ldots, g'_{1,k'_1}\}$ of disjoint open-and-closed sets of diameter less than $1$. We may arrange that $k_1 = k'_1$. Define $f_1$ to be a bijection $G_1 \leftrightarrow G'_1$. Then refine $G_1$ to $G_2$, a collection of disjoint open-and-closed sets of diameter less than $1/2$, and similarly refine $G'_1$ to $G'_2$, matching the refinements so that the inclusion conditions of Theorem 7 hold. Continuing inductively, we obtain sequences $G_1, G_2, \ldots$ and $G'_1, G'_2, \ldots$ of finite open coverings of $C$ and $C'$ respectively, with $\|G_i\| \to 0$ and $\|G'_i\| \to 0$, and bijections $f_i: G_i \to G'_i$ satisfying the compatibility and intersection conditions of the preceding theorem. Thus all the conditions of the preceding theorem are satisfied, and the resulting $f$ is a homeomorphism $C \leftrightarrow C'$.
