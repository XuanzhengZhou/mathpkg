---
role: proof
locale: en
of_concept: polygonal-approximation-lemma
source_book: gtm011
source_chapter: "1"
source_section: "1.19"
---

**Case I.** $G$ is a disk. Since $\{\gamma\}$ is compact, there is $r > 0$ such that $B(\gamma(t); r) \subset G$ for all $t \in [a, b]$. By uniform continuity of $f$ on the compact set $\overline{B(\{\gamma\}; r)}$, choose $\epsilon > 0$ and the corresponding $\delta_2$ from the definition of the line integral.

Choose a partition $P = \{t_0 < t_1 < \ldots < t_n\}$ of $[a, b]$ such that $\|P\| < \delta_2$ and the approximating Riemann-Stieltjes sum satisfies the usual closeness condition. Define $\Gamma$ as the polygonal path with vertices $\gamma(t_0), \gamma(t_1), \ldots, \gamma(t_n)$, i.e., on $[t_{k-1}, t_k]$,

$$\Gamma(t) = \frac{t_k - t}{t_k - t_{k-1}} \gamma(t_{k-1}) + \frac{t - t_{k-1}}{t_k - t_{k-1}} \gamma(t_k).$$

Then $|\Gamma(t) - \gamma(\tau_k)| < \delta$ for $t_{k-1} \leq t \leq t_k$, where $\tau_k$ are the sample points.

Since $\int_{\Gamma} f = \int_a^b f(\Gamma(t)) \Gamma'(t) dt$, we have

$$\int_{\Gamma} f = \sum_{k=1}^{n} \frac{\gamma(t_k) - \gamma(t_{k-1})}{t_k - t_{k-1}} \int_{t_{k-1}}^{t_k} f(\Gamma(t)) dt.$$

Estimating the difference:

$$\left| \int_{\gamma} f - \int_{\Gamma} f \right| \leq \epsilon + \sum_{k=1}^{n} |\gamma(t_k) - \gamma(t_{k-1})| (t_k - t_{k-1})^{-1} \int_{t_{k-1}}^{t_k} |f(\Gamma(t)) - f(\gamma(\tau_k))| dt.$$

Applying the uniform continuity bound to the integrand gives

$$\left| \int_{\gamma} f - \int_{\Gamma} f \right| \leq \epsilon + \epsilon \sum_{k=1}^{n} |\gamma(t_k) - \gamma(t_{k-1})| \leq \epsilon(1 + V(\gamma)).$$

Since $\epsilon > 0$ can be made arbitrarily small, the result follows for Case I.

**Case II.** $G$ is arbitrary. Since $\{\gamma\}$ is compact, there exists $r$ with $0 < r < \text{dist}(\{\gamma\}, \partial G)$. Choose $\delta > 0$ such that $|\gamma(s) - \gamma(t)| < r$ when $|s - t| < \delta$. If $P = \{t_0 < t_1 < \ldots < t_n\}$ is a partition of $[a, b]$ with $\|P\| < \delta$, then the polygonal path $\Gamma$ connecting the points $\gamma(t_0), \gamma(t_1), \ldots, \gamma(t_n)$ lies entirely within $G$, since each segment connecting $\gamma(t_{k-1})$ to $\gamma(t_k)$ has length less than $r$ and hence stays within a disk of radius $r$ around $\gamma(t_{k-1})$, which is contained in $G$. The estimation then proceeds as in Case I.
