---
role: proof
locale: en
of_concept: conjugates-in-field
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 54: Conjugates of Numbers in a Field Extension

**Theorem 54.** Let $K = K(\theta; k)$ be a finite extension of $k$ of relative degree $n$. Let $\theta_1, \ldots, \theta_n$ be the conjugates of $\theta$ with respect to $k$. For each $\alpha \in K$, write $\alpha = g(\theta)$ with $g(x) \in k[x]$, $\deg g \leq n-1$. Then:

1. The numbers $\alpha_i = g(\theta_i)$ for $i = 1, \ldots, n$ are algebraic over $k$ of degree dividing $n$.
2. The conjugates of $\alpha$ with respect to $k$ are precisely the distinct numbers among $\{\alpha_1, \ldots, \alpha_n\}$.
3. If $\alpha$ has degree $d$ over $k$, then $d \mid n$, and each conjugate of $\alpha$ appears exactly $q = n/d$ times among the $\alpha_i$.

*Proof.* **(1)** By Theorem 53, the representation $\alpha = g(\theta)$ with $\deg g \leq n-1$ is possible and unique. Form the polynomial

$$F(x) = \prod_{i=1}^{n} \bigl(x - g(\theta_i)\bigr) = x^n - s_1 x^{n-1} + s_2 x^{n-2} - \cdots + (-1)^n s_n,$$

where $s_1, \ldots, s_n$ are the elementary symmetric functions of $g(\theta_1), \ldots, g(\theta_n)$. Each $s_j$ is a symmetric polynomial in $\theta_1, \ldots, \theta_n$ with coefficients in $k$. By the fundamental theorem on symmetric functions, each $s_j$ can be expressed as a polynomial (with coefficients in $k$) in the elementary symmetric functions of $\theta_1, \ldots, \theta_n$, which themselves are (up to sign) the coefficients of the minimal polynomial $f(x)$ of $\theta$. Since these coefficients belong to $k$, we have $s_j \in k$, and therefore $F(x) \in k[x]$.

Since $\alpha = g(\theta)$ and $F(g(\theta)) = \prod_i (g(\theta) - g(\theta_i))$ with the factor for $i$ such that $\theta_i = \theta$ giving zero, we have $F(\alpha) = 0$. Thus $\alpha$ is algebraic over $k$ and its degree satisfies $d \leq n$. That $d \mid n$ follows from part (3).

**(2)** Let $\sigma_i : k(\theta) \to k(\theta_i)$ be the $k$-isomorphism sending $\theta \mapsto \theta_i$. Extended to an embedding of $K$ into an algebraic closure $\overline{k}$ of $k$, we have $\sigma_i(\alpha) = \sigma_i(g(\theta)) = g(\sigma_i(\theta)) = g(\theta_i)$. Since the conjugates of $\alpha$ over $k$ are precisely the images of $\alpha$ under all $k$-embeddings of $K$ into $\overline{k}$, and these embeddings contain (perhaps with repetitions) the maps $\sigma_1, \ldots, \sigma_n$, the conjugates of $\alpha$ are exactly the distinct values among $g(\theta_1), \ldots, g(\theta_n)$.

**(3)** Let $\varphi(x) = \prod_{j=1}^{d} (x - \alpha_j)$ be the minimal polynomial of $\alpha$ over $k$, where $\alpha_1 = \alpha$ and $\alpha_1, \ldots, \alpha_d$ are the distinct conjugates. Since $\varphi(x)$ is irreducible and $\varphi(\alpha) = 0$, we have $\varphi(x) \mid F(x)$ in $k[x]$. Because $F(x)$ has degree $n$, $d$ divides $n$. Write $n = dq$. Both $F(x)$ and $\varphi(x)^q$ have the same roots (the $\alpha_j$) with equal multiplicities, and both are monic polynomials in $k[x]$ whose roots are the $\alpha_j$. Since the field is perfect (characteristic zero), $F(x) = \varphi(x)^q$, and each conjugate $\alpha_j$ appears exactly $q$ times among the $n$ values $g(\theta_1), \ldots, g(\theta_n)$. $\square$
