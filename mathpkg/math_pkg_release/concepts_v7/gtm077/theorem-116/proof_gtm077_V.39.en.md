---
role: proof
locale: en
of_concept: theorem-116
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 116

**Theorem 116.** If $\mu$ is a number in $k$ which is not the $l$-th power of a number in $k$, then the field $K = k(\sqrt[l]{\mu})$ has the relative degree $l$ with respect to $k$. Moreover, $K$ is identical with all its relative-conjugate fields.

**Proof.** Let $M = \sqrt[l]{\mu}$ (with some fixed choice of the root). Then $M$ satisfies the equation $x^l - \mu = 0$, whose roots are the $l$ numbers

$$\zeta^a M \quad (a = 0, 1, \ldots, l-1),$$

where $\zeta = e^{2\pi i/l}$ and the hypothesis guarantees that $k$ contains $\zeta$.

All relative conjugates of $M$ must occur among these $l$ numbers. Let these conjugates be the $m$ numbers ($m \leq l$)

$$\zeta^{a_1} M, \zeta^{a_2} M, \ldots, \zeta^{a_m} M.$$

As the relative norm of $M$, their product belongs to $k$; therefore $M^m \in k$. But we also know $M^l = \mu \in k$.

Since $l$ is prime, if $m < l$ then $\gcd(m, l) = 1$. In that case there exist integers $u, v$ such that $um + vl = 1$, whence

$$M = M^{um + vl} = (M^m)^u (M^l)^v \in k.$$

This would mean $M \in k$, implying $\mu$ is an $l$-th power in $k$, contradicting the hypothesis.

Therefore the only possibilities are $m = 1$ or $m = l$. The case $m = 1$ is excluded by hypothesis, so $m = l$. Thus the relative degree of $K$ over $k$ is $l$, and all $l$ conjugates $\zeta^a M$ are distinct relative conjugates of $M$. Hence $K$ coincides with all its relative-conjugate fields.
