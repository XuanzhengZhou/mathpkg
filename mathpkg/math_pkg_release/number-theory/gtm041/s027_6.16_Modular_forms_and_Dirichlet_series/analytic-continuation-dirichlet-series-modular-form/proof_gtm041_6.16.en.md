---
role: proof
locale: en
of_concept: analytic-continuation-dirichlet-series-modular-form
source_book: gtm041
source_chapter: "6"
source_section: "6.16"
---

**Proof of Theorem 6.20.** From the integral representation for $\Gamma(s)$ we have, for each $n \geq 1$,
$$(2\pi)^{-s} \Gamma(s) n^{-s} = \int_0^\infty e^{-2\pi n y} y^{s-1} \, dy.$$
Multiplying by $c(n)$ and summing over $n \geq 1$ yields, for $\sigma > k$,
$$(2\pi)^{-s} \Gamma(s) \varphi(s) = \int_0^\infty \left( \sum_{n=1}^{\infty} c(n) e^{-2\pi n y} \right) y^{s-1} \, dy = \int_0^\infty \{f(iy) - c(0)\} y^{s-1} \, dy.$$

Split the integral at $y = 1$:
$$(2\pi)^{-s} \Gamma(s) \varphi(s) = \int_1^\infty \{f(iy) - c(0)\} y^{s-1} \, dy + \int_0^1 \{f(iy) - c(0)\} y^{s-1} \, dy.$$

Since $f \in M_k$, we have the modular transformation $f(i/y) = (iy)^k f(iy)$. Using the change of variable $y \mapsto 1/w$ in the second integral,
$$\int_0^1 \{f(iy) - c(0)\} y^{s-1} \, dy = \int_1^\infty \left\{ f\!\left(\frac{i}{w}\right) - c(0) \right\} w^{-s-1} \, dw.$$

Applying $f(i/w) = (iw)^k f(iw)$ and $i^{-k} = (-1)^{k/2}$ (since $k$ is even),
\begin{align*}
\int_0^1 \{f(iy) - c(0)\} y^{s-1} \, dy
&= \int_1^\infty \{(iw)^k f(iw) - c(0)\} w^{-s-1} \, dw \\
&= (-1)^{k/2} \int_1^\infty f(iw) w^{k-s-1} \, dw - c(0) \int_1^\infty w^{-s-1} \, dw \\
&= (-1)^{k/2} \int_1^\infty \{f(iw) - c(0)\} w^{k-s-1} \, dw \\
&\quad + (-1)^{k/2} c(0) \int_1^\infty w^{k-s-1} \, dw - c(0) \int_1^\infty w^{-s-1} \, dw.
\end{align*}

Computing the elementary integrals,
$$(-1)^{k/2} c(0) \int_1^\infty w^{k-s-1} \, dw = \frac{(-1)^{k/2} c(0)}{s - k}, \qquad c(0) \int_1^\infty w^{-s-1} \, dw = \frac{c(0)}{s},$$
valid for $\sigma > k$ (where both integrals converge). Combining all terms,
\begin{align*}
(2\pi)^{-s} \Gamma(s) \varphi(s) &= \int_1^\infty \{f(iy) - c(0)\} \left( y^s + (-1)^{k/2} y^{k-s} \right) \frac{dy}{y} \\
&\quad - c(0) \left( \frac{1}{s} + \frac{(-1)^{k/2}}{k-s} \right).
\end{align*}

Although this relation was derived under the assumption $\sigma > k$, the right-hand side is meaningful for all complex $s$: the integral converges absolutely for every $s$ because $f(iy) - c(0) = O(e^{-2\pi y})$ as $y \to \infty$, while the rational terms are meromorphic with at most simple poles at $s = 0$ and $s = k$. This provides the analytic continuation of $\varphi(s)$ beyond the line $\sigma = k$, establishing properties (a) and (b).

For the functional equation (c), note that replacing $s$ by $k - s$ in the right-hand side yields
\begin{align*}
(2\pi)^{-(k-s)} \Gamma(k-s) \varphi(k-s) &= \int_1^\infty \{f(iy) - c(0)\} \left( y^{k-s} + (-1)^{k/2} y^{s} \right) \frac{dy}{y} \\
&\quad - c(0) \left( \frac{1}{k-s} + \frac{(-1)^{k/2}}{s} \right).
\end{align*}

Factoring $(-1)^{k/2}$ from the right-hand side of the original expression shows that
$$(2\pi)^{-s} \Gamma(s) \varphi(s) = (-1)^{k/2} (2\pi)^{-(k-s)} \Gamma(k-s) \varphi(k-s),$$
which is equivalent to the stated functional equation after multiplying both sides by $(2\pi)^{k-s}$. $\square$
