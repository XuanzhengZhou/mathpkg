---
role: proof
locale: en
of_concept: analytic-continuation-of-dirichlet-series-of-modular-form
source_book: gtm041
source_chapter: "6"
source_section: "6.16"
---

From the integral representation for the gamma function we have
$$(2\pi)^{-s}\Gamma(s)\varphi(s) = \int_0^\infty \{f(iy) - c(0)\} y^{s-1} dy,$$
valid for $\sigma = \operatorname{Re}(s) > k$.

Split the integral at $y = 1$:
$$(2\pi)^{-s} \Gamma(s) \varphi(s) = \int_1^\infty \{f(iy) - c(0)\} y^{s-1} dy + \int_0^1 \{f(iy) - c(0)\} y^{s-1} dy.$$

Since $f$ is a modular form in $M_k$, we have the transformation $f(i/y) = (iy)^k f(iy)$. In the second integral, rewrite the integrand using $f(iy) = (iy)^{-k}f(i/y)$ and substitute $w = 1/y$:
\begin{align*}
\int_0^1 \{f(iy) - c(0)\} y^{s-1} dy
&= \int_0^1 \{(iy)^{-k} f(i/y) - c(0)\} y^{s-1} dy \\
&= i^{-k} \int_1^\infty f(iw) w^{k-s-1} dw - \frac{c(0)}{s}.
\end{align*}

Since $k$ is even, $i^{-k} = (-1)^{k/2}$. Therefore
\begin{align*}
(2\pi)^{-s} \Gamma(s) \varphi(s)
&= \int_1^\infty \{f(iy) - c(0)\} y^{s-1} dy \\
&\quad + (-1)^{k/2} \int_1^\infty f(iw) w^{k-s-1} dw - \frac{c(0)}{s}.
\end{align*}

Rewrite the second integral by splitting $f(iw) = (f(iw) - c(0)) + c(0)$:
\begin{align*}
(2\pi)^{-s} \Gamma(s) \varphi(s)
&= \int_1^\infty \{f(iy) - c(0)\} y^{s-1} dy \\
&\quad + (-1)^{k/2} \int_1^\infty \{f(iw) - c(0)\} w^{k-s-1} dw \\
&\quad + (-1)^{k/2} c(0) \int_1^\infty w^{k-s-1} dw - \frac{c(0)}{s} \\
&= \int_1^\infty \{f(iy) - c(0)\} \left(y^s + (-1)^{k/2} y^{k-s}\right) \frac{dy}{y} \\
&\quad - c(0) \left(\frac{1}{s} + \frac{(-1)^{k/2}}{k-s}\right).
\end{align*}

Although this last relation was proved under the assumption that $\sigma > k$, the right-hand side is meaningful for all complex $s$ (the integral converges absolutely for all $s$ because $f(iy) - c(0)$ decays exponentially as $y \to \infty$). This gives the analytic continuation of $\varphi(s)$ beyond the line $\sigma = k$.

For part (a): if $c(0) = 0$, the pole terms $\frac{1}{s}$ and $\frac{1}{k-s}$ vanish, so the right-hand side is an entire function of $s$, hence $\varphi(s)$ is entire.

For part (b): if $c(0) \neq 0$, the only singularities are simple poles at $s = 0$ (from the $1/s$ term) and at $s = k$ (from the $1/(k-s)$ term). However, the pole at $s = 0$ is canceled by the factor $\Gamma(s)$ on the left-hand side (since $\Gamma(s)$ has a simple pole at $s = 0$). Thus $\varphi(s)$ has only a simple pole at $s = k$. Computing the residue: near $s = k$, the term $-c(0)(-1)^{k/2}/(k-s)$ dominates, and multiplying both sides by $(2\pi)^s/\Gamma(s)$ gives the residue as stated.

For part (c): replacing $s$ by $k - s$ leaves the right-hand side unchanged except for a factor $(-1)^{k/2}$, so we obtain
$$(2\pi)^{-s}\Gamma(s)\varphi(s) = (-1)^{k/2}(2\pi)^{s-k}\Gamma(k-s)\varphi(k-s),$$
which is the functional equation.
