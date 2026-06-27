---
role: proof
locale: en
of_concept: c-star-embedding-equivalence-theorem
source_book: gtm043
source_chapter: "6"
source_section: "6.4"
---

**(3) implies (4).** If $p \in \operatorname{cl} Z_1 \cap \operatorname{cl} Z_2$, then for every zero-set-neighborhood $V$ (in $T$) of $p$, we have

$$p \in \operatorname{cl} (V \cap Z_1) \text{ and } p \in \operatorname{cl} (V \cap Z_2).$$

Hence (3) implies that $V \cap Z_1$ meets $V \cap Z_2$, i.e., $V$ meets $Z_1 \cap Z_2$. Therefore

$$p \in \operatorname{cl} (Z_1 \cap Z_2).$$

Thus, $\operatorname{cl} Z_1 \cap \operatorname{cl} Z_2 \subset \operatorname{cl} (Z_1 \cap Z_2)$. The reverse inclusion is trivial.

**(4) implies (5).** Since $X$ is dense in $T$, each point of $T$ is the limit of at least one $z$-ultrafilter. On the other hand, distinct $z$-ultrafilters contain disjoint zero-sets (Theorem 2.6(b)), and the hypothesis (in fact, its weaker form (3)) implies that a point $p$ cannot belong to the closures of both these zero-sets. Hence the two $z$-ultrafilters cannot both converge to $p$.

**(5) implies (1).** Given $p \in T$, let $\mathcal{A}$ denote the unique $z$-ultrafilter on $X$ with limit $p$. As in 4.12, we write

$$\tau^{\#} \mathcal{A} = \{E \in Z(Y) : \tau^{\leftarrow}[E] \in \mathcal{A}\}.$$

This is a $z$-filter on the compact space $Y$, and so it has a cluster point (Theorem 4.11). Moreover, since $\mathcal{A}$ is a prime $z$-filter, so is $\tau^{\#} \mathcal{A}$. Therefore, by Theorem 2.13, $\tau^{\#} \mathcal{A}$ has a unique cluster point; denote it by $\bar{\tau}(p)$. The mapping $\bar{\tau}$ is the required continuous extension.

The implications (1) $\implies$ (2) $\implies$ (3) are standard, completing the equivalence proof.
