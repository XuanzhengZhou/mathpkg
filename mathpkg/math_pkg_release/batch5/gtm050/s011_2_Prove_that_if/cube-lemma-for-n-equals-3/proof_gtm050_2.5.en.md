---
role: proof
locale: en
of_concept: cube-lemma-for-n-equals-3
source_book: gtm050
source_chapter: "2"
source_section: "2.5"
---

Let $a^2+3b^2 = P_1 P_2 \cdots P_n$ be a factorization into 4's and odd primes as given by Statement (4') (which combines the odd factor theorem (5') and the divisibility-by-2 lemma (2')).

Since $a^2+3b^2$ is a cube, every prime factor must occur with multiplicity a multiple of 3. In particular:
- If the factorization contains exactly $k$ factors of 4, then $2^{2k}$ is the largest power of 2 dividing $a^2+3b^2$. Since $a^2+3b^2$ is a cube, $2k$ must be a multiple of 3, hence $k$ itself is a multiple of 3.
- Any odd prime $P$ in the factorization must occur with multiplicity a multiple of 3.

Thus $n$ is divisible by 3, and the factors $P_1, P_2, \ldots, P_n$ can be arranged so that $P_{3k+1} = P_{3k+2} = P_{3k+3}$ for each $k$.

By the factorization theorem (Statement 3), $a+b\sqrt{-3}$ can be written as
$$a + b\sqrt{-3} = \pm (p_1 \pm q_1\sqrt{-3})(p_2 \pm q_2\sqrt{-3}) \cdots (p_n \pm q_n\sqrt{-3})$$
where each factor $p_i \pm q_i\sqrt{-3}$ corresponds to the prime $P_i = p_i^2+3q_i^2$.

Since the prime factors come in groups of three identical $P$'s, and the only ambiguity in the factorization is the choice of sign ($p \pm q\sqrt{-3}$), both signs cannot occur for the same prime (the sign is uniquely determined by the divisibility condition $pb \pm aq$). Therefore, in each group of three, the three linear factors are identical.

Taking one factor from each group of three and multiplying them together yields an element $c+d\sqrt{-3}$ such that
$$a + b\sqrt{-3} = \pm (c + d\sqrt{-3})^3.$$

Since $-(c + d\sqrt{-3})^3 = (-c - d\sqrt{-3})^3$, the sign can be absorbed by replacing $c$ with $-c$ and $d$ with $-d$. Thus there exist integers $p$ and $q$ (namely $p = \pm c$, $q = \pm d$) such that
$$a + b\sqrt{-3} = (p + q\sqrt{-3})^3.$$
