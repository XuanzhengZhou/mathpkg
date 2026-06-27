---
role: proof
locale: en
of_concept: factorization-of-a-plus-b-sqrt-minus-3
source_book: gtm050
source_chapter: "2"
source_section: "2.5"
---

Factor $a^2+3b^2 = P_1 P_2 \cdots P_n$ into 4's and odd primes as given by Statement (4')—that is, by repeatedly applying the odd factor theorem (Statement 5') to extract prime factors, and using Statement (2') to handle factors of 2 (which must occur as factors of 4).

For each prime factor $P = p^2+3q^2$ (given by Statement 5'), the fact that $P$ divides $a^2+3b^2$ implies, by the identity $(p^2+3q^2)(a^2+3b^2) = (pa-3qb)^2 + 3(pb+aq)^2$, that $P$ divides either $pb+aq$ or $pb-aq$.

If $pb+aq$ is divisible by $P$, then dividing the identity by $P^2$ yields
$$\frac{a^2+3b^2}{P} = \left(\frac{pa-3qb}{P}\right)^2 + 3\left(\frac{pb+aq}{P}\right)^2,$$
so $u = (pa-3qb)/P$ and $v = (pb+aq)/P$ are integers, and
$$u + v\sqrt{-3} = \frac{(p+q\sqrt{-3})(a+b\sqrt{-3})}{P}.$$

Multiplying by $p-q\sqrt{-3}$ gives $(p-q\sqrt{-3})(u+v\sqrt{-3}) = a+b\sqrt{-3}$, or equivalently,
$$a+b\sqrt{-3} = (p-q\sqrt{-3})(u+v\sqrt{-3}).$$

If $pb-aq$ is divisible by $P$, the symmetric argument gives $a+b\sqrt{-3} = (p+q\sqrt{-3})(u+v\sqrt{-3})$.

Iterating this extraction for each prime factor $P_i$ yields the factorization
$$a+b\sqrt{-3} = \pm(p_1 \pm q_1\sqrt{-3})(p_2 \pm q_2\sqrt{-3})\cdots(p_n \pm q_n\sqrt{-3}).$$
