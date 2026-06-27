---
role: proof
locale: en
of_concept: kronecker-second-form
source_book: gtm041
source_chapter: "7"
source_section: "7.5"
---

We apply the first form of Kronecker's theorem to the system $\alpha_1, \ldots, \alpha_n, 0$ and $\theta_1, \ldots, \theta_n, 1$. Since $\theta_1, \ldots, \theta_n, 1$ are linearly independent by hypothesis, Theorem 7.9 yields a real number $t$ and integers $m_1, \ldots, m_n, m_{n+1}$ such that

$$|t\theta_i - m_i - \alpha_i| < \varepsilon \quad (i = 1, \ldots, n)$$

and

$$|t \cdot 1 - m_{n+1} - 0| < \varepsilon.$$

The last inequality gives $|t - m_{n+1}| < \varepsilon$. Taking $k = m_{n+1}$, we have $t$ close to the integer $k$. Substituting $t$ for $k$ introduces an error of at most $|\theta_i| \cdot |t - k| < |\theta_i|\varepsilon$ in each approximation, which can be absorbed by choosing a smaller $\varepsilon$ originally.
