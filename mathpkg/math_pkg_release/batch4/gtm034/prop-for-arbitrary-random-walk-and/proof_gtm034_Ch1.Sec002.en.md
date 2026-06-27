---
role: proof
locale: en
of_concept: prop-for-arbitrary-random-walk-and
source_book: gtm034
source_chapter: "1"
source_section: "002"
---

Proof: Part (a) follows by computation from P1.1 and D1.3 since

$$\sum_{t \in R} P(x,t)G_n(t,y) = \sum_{k=0}^{n} \sum_{t \in R} P(x,t)P_k(t,y)$$

$$= \sum_{k=1}^{n+1} P_k(x,y) = G_{n+1}(x,y) - \delta(x,y).$$

Dividing equation (a) by $G_n(0,0)$ (which is positive), one finds

(1) $$\sum_{t \in R} P(x,t) \frac{G_n(t,y)}{G_n(0,0)} = \frac{G_n(x,y)}{G_n(0,0)} + \frac{P_{n+1}(x,y)}{G_n(0,0)} - \frac{\delta(x,y)}{G_n(0,0)

so that one may conclude, by letting $n$ tend to infinity in (1), that part (b) of P4 is true.

Now we shall see that P4 very quickly leads to
