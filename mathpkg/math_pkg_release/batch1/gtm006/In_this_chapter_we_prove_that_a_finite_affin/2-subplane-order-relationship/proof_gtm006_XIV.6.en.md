---
role: proof
locale: en
of_concept: 2-subplane-order-relationship
source_book: gtm006
source_chapter: "XIV"
source_section: "6"
---

Let $\Gamma$ be the $2$-subgroup of $\Pi$ whose fixed elements are the points and lines of $\mathcal{Q}$. If $\Gamma = 1$, then $\mathcal{Q} = \mathcal{P}$ and $n = m$, so $g = 0$ and the theorem holds trivially.

Assume $\Gamma \neq 1$. Let $P$ be a point of $\mathcal{P}$ not in $\mathcal{Q}$. The orbit of $P$ under $\Gamma$ has size equal to $[\Gamma : \Gamma_P]$, which is a power of $2$ (since $\Gamma$ is a $2$-group). The fixed points of $\Gamma$ are exactly the points of $\mathcal{Q}$, and each orbit of $\Gamma$ on $\mathcal{P} \setminus \mathcal{Q}$ has size a power of $2$ greater than $1$.

Counting the total number of points: $|\mathcal{P}| = |\mathcal{Q}| + \sum (\text{orbit sizes})$. Since $|\mathcal{P}| = n^2 + n + 1$ and $|\mathcal{Q}| = m^2 + m + 1$, and each orbit size is a power of $2$, we have $n^2 + n + 1 \equiv m^2 + m + 1 \pmod{2}$ (in fact, modulo higher powers). By induction on the structure of the $2$-group action, one deduces that $n$ is a power of $m$ with exponent a power of $2$, i.e., $n = m^{2^g}$.
