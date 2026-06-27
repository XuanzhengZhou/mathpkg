---
role: proof
locale: en
of_concept: generating-element-characterization
source_book: gtm077
source_chapter: "20"
source_section: "20"
---
# Proof of Theorem 56: Characterization of Generating Elements

**Theorem 56.** Let $K = K(\theta; k)$ be an extension of degree $n$ over $k$. For a number $\alpha \in K$, let $\alpha_1, \alpha_2, \ldots, \alpha_n$ be its $n$ conjugates in $K$ (with multiplicities as in Theorem 54).

1. $\alpha$ belongs to the ground field $k$ if and only if all its $n$ conjugates are equal: $\alpha_1 = \alpha_2 = \cdots = \alpha_n$.
2. $\alpha$ has degree $n$ over $k$ if and only if its $n$ conjugates are pairwise distinct.
3. The condition in (2) is necessary and sufficient for $\alpha$ to generate the field $K$, i.e., $K = K(\alpha; k)$.

*Proof.* **(1)** If $\alpha \in k$, then $\alpha = g(\theta)$ with the constant polynomial $g(x) = \alpha$. Then $g(\theta_i) = \alpha$ for all $i$, so $\alpha_1 = \cdots = \alpha_n = \alpha$.

Conversely, suppose $\alpha_1 = \alpha_2 = \cdots = \alpha_n = \alpha$. By Theorem 53 write $\alpha = g(\theta)$ with $\deg g \leq n-1$. The polynomial $g(x) - \alpha$ has roots $\theta_1, \ldots, \theta_n$. Since the $\theta_i$ are pairwise distinct (the minimal polynomial of $\theta$ is separable, characteristic zero), $g(x) - \alpha$ is a polynomial of degree at most $n-1$ with $n$ distinct roots, hence it must be identically zero. Thus $g(x) \equiv \alpha$, which implies $\alpha \in k$.

**(2)** By Theorem 54, if $\alpha$ has degree $d$ over $k$, then $d \mid n$ and each conjugate of $\alpha$ appears $q = n/d$ times among the $\alpha_i$. Hence all $\alpha_i$ are distinct if and only if $q = 1$, i.e., $d = n$.

**(3)** Suppose $\alpha$ has degree $n$ over $k$, so its conjugates $\alpha_1, \ldots, \alpha_n$ are distinct. We show that $\theta$ can be expressed as a rational function of $\alpha$ with coefficients in $k$, so $\theta \in K(\alpha; k)$ and consequently $K = K(\alpha; k)$.

Write $\alpha = g(\theta)$ as before. Form the polynomial

$$H(x) = \prod_{i=1}^{n} (x - \alpha_i).$$

The coefficients of $H$ are symmetric in $\theta_1, \ldots, \theta_n$, hence lie in $k$ as in the proof of Theorem 52. Now construct, via Lagrange interpolation,

$$\Phi(x) = \sum_{i=1}^{n} \theta_i \frac{H(x)}{x - \alpha_i}.$$

As in Theorem 52, the expression $\frac{H(x)}{x - \alpha_i} = G(x, \alpha_i)$ is a polynomial in $x$ and $\alpha_i$ with coefficients in $k$, where

$$G(x, y) = \frac{H(x) - H(y)}{x - y}.$$

Since $\Phi(x)$ is a symmetric expression in $\theta_1, \ldots, \theta_n$ with coefficients in $k$, its coefficients belong to $k$. Thus $\Phi(x) \in k[x]$. Now set $x = \alpha_1 = \alpha$. All summands with $i \neq 1$ vanish because $H(\alpha_1) = 0$. The remaining term gives

$$\Phi(\alpha_1) = \theta_1 \cdot G(\alpha_1, \alpha_1).$$

Since the $\alpha_i$ are distinct, $H'(\alpha_1) = G(\alpha_1, \alpha_1) \neq 0$ (the roots are simple), so

$$\theta_1 = \theta = \frac{\Phi(\alpha)}{G(\alpha, \alpha)} \in K(\alpha).$$

Thus $\theta \in K(\alpha; k)$ and $K = K(\theta; k) \subseteq K(\alpha; k) \subseteq K$, giving equality $K = K(\alpha; k)$.

Conversely, if $\alpha$ generates $K$, then $[K : k] = [K(\alpha) : k]$ is the degree of $\alpha$, which must be $n$. Hence by (2) all conjugates are distinct. $\square$
