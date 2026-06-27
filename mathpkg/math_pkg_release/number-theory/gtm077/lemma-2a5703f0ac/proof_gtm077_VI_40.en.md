---
role: proof
locale: en
of_concept: lemma-2a5703f0ac
source_book: gtm077
source_chapter: "VI"
source_section: "40"
---
# Proof of Lemma (c): Limit Relation for Dirichlet Series

**Lemma (c).** If in the notation of Lemma (b)

$$\lim_{m \to \infty} \frac{S(m)}{m} = c,$$

then, if $s$ approaches 1 (from $s > 1$),

$$\lim_{s \to 1^+} (s - 1) \sum_{n=1}^{\infty} \frac{a_n}{n^s} = c.$$

*Proof.* By Lemma (b) with $\sigma = 1$, the series converges for $s > 1$. Let us set

$$S(n) = cn + \varepsilon_n n,$$

where $\lim_{n \to \infty} \varepsilon_n = 0$ by hypothesis. Define

$$\varphi(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s}.$$

Then, applying partial summation as in Lemma (b), we have for $s > 1$:

$$\begin{aligned}
\left| \varphi(s) - c\zeta(s) \right|
&= \left| \sum_{n=1}^{\infty} \frac{a_n - c}{n^s} \right| \\
&= s \left| \sum_{n=1}^{\infty} n \varepsilon_n \int_{n}^{n+1} \frac{dx}{x^{s+1}} \right| \\
&< s \sum_{n=1}^{\infty} |\varepsilon_n| \int_{n}^{n+1} \frac{dx}{x^s}.
\end{aligned}$$

For an arbitrary $\delta > 0$, choose an integer $N$ such that $|\varepsilon_n| < \delta$ for all $n \geq N$ (possible since $\varepsilon_n \to 0$). Choose $C$ such that $|\varepsilon_n| < C$ for all $n$ (the sequence is bounded). Then:

$$\begin{aligned}
\left| (s - 1)\varphi(s) - c(s - 1)\zeta(s) \right|
&< C s (s - 1) \sum_{n=1}^{N-1} \int_{n}^{n+1} \frac{dx}{x^s} + \delta s (s - 1) \sum_{n=N}^{\infty} \int_{n}^{n+1} \frac{dx}{x^s} \\
&= C s (s - 1) \int_{1}^{N} \frac{dx}{x^s} + \delta s (s - 1) \int_{N}^{\infty} \frac{dx}{x^s}.
\end{aligned}$$

As $s \to 1^+$, the first term tends to $0$ (the factor $(s-1)$ vanishes, while $\int_1^N dx/x^s$ remains bounded). The second term satisfies:

$$\delta s (s - 1) \int_{N}^{\infty} \frac{dx}{x^s} = \delta s (s - 1) \frac{N^{1-s}}{s - 1} = \delta s N^{1-s} \to \delta.$$

Therefore:

$$\limsup_{s \to 1^+} \left| (s - 1)\varphi(s) - c(s - 1)\zeta(s) \right| \leq \delta.$$

Since $\delta > 0$ was arbitrary, it follows that

$$\lim_{s \to 1^+} \left( (s - 1)\varphi(s) - c(s - 1)\zeta(s) \right) = 0.$$

By Lemma (a), $\lim_{s \to 1^+} (s - 1)\zeta(s) = 1$, and therefore:

$$\lim_{s \to 1^+} (s - 1)\varphi(s) = c \cdot 1 = c.$$

This completes the proof. $\square$
