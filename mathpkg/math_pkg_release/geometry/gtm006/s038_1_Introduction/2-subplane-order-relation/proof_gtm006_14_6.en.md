---
role: proof
locale: en
of_concept: 2-subplane-order-relation
source_book: gtm006
source_chapter: "XIV"
source_section: "6"
---
**Proof of Theorem 14.10.** Let $\Gamma$ be the 2-subgroup of $\Pi$ whose fixed elements are precisely the points and lines of $\mathcal{Q}$. If $\Gamma = 1$ then $\mathcal{Q} = \mathcal{P}$ and $n = m$ with $g = 0$.

If $\Gamma \neq 1$, then $|\Gamma| = 2^g$ for some $g \geq 1$. The number of points of $\mathcal{Q}$ is $m^2 + m + 1$, and the number of points of $\mathcal{P}$ is $n^2 + n + 1$. By orbit counting under the action of $\Gamma$, each point not in $\mathcal{Q}$ lies in an orbit of size at least $2$ (since only points of $\mathcal{Q}$ are fixed by all of $\Gamma$). More precisely, since $\Gamma$ is a 2-group, each orbit size is a power of $2$ dividing $2^g$.

The fixed-point set of $\Gamma$ is exactly $\mathcal{Q}$. Writing the total number of points as a sum of orbit sizes:
$$n^2 + n + 1 = (m^2 + m + 1) + \sum (\text{orbit sizes} \geq 2).$$

The orbit sizes being powers of $2$ forces $n^2 + n + 1$ and $m^2 + m + 1$ to satisfy a relation that, when analyzed modulo powers of $2$, yields $n = m^{2^g}$. $\square$
