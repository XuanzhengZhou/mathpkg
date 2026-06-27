---
role: proof
locale: en
of_concept: independent-sets-borel-cantelli
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

Let $\chi_n$ be the characteristic function of $E_n$, so $\chi_n$ are independent functions with $|\chi_n(x)| \leq 1$ a.e. Note that

$$\int \chi_n \, d\mu = \mu(E_n), \quad \sigma^2(\chi_n) = \mu(E_n)(1 - \mu(E_n)).$$

Since $\sum \mu(E_n) < \infty$, the series $\sum \mu(E_n)(1 - \mu(E_n)) \leq \sum \mu(E_n) < \infty$ and $\sum \int \chi_n \, d\mu = \sum \mu(E_n) < \infty$. By Theorem D (since the $\chi_n$ are uniformly bounded by $1$), the series $\sum \chi_n(x)$ converges a.e.

Now, $x \in \limsup E_n$ if and only if $x$ belongs to infinitely many $E_n$, which is equivalent to $\sum \chi_n(x) = \infty$. Since $\sum \chi_n(x)$ converges a.e., it is finite a.e., so $\mu(\limsup E_n) = 0$.

Conversely, if $\mu(\limsup E_n) = 0$, then $\sum \chi_n(x)$ converges a.e. (both $\{E_n\}$ and hence $\{\chi_n\}$ are independent). By Theorem D, the series $\sum \int \chi_n \, d\mu = \sum \mu(E_n)$ must converge. (If it diverged, then since $\sum \sigma^2(\chi_n) = \sum \mu(E_n)(1 - \mu(E_n)) \leq \sum \mu(E_n)$, the divergence of $\sum \mu(E_n)$ together with Theorem D would contradict the a.e. convergence.)
