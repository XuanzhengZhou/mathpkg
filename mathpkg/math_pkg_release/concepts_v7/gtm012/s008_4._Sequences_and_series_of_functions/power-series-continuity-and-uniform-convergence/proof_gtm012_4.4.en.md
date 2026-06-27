---
role: proof
locale: en
of_concept: power-series-continuity-and-uniform-convergence
source_book: gtm012
source_chapter: "4"
source_section: "4. Sequences and series of functions"
---

# Proof of Theorem 4.3: Continuity of power series and uniform convergence of partial sums on subdiscs

**Theorem 4.3.** Let $R$ be the radius of convergence of the power series

$$\sum_{n=0}^{\infty} a_n (z - z_0)^n.$$

For each $n$, define the partial sum

$$f_n(z) = \sum_{m=0}^{n} a_m (z - z_0)^m.$$

Then the function $f$ defined by

$$f(z) = \sum_{m=0}^{\infty} a_m (z - z_0)^m, \quad |z - z_0| < R$$

is a continuous function. Moreover, the functions $f_n$ converge to $f$ uniformly on each disc

$$D_r = \{z \mid |z - z_0| < r\}, \quad 0 < r < R.$$

*Proof.* We prove uniform convergence first. Given $0 < r < R$, choose $s$ with $r < s < R$. Take $w$ with $|w - z_0| = s$. By assumption, $\sum a_n (w - z_0)^n$ converges. Therefore the terms of this series tend to $0$. It follows that there is a constant $M$ such that

$$|a_n (w - z_0)^n| \leq M, \quad n = 0, 1, 2, \ldots.$$

Since $|w - z_0| = s$, this means

$$|a_n| \leq M s^{-n}, \quad n = 0, 1, 2, \ldots.$$

Now suppose $z \in D_r$ and $m < n$. Set $\delta = r/s < 1$. Then

$$
\begin{aligned}
|f_n(z) - f_m(z)|
&= \left| \sum_{j=m+1}^{n} a_j (z - z_0)^j \right| \\
&\leq \sum_{j=m+1}^{n} |a_j| \, |z - z_0|^j \\
&\leq \sum_{j=m+1}^{n} M s^{-j} r^j \\
&= M \sum_{j=m+1}^{n} \delta^{j} \\
&= M \frac{\delta^{m+1} - \delta^{n+1}}{1 - \delta} \\
&\leq \frac{M \delta^{m+1}}{1 - \delta}.
\end{aligned}
$$

Since $\delta < 1$, $\delta^{m+1} \to 0$ as $m \to \infty$. Thus $(f_n)$ is a uniform Cauchy sequence on $D_r$, and by Theorem 4.1 it converges uniformly on $D_r$ to a bounded function. The limit function must be $f$, since pointwise convergence already gives $f_n(z) \to f(z)$.

Since each $f_n$ (being a polynomial in $z$) is continuous, Theorem 4.1 implies that the uniform limit $f$ is continuous on each $D_r$. As every point with $|z - z_0| < R$ lies in some $D_r$ (take $r$ between $|z - z_0|$ and $R$), $f$ is continuous on the whole disc of convergence. $\square$
