---
role: proof
locale: en
of_concept: decomposition-in-relative-quadratic-I
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 116

**Theorem.** If $\mu$ is a number in $k$ which is not the $l$th power of a number in $k$, then the field $K = K(\sqrt[l]{\mu}; k)$ has the relative degree $l$ with respect to $k$. The field $K$ is identical with all its relative-conjugate fields.

*Proof.* Let $M = \sqrt[l]{\mu}$ (fix some value of the root). Then $M$ satisfies the equation

$$x^l - \mu = 0,$$

whose roots are the $l$ numbers

$$\zeta^a M \qquad (a = 0, 1, \ldots, l-1).$$

All relative conjugates of $M$ with respect to $k$ must occur among these $l$ numbers. Let these conjugates be

$$\zeta^{a_1} M,\; \zeta^{a_2} M,\; \ldots,\; \zeta^{a_m} M,$$

where $m \leq l$. Their product is the relative norm of $M$, hence lies in $k$. Therefore $M^m \in k$. But we also have $M^l = \mu \in k$.

If $m < l$, then since $l$ is prime, $m$ is relatively prime to $l$. Hence there exist integers $r, s$ such that $rm + sl = 1$, and consequently

$$M = M^{rm + sl} = (M^m)^r (M^l)^s \in k.$$

This would mean $M \in k$, which contradicts the hypothesis that $\mu$ is not an $l$th power in $k$. Therefore the only possibilities are $m = 1$ (in which case $M \in k$, impossible by hypothesis) or $m = l$. Hence $m = l$, proving that the relative degree is $l$ and that all $l$ conjugates occur, so $K$ is identical with all its relative-conjugate fields. $\square$
