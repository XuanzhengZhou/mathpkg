---
role: proof
locale: en
of_concept: kolmogorov-three-series-theorem
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

For a fixed positive constant $c$, define the truncated functions

$$g_n(x) = \begin{cases} f_n(x) & \text{if } |f_n(x)| \leq c, \\ c & \text{if } |f_n(x)| > c, \end{cases} \qquad h_n(x) = \begin{cases} f_n(x) & \text{if } |f_n(x)| \leq c, \\ -c & \text{if } |f_n(x)| > c. \end{cases}$$

The three series

$$\sum_{n=1}^{\infty} f_n(x), \quad \sum_{n=1}^{\infty} g_n(x), \quad \sum_{n=1}^{\infty} h_n(x)$$

converge at exactly the same points, since $f_n$, $g_n$, and $h_n$ differ only on the set $E_n' = \{x : |f_n(x)| > c\}$, and the a.e. convergence of series (a) (i.e., $\sum \mu(E_n') < \infty$) implies, by the Borel–Cantelli lemma, that $\mu(\limsup E_n') = 0$, so the differences affect at most a null set.

Both $\{g_n\}$ and $\{h_n\}$ are sequences of independent functions uniformly bounded by $c$. Applying Theorem D to $\{g_n\}$ and $\{h_n\}$ separately, the series $\sum g_n(x)$ and $\sum h_n(x)$ converge a.e. if and only if all four series

$$\sum_{n=1}^{\infty} \int g_n \, d\mu, \quad \sum_{n=1}^{\infty} \int h_n \, d\mu, \quad \sum_{n=1}^{\infty} \sigma^2(g_n), \quad \sum_{n=1}^{\infty} \sigma^2(h_n)$$

converge. Computing these integrals in terms of $f_n$ on $E_n$ and $E_n'$:

$$\int g_n \, d\mu = \int_{E_n} f_n \, d\mu + c\,\mu(E_n'), \qquad \int h_n \, d\mu = \int_{E_n} f_n \, d\mu - c\,\mu(E_n'),$$

$$\sigma^2(g_n) = \int_{E_n} f_n^2 \, d\mu + c^2\mu(E_n') - \left( \int_{E_n} f_n \, d\mu + c\,\mu(E_n') \right)^2,$$

$$\sigma^2(h_n) = \int_{E_n} f_n^2 \, d\mu + c^2\mu(E_n') - \left( \int_{E_n} f_n \, d\mu - c\,\mu(E_n') \right)^2.$$

The convergence of these four series is equivalent to the convergence of the three series (a), (b), and (c). The verification uses elementary additions and subtractions, together with the fact that the termwise product of two convergent series, one of which has non-negative terms, is convergent (since the terms of a convergent series are bounded).
