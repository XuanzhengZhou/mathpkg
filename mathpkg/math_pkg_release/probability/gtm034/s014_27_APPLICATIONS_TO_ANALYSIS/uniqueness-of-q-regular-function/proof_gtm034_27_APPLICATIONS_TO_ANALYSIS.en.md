---
role: proof
locale: en
of_concept: uniqueness-of-q-regular-function
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

**Proof of P3:**

Suppose $h(x)$ is $Q$-regular and not identically zero. We must show that $h(x) = cf(x)$ for some constant $c > 0$.

*Step 1: Positivity of $h$.* First observe that $h(x) > 0$ for all $x \in S$. Indeed, if $h(x_0) = 0$ for some $x_0$, then from
$$\sum_{y \in S} Q_n(x_0,y)h(y) = h(x_0) = 0, \quad n \geq 0,$$
and the non-negativity of $Q_n$ and $h$, we would have $h(y) = 0$ whenever $Q_n(x_0,y) > 0$ for some $n$. But $g(x,y) = \sum_n Q_n(x,y) > 0$ for all $x,y \in S$ by hypothesis, so $Q_n(x_0,y) > 0$ for some $n$, implying $h \equiv 0$, contradiction.

*Step 2: The $h$-transform.* Using the positive $Q$-regular function $h$, define $Q^h$ and $g^h$ via D4. By P2, $Q^h$ is a transient kernel and the constant function $e(x) \equiv 1$ is $Q^h$-regular.

*Step 3: Approximating the constant by potentials.* Fix an arbitrary point $\eta \in S$ and define, for $n = 1, 2, \dots$,
$$\tau_n(x) = \min\left[1, \, n g^h(x,\eta)\right], \quad x \in S.$$
Clearly $0 \leq \tau_n(x) \leq 1$ and $\tau_n(x) \to 1$ as $n \to \infty$ for each $x \in S$.

Each $\tau_n$ is the minimum of the constant $e(x) \equiv 1$ (which is $Q^h$-regular, hence excessive) and $n g^h(x,\eta)$ (which is a potential). By P1(2), $\tau_n$ is $Q^h$-excessive. Apply the Riesz decomposition T1 to $\tau_n$:
$$\tau_n(x) = k_n(x) + u_n(x),$$
where $k_n$ is $Q^h$-regular and $u_n$ is a $Q^h$-potential. Since $\tau_n \leq n g^h(\cdot,\eta)$, we have $k_n(x) \leq n g^h(x,\eta)$. But $k_n$ is regular, so $k_n(x) = Q^h_m k_n(x) \leq n Q^h_m g^h(x,\eta)$ for all $m$. By P1(3), $Q^h_m g^h(x,\eta) \to 0$ as $m \to \infty$, hence $k_n \equiv 0$. Thus each $\tau_n$ is itself a $Q^h$-potential:
$$\tau_n(x) = \sum_{y \in S} g^h(x,y) \mu_n(y), \quad x \in S,$$
for some non-negative charge $\mu_n$.

*Step 4: Introducing the Green function ratio.* Rewrite as
$$\tau_n(x) = \sum_{y \in S} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma_n(y), \quad \text{where } \gamma_n(y) = g^h(\xi,y)\mu_n(y).$$
Note that $\sum_y \gamma_n(y) = \tau_n(\xi) \leq 1$.

*Step 5: Taking limits.* By the hypothesis of P3 and the definition of $g^h$,
$$\lim_{|y| \to \infty} \frac{g^h(x,y)}{g^h(\xi,y)} = \frac{h(\xi)}{h(x)} \lim_{|y| \to \infty} \frac{g(x,y)}{g(\xi,y)} = f(x) \frac{h(\xi)}{h(x)}.$$

Choose a subsequence $n'$ along which $\gamma_{n'}(y) \to \gamma(y)$ for each $y \in S$ (possible by diagonal argument). Let $M$ be large enough so that for $|y| > M$,
$$\left| \frac{g^h(x,y)}{g^h(\xi,y)} - f(x)\frac{h(\xi)}{h(x)} \right| < \varepsilon.$$

Then from $\tau_{n'}(x) \to 1$:
$$1 = \sum_{|y| \leq M} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma(y) + \lim_{n' \to \infty} f(x)\frac{h(\xi)}{h(x)} \sum_{|y| > M} \gamma_{n'}(y) + R(M),$$
where $|R(M)| \leq \varepsilon \cdot h(\xi)/h(x)$. Letting $M \to \infty$ and defining $\gamma_\infty = \lim_{M \to \infty} \lim_{n'} \sum_{|y| > M} \gamma_{n'}(y) \in [0,1]$, we obtain
$$1 = \sum_{y \in S} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma(y) + \gamma_\infty f(x) \frac{h(\xi)}{h(x)}, \quad x \in S. \tag{*}$$

*Step 6: Eliminating the first term.* In $(*)$, the left side is $Q^h$-regular, the first term on the right is a $Q^h$-potential, and the second term is $Q^h$-regular times a constant. By the uniqueness of the Riesz decomposition T1, the potential part must vanish: $\sum_{y} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma(y) = 0$. Since $g^h(x,y) > 0$, this forces $\gamma(y) \equiv 0$ for all $y$.

*Step 7: Conclusion.* With $\gamma \equiv 0$, $(*)$ reduces to $1 = \gamma_\infty f(x) h(\xi)/h(x)$, i.e.,
$$h(x) = \gamma_\infty h(\xi) f(x), \quad x \in S.$$
Thus $h$ is a constant multiple of $f$, as required.
