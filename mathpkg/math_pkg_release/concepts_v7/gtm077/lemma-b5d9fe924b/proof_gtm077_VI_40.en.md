---
role: proof
locale: en
of_concept: lemma-b5d9fe924b
source_book: gtm077
source_chapter: "VI"
source_section: "40"
---
# Proof of Lemma (b): Convergence Criterion for Dirichlet Series

**Lemma (b).** Let us set

$$S(m) = a_1 + a_2 + \cdots + a_m; \quad \text{hence } a_n = S(n) - S(n - 1).$$

If there exists a number $\sigma$ ($\sigma > 0$) for which the quotient

$$\left| \frac{S(m)}{m^\sigma} \right| < A, \quad (m = 1, 2, \ldots) \tag{91}$$

where $A$ is a constant independent of $m$, then the series $\sum_{n=1}^{\infty} a_n/n^s$ converges for $s > \sigma$ and represents a continuous function of $s$.

*Proof.* For all positive integers $m$ and $h$, we apply partial summation (Abel summation):

$$\begin{aligned}
\sum_{n=m}^{m+h} \frac{a_n}{n^s} &= \sum_{n=m}^{m+h} \frac{S(n) - S(n-1)}{n^s} \\
&= \frac{S(m+h)}{(m+h)^s} + \sum_{n=m}^{m+h-1} S(n) \left( \frac{1}{n^s} - \frac{1}{(n+1)^s} \right) - \frac{S(m-1)}{m^s}.
\end{aligned}$$

Using the bound $|S(n)| < A n^\sigma$ from hypothesis (91), we estimate:

$$\begin{aligned}
\left| \sum_{n=m}^{m+h} \frac{a_n}{n^s} \right|
&< A (m+h)^{\sigma - s} + A \sum_{n=m}^{m+h-1} n^\sigma \left( \frac{1}{n^s} - \frac{1}{(n+1)^s} \right) + A m^{\sigma - s} \\
&< 2A m^{\sigma - s} + A s \sum_{n=m}^{m+h-1} \frac{n^\sigma}{n^{s+1}} \\
&= 2A m^{\sigma - s} + A s \sum_{n=m}^{m+h-1} \frac{1}{n^{s-\sigma+1}}.
\end{aligned}$$

For $s > \sigma$, the series $\sum_{n=1}^{\infty} 1/n^{s-\sigma+1}$ converges (since the exponent $s - \sigma + 1 > 1$). Therefore the tail sum can be made arbitrarily small for sufficiently large $m$, independently of $h$. By the Cauchy criterion, the series $\sum_{n=1}^{\infty} a_n/n^s$ converges for $s > \sigma$.

Moreover, the convergence is uniform in each interval $\sigma + \delta \leq s \leq \sigma + \delta'$ (where $\delta' > \delta > 0$), since the estimates above depend continuously on $s$ and the bounds hold uniformly in such an interval. Therefore the series represents a continuous function of $s$ for $s > \sigma$. $\square$
