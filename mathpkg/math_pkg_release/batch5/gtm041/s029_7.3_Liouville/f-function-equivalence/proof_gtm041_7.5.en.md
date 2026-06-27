---
role: proof
locale: en
of_concept: f-function-equivalence
source_book: gtm041
source_chapter: "7"
source_section: "7.5"
---

Each term of the sum in the definition of $F(t)$ has absolute value 1 so $|F(t)| \leq n + 1$.

If (a) holds then each number $t\theta_r - \alpha_r$ is nearly an integer, hence each exponential in $F(t)$ is nearly 1, so $|F(t)|$ is nearly $n+1$. Therefore $L \geq n+1$. Since $L \leq n+1$ this proves (b).

Now assume (a) is false and show that (b) is also false. If (a) is false there exists an $\varepsilon > 0$ such that for all integers $h_1, \ldots, h_n$ and all real $t$ there is a $k$, $1 \leq k \leq n$, such that

$$|t\theta_k - \alpha_k - h_k| \geq \frac{\varepsilon}{2\pi}.$$

(We can also assume that $\varepsilon \leq \pi/4$ because if (a) is false for $\varepsilon$ it is also false for every smaller $\varepsilon$.) Let $x_r = t\theta_r - \alpha_r - h_r$. Then $|2\pi x_k| \geq \varepsilon$, so the point $1 + e^{2\pi ix_k}$ lies on the circle of radius 1 about 1 but outside the shaded sector.

Now $|1 + e^{i\varepsilon}| < 2$ so $|1 + e^{i\varepsilon}| = 2 - \delta$ for some $\delta > 0$. Hence

$$|1 + e^{2\pi ix_k}| \leq |1 + e^{i\varepsilon}| = 2 - \delta,$$

so

$$|F(t)| = \left|1 + \sum_{r=1}^{n} e^{2\pi ix_r}\right| \leq |1 + e^{2\pi ix_k}| + \sum_{\substack{r=1 \\ r \neq k}}^{n} |e^{2\pi ix_r}|$$

$$\leq (2 - \delta) + (n - 1) = n + 1 - \delta.$$

Since this is true for all $t$ we must have $L \leq n + 1 - \delta < n + 1$, contradicting (b).
