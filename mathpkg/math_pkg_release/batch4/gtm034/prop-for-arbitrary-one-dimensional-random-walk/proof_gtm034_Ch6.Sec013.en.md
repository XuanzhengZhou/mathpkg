---
role: proof
locale: en
of_concept: prop-for-arbitrary-one-dimensional-random-walk
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Clearly (1), (2), and (3) are mutually exclusive and exhaust all possibilities. Now (1) implies (i) by a very simple probability argument which was given in Chapter IV. For $x \leq 0$, $H_A(x) = P[M > x]$, where $M = \max_{k \geq 0} S_k$. But in P19.2, $M$ was shown to be a random variable when (1) holds, and that proves (i).

Now suppose that either (2) or (3) holds. Then it is evident that $H_A(x) \equiv 1$ on $R$ and also that

$$H_A(x,y) = \hat{H}_A(x,y) \text{ for } x \leq 0, y > 0.$$

This relation makes it convenient to work with the random walk $\hat{x}_n$ defined by $\hat{P}(x,y)$ in D1 above. It is a transient random walk, whether $P(x,y)$ defines a transient random walk or not. Therefore it has a finite Green function which we may call

$$\hat{G}(x,y) = \sum_{n=0}^{\infty} \hat{P}_n(x,y).$$

When $x \leq 0$ and $y > 0$, $\hat{G}(x,y)$ is the probability that the random walk $\hat{x}_n$ defined by $\hat{P}$ visits $y$ in a finite time, if it starts at $\hat{x}_0 = x$. Now one can write

Now we shall apply the renewal theorem for positive random variables (P2) to the Green function $\hat{G}(x,y)$. It gives

$$\lim_{x \to -\infty} \hat{G}(x,t) = \frac{1}{E_0[Z]} \geq 0, \quad t \in R.$$

Therefore

$$\lim_{x \to -\infty} H_A(x,y) = \lim_{x \to -\infty} \hat{H}_A(x,y)$$

$$= \lim_{x \to -\infty} \left\{ \hat{G}(x,y) - \sum_{t=1}^{y-1} \hat{G}(x,t)P_0[Z = y-t] \right\}$$

$$= \frac{1}{E_0[Z]} \left\{ 1 - \sum_{t=1}^{y-1} P_0[Z = y-t] \right\} = \frac{P_0[Z \geq y]}{E_0[Z]} \geq 0$$

for $y \geq 1$.

But if (2) holds, then $E_0[Z] = +\infty$ so that the above limit is to be interpreted as zero according to the renewal theorem P2. Hence (2) implies (ii), and for the same reason (3) implies (iii). The formula for $\gamma_A(y)$ in P7, is of course the one obtained above, as a by-product of the method of proof.

Only a small step remains to be taken to obtain
