---
role: proof
locale: en
of_concept: prop-for-and
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: Operating on part (a) of P10.1 by the transition function $P(x,y)$ on the left gives
$$\sum_{t \in R} P_2(x,t)H_A(t,y) - \sum_{t \in R} P(x,t)H_A(t,y) = \sum_{t \in B} P(x,t)[\Pi_B(t,y) - \delta(t,y)].$$

Now we do this again $n - 1$ times, and the resulting $n + 1$ equations, counting the original one, may be expressed in the abbreviated form
$$PH = H + \Pi - I, \quad P_2H = PH + P(\Pi - I), \ldots, \quad P_{n+1}H = P_nH + P_n(\Pi - I).$$

Adding these equations, using $I$ to denote the identity operator, one finds
$$P_{n+1}H = H + (I + P + \cdots + P_n)(\Pi - I).$$

This shows that P1 holds, if we remember that $I + P + \cdots + P_n$ stands for
$$G_n(x,y) = \sum_{k=0}^{n} P_k(x,y),$$

in view of D1.3.

The next lemma uses the recurrence of the random walk in an essential way. It is
