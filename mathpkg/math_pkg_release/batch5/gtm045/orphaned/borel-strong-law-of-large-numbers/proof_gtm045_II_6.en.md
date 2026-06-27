---
role: proof
locale: en
of_concept: borel-strong-law-of-large-numbers
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "6. Elementary random variables"
---
Let $X_n = S_n/n$. Then $EX_n = p$, $\sigma^2 X_n = pq/n$. Since for every $m$,

$$\sum_{k=1}^{\infty} P\left[|X_{k^2} - p| \geq \frac{1}{m}\right] \leq m^2 pq \sum_{k=1}^{\infty} \frac{1}{k^2} < \infty,$$

it follows by the summable tail proposition that $X_{k^2} \to p$ with probability 1 as $k \to \infty$. To every $n$ there corresponds an integer $k = k(n)$ with $k^2 \leq n < (k+1)^2$. Since

$$|X_n - X_{k^2}| = \left|\left(\frac{1}{n} - \frac{1}{k^2}\right)\sum_{j=1}^{k^2} I_{A_j} + \frac{1}{n}\sum_{j=k^2+1}^{n} I_{A_j}\right| \leq \frac{(n-k^2)k^2}{n k^2} + \frac{n-k^2}{n} \leq \frac{4}{k},$$

we have $|X_n - p| \leq |X_n - X_{k^2}| + |X_{k^2} - p| \leq \frac{4}{k} + |X_{k^2} - p|$. Thus $X_n \to p$ with probability 1 as $n \to \infty$.
