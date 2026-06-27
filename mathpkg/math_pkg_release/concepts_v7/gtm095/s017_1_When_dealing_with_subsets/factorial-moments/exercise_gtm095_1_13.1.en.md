---
role: exercise
locale: en
chapter: "1"
section: "13"
exercise_number: 11
---

# Exercise 11 (Factorial Moments via Generating Functions)

Let $\xi$ be an integer-valued random variable taking values $0, 1, \ldots$. Define the **factorial moments** (of order $r$) by

$$m_{(r)} = \mathbb{E}\,\xi(\xi - 1) \cdots (\xi - r + 1), \qquad r = 1, 2, \ldots.$$

Show that the quantities $m_{(r)}$ can be obtained from the probability generating function $G_{\xi}(x) = \mathbb{E}\,x^{\xi}$ by the formula

$$m_{(r)} = G_{\xi}^{(r)}(1),$$

where $G_{\xi}^{(r)}$ denotes the $r$-th derivative of $G_{\xi}(x)$.

**Hint.** Differentiate the power series $G_{\xi}(x) = \sum_{k=0}^{\infty} \mathbb{P}(\xi = k) \, x^k$ termwise $r$ times and evaluate at $x = 1$.
