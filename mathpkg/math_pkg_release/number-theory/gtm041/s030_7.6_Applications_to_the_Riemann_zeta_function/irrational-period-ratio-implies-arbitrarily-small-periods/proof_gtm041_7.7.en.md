---
role: proof
locale: en
of_concept: irrational-period-ratio-implies-arbitrarily-small-periods
source_book: gtm041
source_chapter: "7"
source_section: "7.7"
---

Since $\omega_2/\omega_1$ is irrational, we can apply Kronecker's theorem (or Dirichlet's approximation theorem). Choose any $\varepsilon > 0$. By the one-dimensional Kronecker approximation theorem applied to the number $\omega_2/\omega_1$, there exist integers $k$ and $h$ with $k > 0$ such that
$$\left| k\frac{\omega_2}{\omega_1} - h \right| < \frac{\varepsilon}{|\omega_1|}.$$

Multiplying by $|\omega_1|$, we obtain
$$|k\omega_2 - h\omega_1| < \varepsilon.$$

Now $\omega = k\omega_2 - h\omega_1$ is a period of $f$ (since it is an integer linear combination of the periods $\omega_1$ and $\omega_2$) that satisfies $|\omega| < \varepsilon$. Moreover, $\omega \neq 0$ because $\omega_2/\omega_1$ is irrational, which precludes the equality $k\omega_2 = h\omega_1$. Hence $f$ has arbitrarily small nonzero periods.
