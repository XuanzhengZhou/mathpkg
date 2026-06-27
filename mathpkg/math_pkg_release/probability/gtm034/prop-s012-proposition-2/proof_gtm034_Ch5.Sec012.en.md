---
role: proof
locale: en
of_concept: prop-s012-proposition-2
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: If the hypothesis of P6 holds, one can combine equations (1) and (2) above to conclude that

$$\frac{m_p}{p!} = \lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \frac{1}{(p-1)!} \sum_{k=0}^{\infty} [(k+1) \cdots (k+p-1)] \mathbf{E}_0[\psi_{N,k}]

= \lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \frac{1}{(p-1)!} \sum_{k=0}^{\infty} k^{p-1} \mathbf{E}_0[\psi_{N,k}]

= \lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \frac{1}{p!} \sum_{k=0}^{\infty} pk^{p-1} \mathbf{E}_0[\psi_{N,k}]

= \lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \frac{1}{p!} \sum_{k=0}^{\infty} [(k+1)^p - k^p] \mathbf{E}_0[\psi_{N,k}]

= \lim_{N \to \infty} \frac{1}{p!} \mathbf{E}_0\left[ \left( \frac{\sigma^2}{N^2} \mathbf{T}_N \right)^p \right].

(At several steps we used the hypothesis of P6 to discard a finite number of terms of order $k^{p-2}$ or lower.)

Thus the proof of P4, and hence of T2, will be complete if we can show that the first limit in P6 exists and has the desired value. To investigate this limit it is natural to define the iterates of the Green function

$$R(s,t) = R^1(s,t) = \min(s,t) - st$$

by

$$R^{p+1}(s,t) = \int_0^1 R(s,x)R^p(x,t) \, dx, \quad p \geq

all $(p - 1)$-tuples $(i_1, i_2, \ldots, i_{p-1})$ with $0 \leq i_\nu \leq N, \nu = 1, 2, \ldots, p - 1$. We shall use T1 in the form

$$\frac{\sigma^2}{2N} g_N(x,y) = R\left(\frac{x}{N}, \frac{y}{N}\right) + \epsilon_N(x,y),$$

$$|\epsilon_N(x,y)| \leq \epsilon_N \rightarrow 0 \text{ as } N \rightarrow \infty.$$

Then

$$\left| \left(\frac{\sigma^2}{2}\right)^p N^{1-2p} g_N^p(x,y) - K^p\left(\frac{x}{N}, \frac{y}{N}\right)\right|$$

$$= N^{1-p} \left| \sum \left[ R\left(\frac{x}{N}, \frac{i_1}{N}\right) + \epsilon_N(x,i_1)\right] \cdots \left[ R\left(\frac{i_{p-1}}{N}, \frac{y}{N}\right) + \epsilon_N(i_{p-1},y)\right]$$

$$- \sum R\left(\frac{x}{N}, \frac{i_1}{N}\right) \cdots R\left(\frac{i_{p-1}}{N}, \frac{y}{N}\right)\right|.$$

Using the fact that

$$0 \leq R(x,y) \leq \frac{1}{4}, \quad 0 \leq x,y \leq 1,$$

one obtains

$$\left| \left(\frac{\sigma^2}{2}\right)^p N^{1-2p} g_N^p(x,y) - K^p\left(\frac{x}{N}, \frac{y}{N}\right)\right|$$

$$\leq N^{1-p} \left[ \sum \left(\frac{1}{4} + \epsilon_N\right)^{p-1} - \sum \left(\frac{1}{4}\right)^{p-1}\right]$$

$$= \left(\frac{1}{4} + \epsilon_N\right

when $p \geq p_0$ for all $x, y, N$. Thus it suffices to exhibit an integer $K > 0$ such that $N > K$ implies

$$\left| R^p \left( \frac{x}{N}, \frac{y}{N} \right) - K^p \left( \frac{x}{N}, \frac{y}{N} \right) \right| < \epsilon$$

for all $0 \leq x, y \leq N$ and all $p = 1, 2, \ldots, p_0 - 1$. Since there are only a finite number of values of $p$ to worry about, it suffices to do so for one value of $p$ at a time (choosing afterward the largest value of $K$). So we are through if for each positive integer $p$

$$R^p \left( \frac{x}{N}, \frac{y}{N} \right) - K^p \left( \frac{x}{N}, \frac{y}{N} \right) \rightarrow 0$$

uniformly in $0 \leq x, y \leq N$. When $p = 1$ this difference is already zero. When $p = 2$,

$$K^p \left( \frac{x}{N}, \frac{y}{N} \right) = \frac{1}{N} \sum_{k=0}^{N} R \left( \frac{x}{N}, \frac{k}{N} \right) R \left( \frac{k}{N}, \frac{y}{N} \right)$$

is the Riemann approximating sum to the integral defining the second iterate $R^2(x/N, y/N)$. Such sums do converge uniformly provided only that the function involved, namely $R(x, y)$, is continuous on the square $0 \leq x, y \leq 1$. It is easy to verify this, and then also the case $p > 2$ presents no new difficulties.

Let us now show how P7 completes the proof of T2. In view of P7

$$\lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \sum_{y=0}^{2

That concludes the evaluation of the limit in P6 and hence T2 is proved.

It is worth pointing out a slightly different formulation of T2, which is not without interest.
