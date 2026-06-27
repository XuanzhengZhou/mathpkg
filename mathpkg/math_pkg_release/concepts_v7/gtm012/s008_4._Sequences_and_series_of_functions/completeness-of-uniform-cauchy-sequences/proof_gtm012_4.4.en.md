---
role: proof
locale: en
of_concept: completeness-of-uniform-cauchy-sequences
source_book: gtm012
source_chapter: "4"
source_section: "4. Sequences and series of functions"
---

# Proof of Theorem 4.1: Completeness of the space of bounded functions under uniform convergence; continuity of the uniform limit

**Theorem 4.1.** Suppose $(f_n)_{n=1}^{\infty}$ is a sequence of bounded functions from a set $S$ to $\mathbb{C}$ which is a uniform Cauchy sequence. Then there is a unique bounded function $f: S \to \mathbb{C}$ such that $(f_n)_{n=1}^{\infty}$ converges uniformly to $f$. If $S$ is a metric space and each $f_n$ is continuous, then $f$ is continuous.

*Proof.* For each $x \in S$, we have

$$|f_n(x) - f_m(x)| \leq \|f_n - f_m\|_{\infty} = \sup_{y \in S} |f_n(y) - f_m(y)|.$$

Therefore $(f_n(x))_{n=1}^{\infty}$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, the limit

$$f(x) = \lim_{n \to \infty} f_n(x)$$

exists for each $x \in S$. This defines a function $f: S \to \mathbb{C}$, and by construction $f_n(x) \to f(x)$ pointwise.

We now show that $f$ is bounded. Since $(f_n)$ is a uniform Cauchy sequence, for any $\varepsilon > 0$ there exists $N$ such that

$$\|f_n - f_m\|_{\infty} < \varepsilon \quad \text{whenever } n, m \geq N.$$

For any $x \in S$ and any $m \geq N$, taking the limit as $n \to \infty$ in the inequality

$$|f_n(x)| \leq |f_n(x) - f_m(x)| + |f_m(x)| \leq \varepsilon + \|f_m\|_{\infty}$$

yields $|f(x)| \leq \varepsilon + \|f_m\|_{\infty}$. Hence $\|f\|_{\infty} \leq \varepsilon + \|f_m\|_{\infty}$, so $f$ is bounded.

To prove uniform convergence, fix $\varepsilon > 0$ and choose $N$ as above. For any $x \in S$ and $n, m \geq N$,

$$|f_n(x) - f(x)| \leq |f_n(x) - f_m(x)| + |f_m(x) - f(x)|.$$

Given $x$ and $n \geq N$, we may choose $m \geq N$ (which may depend on $x$) such that $|f_m(x) - f(x)| < \varepsilon$. Then

$$|f_n(x) - f(x)| < \varepsilon + \varepsilon = 2\varepsilon.$$

Thus $\|f_n - f\|_{\infty} \leq 2\varepsilon$ for $n \geq N$, proving uniform convergence.

Now suppose $S$ is a metric space and each $f_n$ is continuous. Let $x \in S$ and $\varepsilon > 0$. Choose $N$ such that $\|f - f_N\|_{\infty} < \varepsilon$. By continuity of $f_N$, choose $\delta > 0$ such that

$$|f_N(y) - f_N(x)| < \varepsilon \quad \text{if } d(y, x) < \delta.$$

Then for $d(y, x) < \delta$,

$$
\begin{aligned}
|f(y) - f(x)|
&\leq |f(y) - f_N(y)| + |f_N(y) - f_N(x)| + |f_N(x) - f(x)| \\
&\leq \|f - f_N\|_{\infty} + |f_N(y) - f_N(x)| + \|f - f_N\|_{\infty} \\
&< \varepsilon + \varepsilon + \varepsilon = 3\varepsilon.
\end{aligned}
$$

Thus $f$ is continuous at $x$. $\square$
