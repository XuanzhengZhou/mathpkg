---
role: proof
locale: en
of_concept: prop-if-a-random-walk-is-recurrent
source_book: gtm034
source_chapter: "1"
source_section: "002"
---

Proof: If $x \in R^+$, we may assume that $x \neq 0$ and choose $m \geq 1$ so that $P_m(0,x) > 0$. Then, using P1.1,

$$P_m(0,x)P_n(x,x) \leq \sum_{t \in R} P_m(0,t)P_n(t,x) = P_{m+n}(0,x).$$

Summing on $n$ from zero to $k$, one obtains

$$P_m(0,x)G_k(x,x) = P_m(0,x)G_k(0,0) \leq \sum_{n=0}^{k} P_{m+n}(0,x)$$

$$= \sum_{n=0}^{m+k} P_n(0,x) - \sum_{n=0}^{m-1} P_n(0,x)$$

$$= G_{m+k}(0,x) - G_{m-1}(0,x).$$

Letting $k \to +\infty$, one finds that

$$P_m(0,x) \cdot G \leq \lim_{k \to \infty} G_{m+k}(0,x) - G_{m-1}(0,x).$$

But by P1.4, we know that $G = +\infty$, which proves that

$$\lim_{k \to \infty} G_{m+k}(0,x) = G(0,x) = +\infty.$$

The next step, still for recurrent random walk, is the investigation of $F(0,x)$. The obvious probability interpretation of $F(0,x)$ as the probability of a visit to $x$, starting at 0, in a finite time is very helpful. It suggests that $F(0,x) = 1$ for all $x$ in $R^+$. Actually considerable work is required

the hypothesis that the random walk is recurrent. Therefore we have "demonstrated" the impossibility of having $x \in R^+$ while $-x \in R - R^+$. In other words, recurrent random walk has the property that $x \in R^+$ implies $-x \in R^+$. But $R^+$ is a semigroup, and a semigroup which contains the inverse (negative) of each element is a group. Hence $R^+ = \bar{R}$. Now it is easy to go further, and to conclude that $F(0,x) = 1$ not only when $x \in R^+$, but for all $x \in \bar{R}$.

We shall choose to disregard this interesting argument, which is due to Feller [12],* 1951, to obtain the same result by the more elementary methods of this and the last section.
