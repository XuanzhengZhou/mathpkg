---
role: proof
locale: en
of_concept: stable-limit-distribution-condition
source_book: gtm095
source_chapter: "3"
source_section: "§6. Infinitely divisible and stable distributions"
---

# Proof of Stability Characterizes Limit Distributions of Normalized Sums

Let $\xi_1, \xi_2, \ldots$ be a sequence of independent identically distributed random variables and $S_n = \xi_1 + \cdots + \xi_n$. Suppose that there are constants $b_n$ and $a_n > 0$, and a random variable $T$, such that

$$\frac{S_n - b_n}{a_n} \xrightarrow{d} T.$$

We must show that $T$ is a limit in distribution of random variables of the form $(S_n - b_n)/a_n$, $a_n > 0$, if and only if $T$ is stable.

**Sufficiency ($\Leftarrow$).** If $T$ is stable, then by the definition of stability (equation (4) in the text), for every $n \geq 1$ there exist constants $a_n > 0$, $b_n$, and independent random variables $\xi_1, \ldots, \xi_n$, distributed like $T$, such that

$$a_n T + b_n \stackrel{d}{=} \xi_1 + \cdots + \xi_n.$$

Equivalently,

$$T \stackrel{d}{=} \frac{S_n - b_n}{a_n},$$

where $S_n = \xi_1 + \cdots + \xi_n$. Consequently $(S_n - b_n)/a_n \stackrel{d}{\to} T$.

**Necessity ($\Rightarrow$).** Conversely, let $\xi_1, \xi_2, \ldots$ be a sequence of independent identically distributed random variables, $S_n = \xi_1 + \cdots + \xi_n$, and suppose

$$\frac{S_n - b_n}{a_n} \stackrel{d}{\to} T, \quad a_n > 0.$$

We must show that $T$ is a stable random variable.

If $T$ is degenerate, it is evidently stable. Suppose that $T$ is nondegenerate.

Choose $k \geq 1$ and partition the first $kn$ summands into $k$ blocks of length $n$:

$$S_n^{(1)} = \xi_1 + \cdots + \xi_n, \quad \ldots, \quad S_n^{(k)} = \xi_{(k-1)n+1} + \cdots + \xi_{kn},$$

and define

$$T_n^{(1)} = \frac{S_n^{(1)} - b_n}{a_n}, \quad \ldots, \quad T_n^{(k)} = \frac{S_n^{(k)} - b_n}{a_n}.$$

Since the blocks are independent and the summands are identically distributed, as $n \to \infty$,

$$(T_n^{(1)}, \ldots, T_n^{(k)}) \stackrel{d}{\to} (T^{(1)}, \ldots, T^{(k)}),$$

where $T^{(1)}, \ldots, T^{(k)}$ are independent copies of $T$.

On the other hand, consider

$$U_n^{(k)} = \frac{\xi_1 + \cdots + \xi_{kn} - k b_n}{a_n}
= \frac{a_{kn}}{a_n} \left( \frac{\xi_1 + \cdots + \xi_{kn} - b_{kn}}{a_{kn}} \right) + \frac{b_{kn} - k b_n}{a_n}
= \alpha_n^{(k)} V_{kn} + \beta_n^{(k)},$$

where

$$\alpha_n^{(k)} = \frac{a_{kn}}{a_n}, \quad \beta_n^{(k)} = \frac{b_{kn} - k b_n}{a_n},$$

and

$$V_{kn} = \frac{\xi_1 + \cdots + \xi_{kn} - b_{kn}}{a_{kn}}.$$

It is clear that

$$V_{kn} = \frac{U_n^{(k)} - \beta_n^{(k)}}{\alpha_n^{(k)}},$$

where $V_{kn} \stackrel{d}{\to} T$ and $U_n^{(k)} \stackrel{d}{\to} T^{(1)} + \cdots + T^{(k)}$ as $n \to \infty$.

By the Convergence of Constants Lemma (established below), there exist constants $\alpha^{(k)} > 0$ and $\beta^{(k)}$ such that

$$\alpha_n^{(k)} \to \alpha^{(k)} \quad \text{and} \quad \beta_n^{(k)} \to \beta^{(k)} \quad \text{as } n \to \infty.$$

Therefore, by the lemma's conclusion,

$$T \stackrel{d}{=} \frac{T^{(1)} + \cdots + T^{(k)} - \beta^{(k)}}{\alpha^{(k)}},$$

which shows that $T$ is a stable random variable (the defining property of stability holds for every $k \geq 1$). $\square$

**Remark.** The hypothesis that $\xi_1, \xi_2, \ldots$ are identically distributed can be weakened to the asymptotic negligibility condition $\max_{1 \leq k \leq n} P(|\xi_{nk}| \geq \varepsilon) \to 0$, under which the theorem remains valid.
