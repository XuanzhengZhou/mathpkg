---
role: proof
locale: en
of_concept: prop-for-arbitrary-random-walk-recurrent-or
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: When $x \in A$ and $y \in A$, the left-hand side in P1(a) is
$$\sum_{t \in R} P(x,t)H_A(t,y) - H_A(x,y)$
$$= P(x,y) + \sum_{t \in R - A} P(x,t)H_A(t,y) - \delta(x,y).$$

Thus we have to show that
$$\Pi_A(x,y) = P(x,y) + \sum_{t \in R - A} P(x,t)H_A(t,y), \quad x \in A, y \in A.$$

Decomposing $\Pi_A(x,y)$ according to the value of $T,$
$$\Pi_A(x,y) = P_z[x_T = y; T < \infty

Here

$$P_z[x_T = y; T = 1] = P(x,y),$$

and when $k \geq 2$,

$$P_z[x_T = y; T = k] = \sum_{t \in R-A} P_z[x_1 = t; x_T = y; T = k]$$

$$= \sum_{t \in R-A} P(x,t)P_t[x_T = y; T = k - 1].$$

Hence

$$\Pi_A(x,y) = P(x,y) + \sum_{t \in R-A} P(x,t) \sum_{k=2}^{\infty} P_t[x_T = y; T = k - 1]$$

$$= P(x,y) + \sum_{t \in R-A} P(x,t)P_t[x_T = y; 1 \leq T < \infty]$$

$$= P(x,y) + \sum_{t \in R-A} P(x,t)H_A(t,y).$$

When $x \in R-A$ and $y \in A$ we have to show that

$$H_A(x,y) = \sum_{t \in R} P(x,t)H_A(t,y),$$

the right-hand side in P1(a) being zero. This is done, just as in the first half of the proof, by decomposing $H_A(x,y)$ according to the possible values of $T$.

The proof of (b) depends on the interpretation of $g_A(x,y)$ as the expected number of visits of the random walk $x_n$ with $x_0 = x$ to the point $y$ before the time $T$ of the first visit to the set $A$. Since there is nothing to prove when either $x$ or $y$ lies in $A$, we assume the contrary. If in addition $x \neq y$, then

$$g_A(x,y) = \sum_{n=0}^{\infty} Q_n(x,y) = \sum_{n=1}^{\infty} P_z[x_n = y; T > n],$$

and letting $T_y = \min[k \mid 1 \leq k \leq \infty, x_k = y],$

$$g_A(x,y) = \sum_{k=1}^{\infty} \sum_{n=1}^{\infty}

It follows that for all $x,y$ in $R$

$$g_A(x,y) \leq g_A(y,y).$$

The problem of showing that $g_A(y,y) < \infty$ for aperiodic random walk can be reduced to a slightly simpler one by the observation that $g_A(y,y) \leq g_B(y,y)$ when $B$ is a subset of $A$. Thus it suffices to let $B = \{0\}$, $g_B(x,y) = g(x,y)$, and to show that

$$g(x,x) < \infty$$

when $x \neq 0$. This is true for transient, as well as for recurrent random walk, but for different reasons. In the transient case clearly

$$g(x,x) < G(x,x) < \infty.$$

In the recurrent case

$$g(x,x) = 1 + \sum_{n=1}^{\infty} P_z[x_n = x; T_0 > n]$$

where $T_y = \min[k \mid 1 \leq k < \infty, x_k = y]$. Since the random walk is aperiodic, $P_z[T_0 < \infty] = F(x,0) = 1$ by T2.1. In addition it is easy to see that

$$P_z[T_0 < T_z] = \Pi_{(0,x)}(x,0) > 0.$$

But $g(x,x)$ is the expected value of the number of visits to $x$ (counting the visit at time 0) before the first visit to 0. It is quite simple to calculate this expectation (it is the mean of a random variable whose distribution is geometric) and the result of the calculation is

$$g(x,x) = \left[ \Pi_{(0,x)}(x,0) \right]^{-1} < \infty.$$

The reader who is reluctant to fill in the details will find that P3 below yields a much shorter proof that $g_{(0)}(x,x) = g(x,x) < \infty$.

To prove (c) we decompose $H_A(x,y)$ as follows. For $x \in R - A$, $y \in A$,

$$H_A(x,y) = \sum_{n=1}^{\infty} \

Part (d) is of absolutely no interest when the random walk is recurrent, for then both sides are infinite (or possibly both are zero in the periodic case). However, the proof which follows is quite general. We write, for $x \in R - A, y \in A$,

$$G(x,y) = \sum_{n=0}^{\infty} P_n(x,y) = \sum_{n=0}^{\infty} P_z[x_n = y]$$

$$= \sum_{n=0}^{\infty} \sum_{k=1}^{n} P_z[x_n = y; T = k]$$

$$= \sum_{t \in A} \sum_{n=0}^{\infty} \sum_{k=1}^{n} P_z[T = k, x_T = t] P_t[x_{n-k} = y]$$

$$= \sum_{t \in A} \left\{ \sum_{k=1}^{\infty} P_z[T = k, x_T = t] \right\} \left\{ \sum_{n=0}^{\infty} P_t[x_n = y] \right\}$$

$$= \sum_{t \in A} H_A(x,t) G(t,y).$$

That completes the proof of P1.

A very simple but powerful technique, successful because the random variables $X_k = x_{k+1} - x_k$ are identically distributed and independent, consists of reversing a random walk.
