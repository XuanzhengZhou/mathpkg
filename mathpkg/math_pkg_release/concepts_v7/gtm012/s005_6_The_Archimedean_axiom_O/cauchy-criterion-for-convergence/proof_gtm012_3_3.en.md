---
role: proof
locale: en
of_concept: cauchy-criterion-for-convergence
source_book: gtm012
source_chapter: "3"
source_section: "3. Sequences of real and complex numbers"
---

# Proof of Cauchy criterion for convergence in $\mathbb{C}$ and $\mathbb{R}$ (Theorem 3.3)

**Theorem 3.3.** A sequence in $\mathbb{C}$ (or $\mathbb{R}$) converges if and only if it is a Cauchy sequence.

**Proof.**

**($\Rightarrow$)** Suppose first that $z_n \to z$. Given $\varepsilon > 0$, we can choose $N$ so that $|z_n - z| < \varepsilon/2$ if $n \geq N$. Then if $n, m \geq N$, by the triangle inequality,

$$|z_n - z_m| \leq |z_n - z| + |z - z_m| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

Thus $(z_n)_{n=1}^{\infty}$ is a Cauchy sequence.

**($\Leftarrow$)** We first prove the result for real sequences. Suppose $(x_n)_{n=1}^{\infty}$ is a Cauchy sequence in $\mathbb{R}$. Then $(x_n)$ is bounded: choose $N$ so that $|x_n - x_m| < 1$ for $n, m \geq N$, then $|x_n| \leq \max\{|x_1|, \ldots, |x_{N-1}|, |x_N| + 1\}$ for all $n$.

Define $x'_n = \inf\{x_m : m \geq n\}$ and $x''_n = \sup\{x_m : m \geq n\}$. Then $(x'_n)$ is a bounded increasing sequence, and $(x''_n)$ is a bounded decreasing sequence. By Proposition 3.2 (monotone convergence), both converge. Let $x' = \lim x'_n$ and $x'' = \lim x''_n$. Clearly $x'_n \leq x_n \leq x''_n$, so $x' \leq x''$.

Since $(x_n)$ is Cauchy, for any $\varepsilon > 0$ there exists $N$ such that $|x_n - x_m| < \varepsilon$ for $n, m \geq N$. Then for $n \geq N$, $x_n - \varepsilon \leq x_m \leq x_n + \varepsilon$ for all $m \geq N$, hence $x_n - \varepsilon \leq x'_N \leq x'$ and $x'' \leq x''_N \leq x_n + \varepsilon$. Therefore $|x_n - x'| \leq \varepsilon$ and $|x_n - x''| \leq \varepsilon$ for all $n \geq N$, which implies $x' = x''$ and $x_n \to x'$. Thus every real Cauchy sequence converges.

Now consider the case of a complex Cauchy sequence $(z_n)_{n=1}^{\infty}$. Write $z_n = x_n + i y_n$ with $x_n, y_n \in \mathbb{R}$. Since $|x_n - x_m| \leq |z_n - z_m|$ and $|y_n - y_m| \leq |z_n - z_m|$, both $(x_n)_{n=1}^{\infty}$ and $(y_n)_{n=1}^{\infty}$ are Cauchy sequences in $\mathbb{R}$. Therefore $x_n \to x \in \mathbb{R}$ and $y_n \to y \in \mathbb{R}$. By Proposition 3.1(b) (with $c = i$) and (a), $z_n = x_n + i y_n \to x + i y \in \mathbb{C}$. $\square$

**Remark.** The importance of this theorem lies partly in the fact that it gives a criterion for the existence of a limit in terms of the sequence itself. An immediately recognizable example is the sequence

$$3, 3.1, 3.14, 3.142, 3.1416, 3.14159, \ldots,$$

where successive terms are to be computed (in principle) in some specified way. This sequence can be shown to be a Cauchy sequence, so we know it has a limit. Knowing this, we are free to give the limit a name, such as "$\pi$".
