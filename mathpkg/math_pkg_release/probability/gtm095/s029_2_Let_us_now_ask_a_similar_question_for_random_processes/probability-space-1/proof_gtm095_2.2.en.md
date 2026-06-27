---
role: proof
locale: en
of_concept: probability-space-1
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Corollary 2: Existence of a Markov Process

**Corollary 2.** Let $T = [0, \infty)$ and let $\{P(s, x; t, B)\}$ be a family of nonnegative functions defined for $s, t \in T$, $t > s$, $x \in \mathbb{R}$, $B \in \mathcal{B}(\mathbb{R})$, and satisfying the following conditions:

(a) $P(s, x; t, B)$ is a probability measure in $B$ for given $s$, $x$ and $t$;

(b) for given $s$, $t$ and $B$, the function $P(s, x; t, B)$ is a Borel function of $x$;

(c) for all $0 \leq s < t < \tau$ and $B \in \mathcal{B}(\mathbb{R})$, the Kolmogorov--Chapman equation

$$P(s, x; \tau, B) = \int_{\mathbb{R}} P(s, x; t, dy) \, P(t, y; \tau, B)$$

is satisfied.

Also let $\pi = \pi(\cdot)$ be a probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Then there are a probability space $(\Omega, \mathcal{F}, \mathsf{P})$ and a random process $X = (\xi_t)_{t \geq 0}$ defined on it, such that

$$\mathsf{P}\{\xi_{t_0} \leq x_0, \xi_{t_1} \leq x_1, \ldots, \xi_{t_n} \leq x_n\} = \int_{-\infty}^{x_0} \pi(dy_0) \int_{-\infty}^{x_1} P(0, y_0; t_1, dy_1) \cdots \int_{-\infty}^{x_n} P(t_{n-1}, y_{n-1}; t_n, dy_n)$$

for $0 = t_0 < t_1 < \cdots < t_n$.

The process $X$ so constructed is a Markov process with initial distribution $\pi$ and transition probabilities $\{P(s, x; t, B)\}$.

*Proof.* The finite-dimensional distributions are defined recursively via the transition functions and the initial distribution. For $0 = t_0 < t_1 < \cdots < t_n$, define the measure $\mu_{t_0, t_1, \ldots, t_n}$ on $(\mathbb{R}^{n+1}, \mathcal{B}(\mathbb{R}^{n+1}))$ by

$$\mu_{t_0, t_1, \ldots, t_n}(B) = \int_{\mathbb{R}} \pi(dy_0) \int_{\mathbb{R}} P(0, y_0; t_1, dy_1) \cdots \int_{\mathbb{R}} I_B(y_0, \ldots, y_n) \, P(t_{n-1}, y_{n-1}; t_n, dy_n).$$

The Kolmogorov--Chapman equation (c) guarantees that the resulting family of finite-dimensional distributions $\{\mu_{t_0, \ldots, t_n}\}$ is consistent. By Kolmogorov's Existence Theorem (Theorem 1 of this section), there exists a probability space $(\Omega, \mathcal{F}, \mathsf{P})$ and a stochastic process $(\xi_t)_{t \geq 0}$ with these finite-dimensional distributions.

By construction, the process satisfies the Markov property with the given transition probabilities: the conditional distribution of $\xi_t$ given the past depends only on the most recent value. $\square$
