---
role: proof
locale: en
of_concept: macmillan
source_book: gtm095
source_chapter: "1"
source_section: "4"
---

# Proof of Theorem (Macmillan)

**Theorem** (Macmillan). Let $p_i > 0$, $i = 1, \ldots, r$, $\sum_{i=1}^r p_i = 1$, and $0 < \varepsilon < 1$. Let $H = -\sum_{i=1}^r p_i \log p_i$. Then there exists an $n_0 = n_0(\varepsilon; p_1, \ldots, p_r)$ such that for all $n > n_0$

(a) $e^{n(H-\varepsilon)} < N(C(n, \varepsilon)) < e^{n(H+\varepsilon)}$,

(b) $e^{-n(H+\varepsilon)} < p(\omega) < e^{-n(H-\varepsilon)}$ for all $\omega \in C(n, \varepsilon)$,

where $C(n, \varepsilon) = \{\omega : |v_i(\omega)/n - p_i| < \varepsilon,\ i = 1, \ldots, r\}$ and $v_i(\omega)$ is the number of occurrences of the symbol $i$ in the sequence $\omega = (a_1, \ldots, a_n)$.

**Proof.** Put

$$\varepsilon_1 = \varepsilon \left( -\sum_{k=1}^{r} \log p_k \right)^{-1}.$$

Then if $\omega \in C(n, \varepsilon_1)$, we have $|v_i(\omega)/n - p_i| < \varepsilon_1$ for all $i = 1, \ldots, r$, and consequently

$$
\begin{aligned}
\left| \sum_{k=1}^{r} \left( -\frac{v_k(\omega)}{n} \log p_k \right) - H \right|
&= \left| \sum_{k=1}^{r} \left( -\frac{v_k(\omega)}{n} \log p_k \right) - \sum_{k=1}^{r} (-p_k \log p_k) \right| \\
&\leq \sum_{k=1}^{r} \left| \frac{v_k(\omega)}{n} - p_k \right| (-\log p_k) \\
&< \varepsilon_1 \left( -\sum_{k=1}^{r} \log p_k \right) = \varepsilon.
\end{aligned}
$$

Thus for $\omega \in C(n, \varepsilon_1)$,

$$H - \varepsilon < \sum_{k=1}^{r} \left( -\frac{v_k(\omega)}{n} \log p_k \right) < H + \varepsilon.$$

Since

$$p(\omega) = p_1^{v_1(\omega)} \cdots p_r^{v_r(\omega)} = \exp\left\{ -n \sum_{k=1}^{r} \left( -\frac{v_k(\omega)}{n} \log p_k \right) \right\},$$

we obtain, for $\omega \in C(n, \varepsilon_1)$,

$$e^{-n(H+\varepsilon)} < p(\omega) < e^{-n(H-\varepsilon)}. \tag{1}$$

Now we estimate $N(C(n, \varepsilon_1))$, the number of elements in $C(n, \varepsilon_1)$. First note the elementary bounds

$$P(C(n, \varepsilon_1)) \geq N(C(n, \varepsilon_1)) \cdot \min_{\omega \in C(n, \varepsilon_1)} p(\omega),$$

$$P(C(n, \varepsilon_1)) \leq N(C(n, \varepsilon_1)) \cdot \max_{\omega \in C(n, \varepsilon_1)} p(\omega).$$

From (1) we have $\min_{\omega \in C} p(\omega) > e^{-n(H+\varepsilon)}$ and $\max_{\omega \in C} p(\omega) < e^{-n(H-\varepsilon)}$, so

$$N(C(n, \varepsilon_1)) \leq \frac{P(C(n, \varepsilon_1))}{\min_{\omega \in C(n, \varepsilon_1)} p(\omega)} < \frac{1}{e^{-n(H + \varepsilon)}} = e^{n(H + \varepsilon)},$$

and similarly

$$N(C(n, \varepsilon_1)) \geq \frac{P(C(n, \varepsilon_1))}{\max_{\omega \in C(n, \varepsilon_1)} p(\omega)} > P(C(n, \varepsilon_1)) \, e^{n(H - \varepsilon)}.$$

Since $P(C(n, \varepsilon_1)) \to 1$ as $n \to \infty$ (by the law of large numbers applied to the indicator variables $\xi_k^{(i)}(\omega) = 1_{\{a_k = i\}}$), there exists $n_1$ such that $P(C(n, \varepsilon_1)) > 1 - \varepsilon$ for $n > n_1$. Therefore

$$N(C(n, \varepsilon_1)) \geq (1 - \varepsilon) \exp\{n(H - \varepsilon)\} = \exp\{n(H - \varepsilon) + \log(1 - \varepsilon)\}.$$

Let $n_2$ be such that $n\varepsilon + \log(1 - \varepsilon) > 0$ for $n > n_2$ (possible since $\log(1-\varepsilon)$ is fixed and $n\varepsilon \to \infty$). Then for $n \geq n_0 = \max(n_1, n_2)$ we obtain

$$N(C(n, \varepsilon_1)) \geq e^{n(H - 2\varepsilon)}.$$

Replacing $\varepsilon$ by $\varepsilon/2$ throughout yields the symmetric bounds

$$e^{n(H-\varepsilon)} < N(C(n, \varepsilon)) < e^{n(H+\varepsilon)},$$

$$e^{-n(H+\varepsilon)} < p(\omega) < e^{-n(H-\varepsilon)} \quad (\omega \in C(n, \varepsilon)),$$

for all $n > n_0(\varepsilon/2; p_1, \ldots, p_r)$.

This completes the proof of the theorem. $\square$
