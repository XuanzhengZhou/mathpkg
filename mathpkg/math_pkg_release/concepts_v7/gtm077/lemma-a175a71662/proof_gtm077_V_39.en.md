---
role: proof
locale: en
of_concept: lemma-a175a71662
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of The numbers $1 - \zeta^a$ are all associated

We prove two assertions:

**1. The numbers $1 - \zeta^a$ ($a \not\equiv 0 \pmod{l}$) are all associated.**

Let $a$ and $a_1$ be rational integers coprime to $l$. Determine a positive rational integer $b$ such that

$$ab \equiv a_1 \pmod{l},$$

so that $\zeta^{a_1} = \zeta^{ab}$. Then

$$\frac{1 - \zeta^{a_1}}{1 - \zeta^a} = \frac{1 - \zeta^{ab}}{1 - \zeta^a} = 1 + \zeta^a + \zeta^{2a} + \cdots + \zeta^{(b-1)a},$$

which is a sum of roots of unity and hence an algebraic integer. The same reasoning applies to the inverse quotient $\frac{1 - \zeta^a}{1 - \zeta^{a_1}}$ by interchanging the roles of $a$ and $a_1$. Therefore the quotient is both an algebraic integer and its inverse is an algebraic integer, which means it is a unit. Consequently, $1 - \zeta^a$ and $1 - \zeta^{a_1}$ are associated.

**2. The ideal equation $(l) = (1 - \zeta)^{l-1}$.**

Consider the cyclotomic polynomial

$$\Phi_l(x) = 1 + x + x^2 + \cdots + x^{l-1} = \prod_{a=1}^{l-1} (x - \zeta^a).$$

Evaluating at $x = 1$ yields

$$l = \Phi_l(1) = \prod_{a=1}^{l-1} (1 - \zeta^a).$$

By part 1, each factor $1 - \zeta^a$ is associated to $1 - \zeta$, so there exist units $\varepsilon_a$ such that $1 - \zeta^a = \varepsilon_a (1 - \zeta)$. Hence

$$l = \prod_{a=1}^{l-1} \varepsilon_a (1 - \zeta) = \varepsilon (1 - \zeta)^{l-1},$$

where $\varepsilon = \prod_{a=1}^{l-1} \varepsilon_a$ is a unit. Passing to ideals, $(l) = (1 - \zeta)^{l-1}$.
