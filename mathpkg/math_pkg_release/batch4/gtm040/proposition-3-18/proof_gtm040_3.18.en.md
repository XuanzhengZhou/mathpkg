---
role: proof
locale: en
of_concept: proposition-3-18
source_book: gtm040
source_chapter: "3"
source_section: "18"
---

**Proof:** We may assume that $f \geq 0$ since the general case follows by considering $f^+$ and $f^-$ separately. Then $g_n \geq 0

Choose $N$ large enough so that the right side is less than $\delta$. Then for all $n$ we have

$$\int_{\{g_n \geq N\}} f d\mu < \epsilon.$$

Since

$$\int_{\{g_n \geq N\}} g_n d\mu = \int_{\{g_n \geq N\}} f d\mu$$

by Lemma 3-6, we conclude the $g_n$ are uniformly integrable.

Let $E$ be any subset of $\mathcal{R}_n^*$. For $m \geq n$,

$$\int_E g_m d\mu = \int_E f d\mu.$$

By uniform integrability and Proposition 1-52,

$$\lim_m \int_E g_m d\mu = \int_E g_d\mu.$$

Therefore

$$\int_E f d\mu = \int_E g_d\mu$$

for all $E$ in $\bigcup \mathcal{R}_n^*$. The two sides of this last equation, considered as set functions, are equal on $\bigcup \mathcal{R}_n^*$. By the uniqueness half of Theorem 1-19 they must be equal on $\mathcal{R}^*$. That is, $f$ and $g$ are measurable with respect to $\mathcal{R}^*$ and satisfy

$$\int_E f d\mu = \int_E g_d\mu.$$

Taking $E$ successively to be the set where $f \geq g$ and the set where $f \leq g$ and applying Corollary 1-40, we find that $f = g$ a.e.

5. Examples of convergent martingales

Four examples will serve at present to illustrate Theorems 3-12 and 3-15. Each of the first three refers to the correspondingly numbered example in Section 2.

Example 1: The sequence $\{s_n\}$ of $n$th partial sums of the independent random variables $y_n$ forms a martingale if $M[y_n] = 0$. Suppose the $y_n$ have identical distributions and mean zero, suppose they assume only the values 0, 1, and $-1$, and suppose that the process is stopped whenever $

if $s_n(\omega)$ ever equals $-N$ and he breaks the bank if $s_n(\omega) = M$. Set

$$p = \Pr[\text{player breaks the bank}]$$

and

$$q = \Pr[\text{player is eventually ruined}].$$

By the remarks following Proposition 3-17, $p + q = 1$. In this situation, Corollary 3-16 applies and

$$0 = M[s_0] = M[s_t] = p \cdot M + q(-N)$$

$$= pM + (1 - p)(-N)$$

or

$$p = \frac{N}{M + N}$$

and

$$q = \frac{M}{M + N}.$$

**Example 2:** With the particle moving on the line, suppose there is an $r > 0$ which is a root of the equation $f(s) = 1$. We shall assume that $r < 1$. Then $\{r^{x_n}\}$ is a non-negative martingale, and by Corollary 3-13, $\{r^{x_n}\}$ converges to a limiting function a.e. Since $x_n$ is integer-valued, this convergence means either

(1) for almost all $\omega$, there is an $N$ such that if $n \geq N$, then $x_n = x_N$, or

(2) $\lim x_n = +\infty$.

Now $x_N = x_{N+1} = x_{N+2} = \cdots = x_{N+k}$ means that the particle fails to move for $k$ consecutive steps. Since such a thing happens with probability $p_0^k < 1$, the probability that $x_n = x_N$ for all $n \geq N$ is zero. Thus case 1 is eliminated, and we have established that $\lim x_n = +\infty$ a.e. That is, for any $k$ and for almost all $\omega$, $x_n(\omega) = k$ for only finitely many $n$.
