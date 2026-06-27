---
role: proof
locale: en
of_concept: cauchy-theorem-homotopy
source_book: gtm011
source_chapter: "4"
source_section: "6"
---

Let $\Gamma: I^2 \to G$ satisfy the homotopy conditions (6.2). Since $\Gamma$ is continuous and $I^2$ is compact, $\Gamma$ is uniformly continuous and $\Gamma(I^2)$ is a compact subset of $G$. Thus
$$
r = d(\Gamma(I^2), \mathbb{C} - G) > 0
$$
and there is an integer $n$ such that if $(s - s')^2 + (t - t')^2 < 4/n^2$ then
$$
|\Gamma(s, t) - \Gamma(s', t')| < r.
$$

Let
$$
Z_{jk} = \Gamma\left(\frac{j}{n}, \frac{k}{n}\right), \quad 0 \leq j, k \leq n
$$
and put
$$
J_{jk} = \left[ \frac{j}{n}, \frac{j+1}{n} \right] \times \left[ \frac{k}{n}, \frac{k+1}{n} \right]
$$
for $0 \leq j, k \leq n - 1$. Since the diameter of the square $J_{jk}$ is $\sqrt{2}/n$, it follows that $\Gamma(J_{jk}) \subset B(Z_{jk}; r)$. So if we let $P_{jk}$ be the closed polygon $[Z_{jk}, Z_{j+1, k}, Z_{j+1, k+1}, Z_{j,k+1}, Z_{jk}]$, then, because disks are convex, $P_{jk} \subset B(Z_{jk}; r)$. But $B(Z_{jk}; r) \subset G$ by definition of $r$.

For the special case where $\Gamma$ has continuous second partial derivatives, one defines
$$
g(t) = \int_0^1 f(\Gamma(s, t)) \frac{\partial \Gamma}{\partial s}(s, t) \, ds
$$
so that $g(0) = \int_{\gamma_0} f$ and $g(1) = \int_{\gamma_1} f$. Differentiating under the integral sign and using $\frac{\partial^2 \Gamma}{\partial s \partial t} = \frac{\partial^2 \Gamma}{\partial t \partial s}$ together with the chain rule yields
$$
g'(t) = f(\Gamma(1, t)) \frac{\partial \Gamma}{\partial t}(1, t) - f(\Gamma(0, t)) \frac{\partial \Gamma}{\partial t}(0, t).
$$
Since $\Gamma(1, t) = \Gamma(0, t)$ for all $t$, we get $g'(t) = 0$ for all $t$. So $g$ is constant; in particular $\int_{\gamma_0} f = \int_{\gamma_1} f$.

The general case is obtained by approximating the homotopy on each small square $J_{jk}$ using Cauchy's Theorem in the convex disk $B(Z_{jk}; r)$.
