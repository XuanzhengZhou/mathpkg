---
role: proof
locale: en
of_concept: cramer-chernoff-bound-bernoulli
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Cramér–Chernoff Bound for Bernoulli Sums

Let $\xi_1, \ldots, \xi_n$ be independent identically distributed random variables with $P(\xi_i = 1) = p$, $P(\xi_i = 0) = q = 1-p$, and let $S_n = \xi_1 + \cdots + \xi_n$.

Define the moment generating function of a single trial:
$$\varphi(\lambda) = E[e^{\lambda \xi_1}] = (1-p) \cdot 1 + p \cdot e^{\lambda} = 1 - p + p e^{\lambda}.$$

By independence,
$$E[e^{\lambda S_n}] = [\varphi(\lambda)]^n.$$

Apply the exponential Chebyshev inequality to the random variable $X = S_n / n$ (which is nonnegative). For any $a$ with $0 < a < 1$, and any $\lambda > 0$,

$$P\left\{ \frac{S_n}{n} \geq a \right\} \leq \inf_{\lambda > 0} E[e^{\lambda(S_n / n - a)}] = \inf_{\lambda > 0} e^{-n [ \lambda a / n - \log \varphi(\lambda / n) ]}.$$

With the substitution $s = \lambda / n$, this becomes

$$P\left\{ \frac{S_n}{n} \geq a \right\} \leq \inf_{s > 0} e^{-n [ a s - \log \varphi(s) ]} = \exp\!\left( -n \sup_{s > 0} [a s - \log \varphi(s)] \right). \tag{36}$$

A completely analogous argument with $\lambda < 0$ yields

$$P\left\{ \frac{S_n}{n} \leq a \right\} \leq \exp\!\left( -n \sup_{s < 0} [a s - \log \varphi(s)] \right). \tag{37}$$

It remains to evaluate the supremum of the function
$$f(s) = a s - \log(1 - p + p e^{s}).$$

For $p \leq a \leq 1$, $f$ attains its maximum at a point $s_0 > 0$ determined by

$$f'(s_0) = a - \frac{p e^{s_0}}{1 - p + p e^{s_0}} = 0,$$

which gives
$$e^{s_0} = \frac{a(1-p)}{p(1-a)}.$$

Substituting back,
$$\sup_{s > 0} f(s) = f(s_0) = a \log \frac{a}{p} + (1-a) \log \frac{1-a}{1-p} \equiv H(a).$$

Here $H(a)$ is the relative entropy (Kullback–Leibler divergence) between the Bernoulli distributions with parameters $a$ and $p$.

Therefore we obtain the **Cramér–Chernoff bounds**:

- For $p \leq a \leq 1$: $\displaystyle P\left\{ \frac{S_n}{n} \geq a \right\} \leq e^{-n H(a)}.$

- For $0 \leq a \leq p$: $\displaystyle P\left\{ \frac{S_n}{n} \leq a \right\} \leq e^{-n H(a)}.$

These bounds show that the probability of a sample mean deviating from $p$ decays exponentially fast in $n$, with rate governed by the relative entropy $H(a)$.
