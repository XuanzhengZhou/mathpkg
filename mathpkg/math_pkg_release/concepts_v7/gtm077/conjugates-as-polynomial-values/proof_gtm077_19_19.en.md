---
role: proof
locale: en
of_concept: conjugates-as-polynomial-values
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 54: Conjugates as Polynomial Values

**Theorem 54.** Let $K = K(\theta; k)$ be a simple extension of $k$ of relative degree $n$, with $\theta_1, \ldots, \theta_n$ the conjugates of $\theta$ with respect to $k$. Every number $\alpha = g(\theta) \in K$ (with $g(x) \in k[x]$ of degree at most $n-1$) is algebraic over $k$ of degree at most $n$. The relative conjugates of $\alpha$ are exactly the distinct numbers among the values

$$g(\theta_1), g(\theta_2), \ldots, g(\theta_n),$$

and each distinct conjugate appears equally often among these $n$ values.

*Proof.* Represent $\alpha$ as $\alpha = g(\theta)$ with $g(x) \in k[x]$, $\deg g \leq n-1$, which is possible by Theorem 53. Form the polynomial

$$F(x) = \prod_{i=1}^{n} \bigl(x - g(\theta_i)\bigr).$$

The coefficients of $F(x)$ are, up to sign, the elementary symmetric functions in the quantities $g(\theta_1), \ldots, g(\theta_n)$. Each such symmetric function is a polynomial expression in the $\theta_i$ that is symmetric in $\theta_1, \ldots, \theta_n$ and has coefficients in $k$. By the fundamental theorem on symmetric functions, any symmetric polynomial in $\theta_1, \ldots, \theta_n$ with coefficients in $k$ can be expressed as a polynomial in the elementary symmetric functions of the $\theta_i$, which are (up to sign) the coefficients of the minimal polynomial $f(x)$ of $\theta$. Since these coefficients lie in $k$, the coefficients of $F(x)$ belong to $k$.

Thus $F(x) \in k[x]$ and $F(\alpha) = F(g(\theta)) = 0$. Hence $\alpha$ is algebraic over $k$ of degree at most $n$.

Now let $\alpha_1 = \alpha$ and let its conjugates with respect to $k$ be $\alpha_1, \alpha_2, \ldots, \alpha_d$, where $d \mid n$ (see below). The irreducible polynomial of $\alpha$ over $k$ is

$$\varphi(x) = \prod_{j=1}^{d} (x - \alpha_j).$$

Since $\varphi(x) \mid F(x)$ (because $F(\alpha) = 0$ and $\varphi$ is minimal), and $F(x) = \prod_{i=1}^{n} (x - g(\theta_i))$, each conjugate $\alpha_j$ must appear among the values $g(\theta_1), \ldots, g(\theta_n)$. Conversely, each $g(\theta_i)$ is a conjugate of $\alpha$. Thus the set of relative conjugates of $\alpha$ is exactly the set of distinct numbers among the $g(\theta_i)$.

Moreover, the number of times each conjugate $\alpha_j$ appears among the $n$ values $g(\theta_i)$ is the same for all $j$, because $\varphi(x)$ divides $F(x)$ and $F(x)$ is the $n$-th power of the product over distinct conjugates if we group equal factors. More precisely, let $q = n/d$. Since $F(x) = \varphi(x)^q$ (as $F$ and $\varphi$ share the same roots over an algebraic closure of $k$ and $\varphi$ is separable), each conjugate appears exactly $q$ times. $\square$
