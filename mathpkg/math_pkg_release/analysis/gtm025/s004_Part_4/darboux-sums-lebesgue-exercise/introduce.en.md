---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $f$ be a bounded, real-valued function on $[a, b]$. For each $x \in [a,b]$, define

$$m(x) = \lim_{\delta \to 0} \inf\{f(t): |t-x| < \delta, t \in [a,b]\}, \quad M(x) = \lim_{\delta \to 0} \sup\{f(t): |t-x| < \delta, t \in [a,b]\}.$$

Let $(\Delta_j)_{j=1}^{\infty}$ be a sequence of subdivisions of $[a, b]$ with mesh tending to zero. Let $\varphi_j$ and $\psi_j$ be the corresponding lower and upper step functions.

Prove that:
(b) if $x \in [a, b]$ and $x$ is distinct from all subdivision points $x_k^{(j)}$, then $\lim_{j \to \infty} \varphi_j(x) = m(x)$ and $\lim_{j \to \infty} \psi_j(x) = M(x)$;
(c) $m$ and $M$ are Lebesgue measurable on $[a, b]$;
(d) if $L(f, \Delta_j)$ and $U(f, \Delta_j)$ are the lower and upper Darboux sums for $f$ corresponding to $\Delta_j$, then
$$\lim_{j \to \infty} L(f, \Delta_j) = \int_a^b m(x) \, dx \quad \text{and} \quad \lim_{j \to \infty} U(f, \Delta_j) = \int_a^b M(x) \, dx;$$
(e) $f$ is Riemann integrable on $[a,b]$ if and only if $m(x) = M(x)$ for almost all $x \in [a,b]$.
