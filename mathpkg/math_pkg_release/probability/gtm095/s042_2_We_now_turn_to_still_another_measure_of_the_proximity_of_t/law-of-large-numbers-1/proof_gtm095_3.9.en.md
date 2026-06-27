---
role: proof
locale: en
of_concept: law-of-large-numbers-1
source_book: gtm095
source_chapter: "3"
source_section: "9.2"
---

# Proof of the Law of Large Numbers (for empirical distribution functions)

**Theorem (Law of Large Numbers, Sect. 3, Theorem 2).** Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with $\mathbb{E}|\xi_1| < \infty$ and $\mathbb{E}\xi_1 = \mu$. Then

$$\frac{\xi_1 + \cdots + \xi_n}{n} \xrightarrow{\mathbb{P}} \mu, \quad n \to \infty,$$

i.e., convergence in probability.

**Application in the context of §9.2.** In the setting of discrimination between two hypotheses, let $\xi_1, \xi_2, \ldots$ be independent identically distributed random elements with distribution either $P$ (Hypothesis $H$) or $\tilde{P}$ (Hypothesis $\tilde{H}$), where $\tilde{P} \neq P$ and therefore $\rho^2(P, \tilde{P}) > 0$. The law of large numbers ensures that the empirical frequencies converge to the true probabilities, making consistent discrimination possible as $n \to \infty$.

More concretely, for the empirical distribution function

$$F_N(x; \omega) = \frac{1}{N} \sum_{k=1}^{N} I(\xi_k(\omega) \leq x),$$

the law of large numbers gives, for each fixed $x \in \mathbb{R}$,

$$F_N(x; \omega) \xrightarrow{\mathbb{P}} F(x), \quad N \to \infty.$$

**Proof sketch (Khinchin's form).** Let $\varphi(t) = \mathbb{E}e^{it\xi_1}$ be the characteristic function of $\xi_1$. The characteristic function of the sample mean $\overline{\xi}_n = \frac{1}{n}\sum_{k=1}^{n} \xi_k$ is

$$\varphi_{\overline{\xi}_n}(t) = \left[\varphi\left(\frac{t}{n}\right)\right]^n.$$

By the Taylor expansion $\varphi(t) = 1 + i\mu t + o(t)$ as $t \to 0$, we have

$$\varphi\left(\frac{t}{n}\right) = 1 + \frac{i\mu t}{n} + o\left(\frac{1}{n}\right),$$

and therefore

$$\varphi_{\overline{\xi}_n}(t) = \left[1 + \frac{i\mu t}{n} + o\left(\frac{1}{n}\right)\right]^n \to e^{i\mu t}, \quad n \to \infty.$$

Since $e^{i\mu t}$ is the characteristic function of the constant $\mu$, the continuity theorem for characteristic functions implies $\overline{\xi}_n \xrightarrow{d} \mu$, and convergence in distribution to a constant is equivalent to convergence in probability.

**Connection to the Hellinger distance (§9.2).** For the error probability $\mathcal{E}r(P^n, \tilde{P}^n)$ of optimal discrimination, the law of large numbers together with the inequalities

$$\frac{1}{2} e^{-2\lambda n} \leq \mathcal{E}r(P^n, \tilde{P}^n) \leq e^{-\lambda n} \leq e^{-n\rho^2(P, \tilde{P})}, \quad \lambda = -\log H(P, \tilde{P}),$$

shows that when $\rho^2(P, \tilde{P}) > 0$, the error probability decreases exponentially to zero as $n \to \infty$.
