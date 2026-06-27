---
role: proof
locale: en
of_concept: convergence-halfplane-general-dirichlet-series
source_book: gtm041
source_chapter: "8"
source_section: "8.2"
---

**Proof.** First we prove that $L \leq \sigma_0$. Let $A(n)$ denote the partial sums of the coefficients,
$$A(n) = \sum_{k=1}^n a(k).$$

Note that $\lambda(n) > 0$ for all sufficiently large $n$. If we prove that for every $\varepsilon > 0$,
$$\log|A(n)| \leq (\sigma_0 + \varepsilon)\lambda(n) + O(1)$$
then $L \leq \sigma_0$ will follow. To compare $A(n)$ with the partial sums
$$S(n) = \sum_{k=1}^n a(k)e^{-s_0\lambda(k)}$$
the $S(n)$ are bounded since the series $\sum_{k=1}^\infty a(k)e^{-s_0\lambda(k)}$ converges. Suppose that $|S(n)| < M$ for all $n$. To express $A(n)$ in terms of the $S(n)$ we use partial summation:
$$A(n) = \sum_{k=1}^n a(k) = \sum_{k=1}^n a(k)e^{-s_0\lambda(k)}e^{s_0\lambda(k)} = \sum_{k=1}^n \{S(k) - S(k-1)\}e^{s_0\lambda(k)},$$
provided $S(0) = 0$. Thus
$$A(n) = \sum_{k=1}^n S(k)e^{s_0\lambda(k)} - \sum_{k=1}^{n-1} S(k)e^{s_0\lambda(k+1)}$$
$$= \sum_{k=1}^{n-1} S(k)\bigl\{e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}\bigr\} + S(n)e^{s_0\lambda(n)}.$$

Hence
$$|A(n)| < M \sum_{k=1}^{n-1}\bigl|e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}\bigr| + M e^{\sigma_0\lambda(n)}.$$

But
\begin{align*}
\sum_{k=1}^{n-1}\bigl|e^{s_0\lambda(k)} - e^{s_0\lambda(k+1)}\bigr| &= \sum_{k=1}^{n-1}\left|s_0 \int_{\lambda(k)}^{\lambda(k+1)} e^{s_0u}\,du\right| \\
&\leq |s_0| \sum_{k=1}^{n-1}\int_{\lambda(k)}^{\lambda(k+1)} e^{\sigma_0 u}\,du \\
&= |s_0| \int_{\lambda(1)}^{\lambda(n)} e^{\sigma_0 u}\,du = \frac{|s_0|}{\sigma_0}\bigl(e^{\sigma_0\lambda(n)} - e^{\sigma_0\lambda(1)}\bigr).
\end{align*}

Thus
$$|A(n)| < M\cdot\frac{|s_0|}{\sigma_0}\bigl(e^{\sigma_0\lambda(n)} - e^{\sigma_0\lambda(1)}\bigr) + M e^{\sigma_0\lambda(n)} < C e^{\sigma_0\lambda(n)}$$
where $C$ is a constant depending only on $M$, $s_0$, and $\sigma_0$. This gives
$$\frac{\log|A(n)|}{\lambda(n)} < \sigma_0 + \frac{\log C}{\lambda(n)}$$
so the limsup is $\leq \sigma_0$, proving the first part.

Now we prove convergence. Again we use partial summation to compare it to the partial sums $A(n) = \sum_{k=1}^n a(k)$. We have
\begin{align*}
\sum_{n=a}^{b} a(n)e^{-s\lambda(n)} &= \sum_{n=a}^{b} \{A(n) - A(n-1)\} e^{-s\lambda(n)} \\
&= \sum_{n=a}^{b} A(n) \bigl\{e^{-s\lambda(n)} - e^{-s\lambda(n+1)}\bigr\} + A(b) e^{-s\lambda(b+1)} - A(a-1) e^{-s\lambda(a)}.
\end{align*}

This relation holds for any choice of $s$, $a$ and $b$. Now suppose $s$ is any complex number with $\sigma > L$. Let $\varepsilon = \frac{1}{2}(\sigma - L)$. Then $\varepsilon > 0$ and $\sigma = L + 2\varepsilon$. By the definition of $L$, for this $\varepsilon$ there is an integer $N(\varepsilon)$ such that for all $n \geq N(\varepsilon)$ we have
$$\frac{\log|A(n)|}{\lambda(n)} < L + \varepsilon.$$

We can also assume that $\lambda(n) > 0$ for $n \geq N(\varepsilon)$. Hence
$$|A(n)| < e^{(L+\varepsilon)\lambda(n)} \quad\text{for all } n \geq N(\varepsilon).$$

If we choose $b \geq a > N(\varepsilon)$ we get the estimate
\begin{align*}
\Bigl|\sum_{n=a}^{b} a(n)e^{-s\lambda(n)}\Bigr| &\leq \sum_{n=a}^{b} e^{(L+\varepsilon)\lambda(n)} \bigl|e^{-s\lambda(n)} - e^{-s\lambda(n+1)}\bigr| \\
&\quad + e^{(L+\varepsilon)\lambda(b+1)} e^{-\sigma\lambda(b+1)} + e^{(L+\varepsilon)\lambda(a)} e^{-\sigma\lambda(a)}.
\end{align*}

The last two terms are $e^{-\varepsilon\lambda(b+1)} + e^{-\varepsilon\lambda(a)}$ since $L + \varepsilon - \sigma = -\varepsilon$. For the sum, we use the same integral estimate as before:
\begin{align*}
\sum_{n=a}^{b} e^{(L+\varepsilon)\lambda(n)} \bigl|e^{-s\lambda(n)} - e^{-s\lambda(n+1)}\bigr| &\leq \sum_{n=a}^{b} \bigl|e^{-(\sigma - L - \varepsilon)\lambda(n)} - e^{-(\sigma - L - \varepsilon)\lambda(n+1)}\bigr| \\
&= \sum_{n=a}^{b} \bigl|e^{-\varepsilon\lambda(n)} - e^{-\varepsilon\lambda(n+1)}\bigr| \cdot e^{-(\sigma - L - 2\varepsilon)\lambda(n)} \\
&\leq \int_{\lambda(a)}^{\lambda(b+1)} \varepsilon e^{-\varepsilon u}\,du = e^{-\varepsilon\lambda(a)} - e^{-\varepsilon\lambda(b+1)}.
\end{align*}

Each term on the right tends to $0$ as $a \to \infty$, so the Cauchy criterion shows that the series converges for all $s$ with $\sigma > L$. This completes the proof. Note also that this proves uniform convergence on any compact subset of the half-plane $\sigma > L$.
