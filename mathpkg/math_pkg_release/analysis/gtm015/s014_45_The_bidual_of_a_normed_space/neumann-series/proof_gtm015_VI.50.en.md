---
role: proof
locale: en
of_concept: neumann-series
source_book: gtm015
source_chapter: "VI"
source_section: "50"
---

# Proof of the Neumann Series for Banach Algebra Elements

Let $A$ be a Banach algebra with unity element $1$, and let $z \in A$ with $\|z\| < 1$. Define the partial sums
$$y_n = \sum_{k=0}^{n-1} z^k = 1 + z + z^2 + \cdots + z^{n-1},$$
with the convention $z^0 = 1$.

**Cauchy criterion:** Since $\|z\| < 1$, the sequence $(y_n)$ is Cauchy. Indeed, for $n, p \geq 0$,
$$\|y_{n+p} - y_n\| = \left\| \sum_{k=n}^{n+p-1} z^k \right\| \leq \sum_{k=n}^{n+p-1} \|z\|^k = \|z\|^n \sum_{k=0}^{p-1} \|z\|^k \leq \|z\|^n \sum_{k=0}^{\infty} \|z\|^k = \frac{\|z\|^n}{1 - \|z\|}.$$

Since $\|z\|^n \to 0$, the right-hand side tends to $0$ as $n \to \infty$, uniformly in $p$. Thus $(y_n)$ is Cauchy in the complete space $A$ and converges to some limit $y \in A$.

**Norm estimate:** For all $n$,
$$\|y_n\| \leq 1 + \|z\| + \cdots + \|z\|^{n-1} \leq \sum_{k=0}^{\infty} \|z\|^k = \frac{1}{1 - \|z\|}.$$
Since the norm is continuous (16.4), $\|y\| = \lim \|y_n\| \leq (1 - \|z\|)^{-1}$.

**Inverse verification:** Compute
$$z y_n = y_n z = z + z^2 + \cdots + z^n = y_{n+1} - 1.$$
Taking limits as $n \to \infty$,
$$z y = y z = y - 1,$$
hence $y - zy = y - yz = 1$, i.e., $(1 - z)y = y(1 - z) = 1$.

Thus $1 - z$ is invertible, with inverse
$$(1 - z)^{-1} = y = \sum_{n=0}^{\infty} z^n,$$
and the norm estimate $\|(1 - z)^{-1}\| \leq \frac{1}{1 - \|z\|}$ holds. $\square$
