---
role: proof
locale: en
of_concept: rademacher-series-convergence
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

The Rademacher functions $f_n$ are independent, satisfy $|f_n(x)| = 1$ a.e., $\int f_n \, d\mu = 0$, and $\sigma^2(f_n) = 1$. Define $g_n(x) = c_n f_n(x)$. Then the $g_n$ are independent, uniformly bounded by $\sup |c_n|$ (and certainly bounded by any constant exceeding all $|c_n|$ if the $c_n$ are bounded; otherwise we apply Theorem E / truncation).

More directly, since $|g_n(x)| = |c_n|$, we may apply Theorem D immediately when the $c_n$ are bounded. In general, we apply Kolmogorov's Three Series Theorem (Theorem E). Since $|g_n(x)| = |c_n|$, we have:

For a fixed $c > 0$: $\mu(|g_n| > c) = 1$ if $|c_n| > c$, and $0$ otherwise. For the series (a) to converge, we need $|c_n| \leq c$ for all but finitely many $n$.

The truncated integrals are $\int g_n \, d\mu = 0$ for all $n$, so series (b) converges trivially. The truncated second moments give $\int g_n^2 \, d\mu = c_n^2$. So series (c) reduces to $\sum c_n^2$, and the convergence of all three series is equivalent to $\sum c_n^2 < \infty$.
