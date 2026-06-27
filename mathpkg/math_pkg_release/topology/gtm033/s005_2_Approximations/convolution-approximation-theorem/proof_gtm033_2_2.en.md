---
role: proof
locale: en
of_concept: convolution-approximation-theorem
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.3 — Convolution Approximation

**Theorem 2.3.** Let $\theta: \mathbb{R}^m \to \mathbb{R}$ have support radius $\delta > 0$. Let $U \subset \mathbb{R}^m$ be an open set, and $f: U \to \mathbb{R}^n$ a continuous map. The convolution $\theta * f: U_\delta \to \mathbb{R}^n$ has the following properties:

(a) If $\theta|\operatorname{Int Supp}\theta$ is $C^k$, $1 \leqslant k \leqslant \infty$, then so is $\theta * f$; and for each finite $k$,

$$D^k(\theta * f) = (D^k \theta) * f$$

on $U_\delta$.

(b) If $f$ is $C^k$ then

$$D^k(\theta * f) = \theta * D^k f.$$

(c) Suppose $f$ is $C^r$, $0 \leqslant r \leqslant \infty$. Let $K \subset U$ be compact. Given $\varepsilon > 0$ there exists $\delta > 0$ such that $K \subset U_\delta$, and if $\theta$ is a $C^r$ convolution kernel of support radius $\delta$, then $\theta * f$ is $C^r$ and

$$\|\theta * f - f\|_{r, K} < \varepsilon.$$

*Proof.* To prove (b), observe that the domain of integration in (1) can be restricted to $\operatorname{Int Supp} \theta$; the integrand is then differentiable in $x$, and (b) follows by induction on $k$ and differentiating under the integral sign. (a) is proved similarly using (3).

To prove (c) it suffices to take $r = 0$, by (b). Since $d(K, \mathbb{R}^m - U) > 0$, we can choose $\delta$ so small that $K \subset U_\delta$. By uniform continuity of $f$ on a compact neighborhood of $K$, we can choose $\delta$ so small that if $x \in K$ and $|x - y| \leqslant \delta$ then $|f(x) - f(y)| < \varepsilon$.

Since $\int_{\mathbb{R}^m} \theta = 1$, we have, integrating over $\mathbb{R}^m$:

$$
\begin{aligned}
\left| \theta * f(x) - f(x) \right|
&= \left| \int \theta(y) \left( f(x - y) - f(x) \right) dy \right| \\
&\leqslant \int \theta(y) \left| f(x - y) - f(x) \right| dy \\
&\leqslant \varepsilon \int \theta(y) \, dy = \varepsilon.
\end{aligned}
$$

QED
