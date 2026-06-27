---
role: proof
locale: en
of_concept: characterization-of-finite-order-element
source_book: gtm028
source_chapter: "I"
source_section: "2. Groups"
---

Let $a$ be an element of finite order $m$, meaning the cyclic subgroup $H = \langle a \rangle$ has $m$ elements.

Since $H$ is finite, there exist distinct integers $n, n'$ such that $a^n = a^{n'}$ (otherwise $H$ would be infinite). From $a^n = a^{n'}$ we obtain $a^{n-n'} = 1$, so there exist positive integers $\nu$ such that $a^\nu = 1$. Let $\mu$ be the smallest such positive integer.

We claim that $1, a, a^2, \ldots, a^{\mu-1}$ are distinct elements. If $a^i = a^j$ with $0 \leq i < j < \mu$, then $a^{j-i} = 1$ with $0 < j-i < \mu$, contradicting the minimality of $\mu$.

For any integer $n$, write $n = q\mu + n'$ with $0 \leq n' < \mu$. Then
$$a^n = a^{q\mu+n'} = (a^\mu)^q \cdot a^{n'} = 1^q \cdot a^{n'} = a^{n'}.$$
Thus every power $a^n$ is equal to one of $1, a, a^2, \ldots, a^{\mu-1}$, so the cyclic group consists precisely of these $\mu$ elements. Hence $\mu = m$, establishing (1) and (2).

For (3): if $m \mid n$, write $n = qm$, then $a^n = (a^m)^q = 1^q = 1$. Conversely, if $a^n = 1$, write $n = qm + n'$ with $0 \leq n' < m$. Then $1 = a^n = a^{qm+n'} = (a^m)^q a^{n'} = a^{n'}$. If $n' > 0$, this contradicts the minimality of $m$. Hence $n' = 0$, so $m \mid n$.
