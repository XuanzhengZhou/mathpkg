---
role: proof
locale: en
of_concept: factorial-moments-generating-function
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Factorial Moments via Generating Functions

**Theorem.** Let $\xi$ be an integer-valued random variable taking values $0, 1, 2, \dots$ with probability generating function

$$G_{\xi}(x) = \mathbb{E}\, x^{\xi} = \sum_{k=0}^{\infty} \mathbb{P}(\xi = k) \, x^k, \qquad |x| \leq 1.$$

Define the **factorial moments** of order $r$ ($r = 1, 2, \dots$) by

$$m_{(r)} = \mathbb{E}\bigl[\xi(\xi - 1) \cdots (\xi - r + 1)\bigr].$$

Then the factorial moments can be obtained from the generating function by differentiation:

$$m_{(r)} = G_{\xi}^{(r)}(1),$$

where $G_{\xi}^{(r)}$ denotes the $r$-th derivative of $G_{\xi}(x)$.

---

**Proof.** The generating function is a power series:

$$G_{\xi}(x) = \sum_{k=0}^{\infty} p_k \, x^k, \qquad p_k = \mathbb{P}(\xi = k).$$

Since the series converges for $|x| \leq 1$, we may differentiate termwise inside the radius of convergence. The $r$-th derivative is

$$G_{\xi}^{(r)}(x) = \frac{d^r}{dx^r} \sum_{k=0}^{\infty} p_k \, x^k = \sum_{k=r}^{\infty} p_k \cdot k(k-1) \cdots (k-r+1) \, x^{k-r}.$$

The terms for $k = 0, 1, \dots, r-1$ vanish because the $r$-th derivative of $x^k$ is zero when $k < r$.

Evaluating at $x = 1$:

$$G_{\xi}^{(r)}(1) = \sum_{k=r}^{\infty} p_k \cdot k(k-1) \cdots (k-r+1) \cdot 1^{k-r} = \sum_{k=r}^{\infty} p_k \cdot k(k-1) \cdots (k-r+1).$$

For $k < r$, the product $k(k-1)\cdots(k-r+1)$ contains a factor of $0$, so we may extend the summation to all $k \geq 0$ without changing the value:

$$G_{\xi}^{(r)}(1) = \sum_{k=0}^{\infty} p_k \cdot k(k-1) \cdots (k-r+1) = \mathbb{E}\bigl[\xi(\xi - 1) \cdots (\xi - r + 1)\bigr] = m_{(r)}.$$

Thus $m_{(r)} = G_{\xi}^{(r)}(1)$. $\square$

**Remarks.**

1. For $r = 1$: $m_{(1)} = G_{\xi}'(1) = \mathbb{E}\,\xi$, the ordinary expectation.

2. For $r = 2$: $m_{(2)} = G_{\xi}''(1) = \mathbb{E}[\xi(\xi - 1)] = \mathbb{E}\,\xi^2 - \mathbb{E}\,\xi$, from which the variance can be recovered: $\operatorname{Var}(\xi) = m_{(2)} + m_{(1)} - m_{(1)}^2$.

3. The factorial moments are particularly useful for distributions whose generating functions have a simple closed form (e.g., binomial, Poisson), as they avoid the need to compute raw moments $\mathbb{E}\,\xi^r$ directly.
