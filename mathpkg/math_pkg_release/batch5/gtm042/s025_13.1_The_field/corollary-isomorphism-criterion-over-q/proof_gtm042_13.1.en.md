---
role: proof
locale: en
of_concept: corollary-isomorphism-criterion-over-q
source_book: gtm042
source_chapter: "13"
source_section: "13.1"
---

The necessity is obvious. To see that the condition is sufficient, let $\chi$ and $\chi'$ be the characters of $V$ and $V'$. We have

$$\dim V^C = \langle \operatorname{Res}_C^G \chi, 1_C \rangle_C$$

and hence $\langle \operatorname{Res}_C^G (\chi - \chi'), 1_C \rangle_C = 0$ for each cyclic subgroup $C$. This means $\sum_{x \in C} (\chi(x) - \chi'(x)) = 0$ for every cyclic subgroup $C$. Since $\chi - \chi'$ is a $\mathbb{Q}$-valued class function, Theorem 30 implies $\chi - \chi' = 0$, hence $\chi = \chi'$. Thus $V$ and $V'$ are isomorphic.
