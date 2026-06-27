---
role: proof
locale: en
of_concept: equal-number-of-point-and-line-orbits
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Let $t_1$ be the number of point orbits of $\Pi$ and $t_2$ the number of line orbits. For any $\alpha \in \Pi$, let $\chi(\alpha)$ be the number of fixed points of $\alpha$. By Theorem 13.3, $\chi(\alpha)$ is also the number of lines fixed by $\alpha$.

Applying Burnside's Lemma (Result 1.14) to the permutation group $\Pi(P)$ on points and to $\Pi(l)$ on lines respectively, we obtain:
$$
|\Pi| t_1 = \sum_{\alpha \in \Pi} \chi(\alpha), \qquad |\Pi| t_2 = \sum_{\alpha \in \Pi} \chi(\alpha).
$$

Since the right-hand sides are identical, we have $|\Pi| t_1 = |\Pi| t_2$, and therefore $t_1 = t_2$. Thus $\Pi$ has equally many point and line orbits.
