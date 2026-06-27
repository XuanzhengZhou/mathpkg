---
role: proof
locale: en
of_concept: prop-if-is-a-stopping-time-and
source_book: gtm034
source_chapter: "1"
source_section: "003"
---

Proof: Since $P[\cdot]$ is a completely additive measure, the measure of the intersection of a monotone sequence of sets is the limit of their measures (see (1) preceding D1). Since the sets $\bigcup_{k=n}^{\infty} A_k = B_n$ form a monotone sequence, we have

(1) $P\left[\lim_{n \to \infty} A_n\right] = \lim_{n \to \infty} P[B_n]$.

Now consider the sets

$$B_{n,m} = \bigcup_{k=n}^{n+m} A_k$$

which are easily seen to have measure

(2) $P[B_{n,m}] = \sum_{t \in R} P_{n-1}(0,t) \sum_{k=1}^{m+1} F_k(t,0), \quad n \geq 1, \quad m \geq 0.$

In the recurrent case we let $m \to \infty$ in (2), observing that the sets $B_{n,m}$ increase to $B_n$, so that

(3) $P[B_n] = \lim_{m \to \infty} P[B_{n,m}] = \sum_{t \in R} P_{n-1}(0,t) F(t,0).$

But we know from P2.5 that $F(t,0) = 1$ for all $t$ such that $P_{n-1}(0,t) > 0$. Therefore $P[B_n] = 1$ for $n \geq 1$, and equation (1) shows that

$$P\left[\lim_{n \to \infty} A_n\right] = 1.$$

In the transient case one goes back to equation (2), observing that

(4) $P[B_{n,m}] \leq \sum_{t \in R} P_{n-1}(0,t) \sum_{k=1}^{m+1} P_k(t,0)$

$$= \sum_{j=n}^{n+m} P_j(0,0) = G_{n+m}(0,0) - G_{n-1}(0,0), \quad n \geq 1.$$

If we let $m \to \

The next step brings us to Kolmogorov's strong law of large numbers which we shall formulate, without proof, in the terminology of D1.
