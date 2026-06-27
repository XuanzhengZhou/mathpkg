---
role: proof
locale: en
of_concept: proposition-7.7-divisors-and-sections
source_book: gtm052
source_chapter: "II"
source_section: "7"
---

**Proof.** (a) We may identify $\mathcal{L}$ with the subsheaf $\mathcal{L}(D_0)$ of the constant sheaf $\mathcal{K}$ of rational functions on $X$. Then $s$ corresponds to a rational function $f \in K$. If $D_0$ is locally defined as a Cartier divisor by $\{(U_i, f_i)\}$ with $f_i \in \Gamma(U_i, \mathcal{K}^*)$, then over $U_i$, the section $s$ corresponds to $f = f_i \cdot g_i$ for some $g_i \in \Gamma(U_i, \mathcal{O}_{U_i})$. The divisor of zeros $(s)_0$ is locally defined by $\{(U_i, g_i)\}$, and since $(f) = D_0 + (s)_0$ as Cartier divisors, we have $(s)_0 \sim D_0$ (linearly equivalent). Moreover, $(s)_0$ is effective because each $g_i$ is a regular function.

(b) Let $D$ be an effective divisor linearly equivalent to $D_0$. Then $D - D_0 = (f)$ for some rational function $f \in K^*$. Since $D$ is effective and $D_0$ is fixed, the rational function $f$ satisfies that for any local equation $f_i$ of $D_0$ on $U_i$, we have $f \cdot f_i \in \Gamma(U_i, \mathcal{O}_{U_i})$. Therefore $f$ defines a global section $s \in \Gamma(X, \mathcal{L}(D_0)) \cong \Gamma(X, \mathcal{L})$, and by construction $(s)_0 = D$.

(c) If $s' = \lambda s$ for $\lambda \in k^*$, then locally $\varphi(s') = \lambda \varphi(s)$, so the Cartier divisors defined by $\{(U, \varphi(s))\}\) and $\{(U, \varphi(s'))\}$ are the same. Conversely, if $(s)_0 = (s')_0$, then the ratio $s/s'$ is a rational function on $X$ with no zeros or poles, hence is a regular invertible function on $X$. Since $X$ is projective and $k$ is algebraically closed, $\Gamma(X, \mathcal{O}_X^*) = k^*$, so $s/s' = \lambda \in k^*$, giving $s' = \lambda s$. $\square$
