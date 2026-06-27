---
role: proof
locale: en
of_concept: proposition-5-18
source_book: gtm040
source_chapter: "5"
source_section: "18"
---

**Proof:** We have $\Pr[p] = 1 - B_{i0}$ and $\Pr[p_n] = 1 - nB_{i0}$. Since the union of the truth sets of the $p_n$ is the truth set of $p$, we have, by Proposition 1-16,

$$1 - B_{i0} = \lim_n (1 - nB_{i0}).$$

For the $N$-matrix we note that

$$nN_{ij} = M_i[nn_j]$$

and

$$n_j = \lim_n nn_j \text{ monotonically.}$$

The result for $N$ therefore follows from the Monotone Convergence Theorem. Since $a_i = M_i[a] = \sum_j N_{ij}$, the assertion about $a_i$ is also a consequence of monotone convergence.

Taking the limits of some of the quantities computed for the finite drunkard's walk we find that

$$B_{i0} = \begin{cases} 1 & \text{if } r \geq 1 \\ r^i & \text{if } r \leq 1 \end{cases}$$

and

$$a_i = \begin{cases} \frac{i}{q - p} & \text{if } r > 1 \\ +\infty & \text{if } r \leq 1. \end{cases}$$

The value of $B_{i0}$ shows that the chain is absorbing when $p \leq q$; that is, $a$ is finite almost everywhere when $p \leq q

If we have calculated $B_{i0}$ and have seen that $a$ is a stopping time when $p \leq q$, we may compute $M_i[a]$ directly from martingales without any knowledge of the $N$-matrix. Let $p \leq q$, and for $0 < s \leq 1$ define

$$f(k, n) = \frac{s^k}{(ps + qs^{-1})^n},$$

where $n$ represents time and $k$ represents position. Now

$$f(k, n) = s^k(ps + qs^{-1})^{-n} \leq (ps + qs^{-1})^{-n},$$

which is maximized when $s = \sqrt{q/p}$. Thus

$$f(k, n) \leq (p/q)^{n/2}$$

$$\leq 1 \quad \text{since } p \leq q.$$

Hence $f$ is bounded. It is easily seen that $\{f(x_n, n)\}$ is a martingale: Since $f$ is bounded, $M[f]$ is finite; the reader may verify the regularity property by showing that

$$p \cdot f(x_n + 1, n + 1) + q \cdot f(x_n - 1, n + 1) = f(x_n, n).$$

Let $a$ be the stopping time of Corollary 3-16. Taking $i$ as the starting state, we have

$$\frac{s^i}{(ps + qs^{-1})^0} = \sum \Pr[a = n] \frac{s^0}{(ps + qs^{-1})^n}.$$

Set $1/u = ps + qs^{-1}$. Then

$$s = \frac{1 - \sqrt{1 - 4pqu^2}}{2pu}$$

and

$$\sum \Pr[a = n] u^n = \left( \frac{1 - \sqrt{1 - 4pqu^2}}{2pu} \right)^i.$$

Defining

$$\varphi(u) = \sum \Pr[a = n] u^n,$$

we note that

$$\varphi'(u) = \sum n \Pr[a = n

The present method further allows us to find the probability distribution of $\Pr[\mathbf{a} = n]$ by expanding $[(1 - \sqrt{1 - 4pqu^2})/(2pu)]^i$ as a power series in $u$. We thus find that

$$\Pr[\mathbf{a} = n] = 0 \quad \text{for } n < i$$
$$\Pr[\mathbf{a} = i] = q^i$$
$$\Pr[\mathbf{a} = i + 1] = 0$$
$$\Pr[\mathbf{a} = i + 2] = ipq^{i+1}$$

and so on.

6. A zero-one law for sums of independent random variables

Historically, the first infinite Markov chain that was studied was the sums of independent random variables process. We gather some of the results in the next few sections, beginning with two propositions and a corollary of rather general applicability.
