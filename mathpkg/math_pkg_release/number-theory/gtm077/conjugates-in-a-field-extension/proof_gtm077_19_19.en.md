---
role: proof
locale: en
of_concept: conjugates-in-a-field-extension
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 54: Conjugates of Numbers in $K(\theta)$

**Theorem 54 (Conjugates in a Field Extension).** Let $K = K(\theta; k)$ be a finite extension of $k$ of relative degree $n$, and let $\theta_1, \theta_2, \ldots, \theta_n$ be the conjugates of $\theta$ with respect to $k$. For every $\alpha = g(\theta) \in K$, the $n$ values

$$\alpha_i = g(\theta_i) \qquad (i = 1, 2, \ldots, n)$$

form a complete system of conjugates of $\alpha$ with respect to $k$, each one taken with a certain multiplicity. The degree of $\alpha$ over $k$ divides $n$, and if the degree is $d$, then each conjugate appears $q = n/d$ times among the $\alpha_i$.

*Proof.* By Theorem 53, write $\alpha = g(\theta)$ for a polynomial $g(x) \in k[x]$ of degree at most $n-1$. Consider the polynomial

$$F(x) = \prod_{i=1}^{n} \bigl(x - g(\theta_i)\bigr).$$

We claim $F(x) \in k[x]$. Indeed, the coefficients of $F$ are symmetric polynomials in $g(\theta_1), \ldots, g(\theta_n)$, hence symmetric polynomials in $\theta_1, \ldots, \theta_n$ with coefficients in $k$. By the fundamental theorem on symmetric functions, any symmetric polynomial in $\theta_1, \ldots, \theta_n$ with coefficients in $k$ can be expressed as a polynomial over $k$ in the elementary symmetric functions of $\theta_1, \ldots, \theta_n$, which are (up to sign) the coefficients of the minimal polynomial of $\theta$. These coefficients lie in $k$, hence $F(x) \in k[x]$.

Since $F(g(\theta)) = F(\alpha) = 0$, the number $\alpha$ is algebraic over $k$ and its degree $d$ over $k$ satisfies $d \leq n$. Let $\varphi(x) \in k[x]$ be the minimal polynomial of $\alpha$, so $\deg \varphi = d$ and $\varphi(x)$ is irreducible. Then $\varphi(x) \mid F(x)$ in $k[x]$.

Over an algebraic closure of $k$, both $F(x)$ and $\varphi(x)$ split completely. The roots of $\varphi(x)$ are exactly the $d$ conjugates of $\alpha$, each with multiplicity one (since we work in characteristic zero). The roots of $F(x)$ are the numbers $g(\theta_1), \ldots, g(\theta_n)$. Because $\varphi(x) \mid F(x)$, every root of $\varphi$ is a root of $F$, so the conjugates of $\alpha$ are among the values $g(\theta_i)$.

Conversely, for each $i$, the isomorphism $\sigma_i : k(\theta) \to k(\theta_i)$ defined by $\sigma_i(\theta) = \theta_i$ extends to an embedding of $K$ into the algebraic closure, and $\sigma_i(\alpha) = \sigma_i(g(\theta)) = g(\sigma_i(\theta)) = g(\theta_i)$. Hence $g(\theta_i)$ is a conjugate of $\alpha$. Therefore the set of conjugates of $\alpha$ is precisely $\{g(\theta_1), \ldots, g(\theta_n)\}$ (with repetitions).

Since $\varphi(x) \mid F(x)$ and $\varphi$ is separable of degree $d$, the polynomial $F$ must be a power of $\varphi$: $F(x) = \varphi(x)^q$ where $q = n/d$. Thus each conjugate $\alpha_j$ appears exactly $q$ times among the $n$ values $g(\theta_i)$. In particular, the relative degree $n$ of $K(\theta)$ depends only on the field $K$ and not on the choice of generating element $\theta$. $\square$
