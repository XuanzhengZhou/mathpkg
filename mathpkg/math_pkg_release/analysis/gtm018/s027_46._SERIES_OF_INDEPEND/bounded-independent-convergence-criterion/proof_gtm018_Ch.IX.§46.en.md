---
role: proof
locale: en
of_concept: bounded-independent-convergence-criterion
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

**Sufficiency ("if"):** Define $g_n(x) = f_n(x) - \int f_n \, d\mu$ for $n = 1, 2, \dots$. Then $\int g_n \, d\mu = 0$, $|g_n(x)| \leq 2c$ a.e., and $\sigma^2(g_n) = \sigma^2(f_n)$. Since $\sum \sigma^2(f_n) < \infty$, Theorem B implies that $\sum g_n(x)$ converges a.e. Since $\sum \int f_n \, d\mu$ converges (as a numerical series), adding the constant terms gives the a.e. convergence of $\sum f_n(x)$.

**Necessity ("only if"):** Assume $\sum f_n(x)$ converges a.e. Consider the Cartesian product $X \times X$ with the product measure $\mu \times \mu$, and define

$$h_n(x,y) = f_n(x) - f_n(y), \quad n = 1, 2, \dots.$$

The functions $h_n$ are independent on the product space. Since $\sum f_n(x)$ converges a.e., it follows that $\sum h_n(x,y)$ converges a.e. on $X \times X$. Moreover, $\int h_n \, d(\mu \times \mu) = 0$ and $\int h_n^2 \, d(\mu \times \mu) < \infty$ (since the $f_n$ are bounded). By Theorem C, convergence on a set of positive measure implies

$$\sum_{n=1}^{\infty} \sigma^2(h_n) < \infty.$$

Since $\sigma^2(h_n) = 2\sigma^2(f_n)$, we obtain $\sum_{n=1}^{\infty} \sigma^2(f_n) < \infty$.

Now $\sigma^2(g_n) = \sigma^2(f_n)$, so Theorem B implies $\sum g_n(x)$ converges a.e. Since $f_n(x) = g_n(x) + \int f_n \, d\mu$ and $\sum f_n(x)$ converges a.e., the numerical series $\sum \int f_n \, d\mu$ must also converge.
