---
role: proof
locale: en
of_concept: vandermonde-convolution-identity
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Vandermonde's Convolution Identity

## Statement

For nonnegative integers $n$, $m$, and $k$,

$$\sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j} = \binom{n+m}{k}.$$

## Proof via Generating Functions

Consider the binomial expansions of $(1+x)^n$ and $(1+x)^m$:

$$(1+x)^n = \sum_{j=0}^{n} \binom{n}{j} x^j, \qquad (1+x)^m = \sum_{\ell=0}^{m} \binom{m}{\ell} x^\ell.$$

By the convolution property of generating functions, the coefficient of $x^k$ in the product $(1+x)^n(1+x)^m$ is obtained by convolving the two sequences of binomial coefficients:

$$\text{coeff}_{x^k}\left[(1+x)^n(1+x)^m\right] = \sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j},$$

where we adopt the convention $\binom{n}{j} = 0$ for $j > n$ and $\binom{m}{k-j} = 0$ for $k-j > m$, so that the sum can be written over $j = 0, \ldots, k$.

On the other hand, by the law of exponents,

$$(1+x)^n(1+x)^m = (1+x)^{n+m} = \sum_{k=0}^{n+m} \binom{n+m}{k} x^k.$$

The coefficient of $x^k$ on the right-hand side is $\binom{n+m}{k}$.

Equating the two expressions for the coefficient of $x^k$, we obtain Vandermonde's convolution identity:

$$\boxed{\sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j} = \binom{n+m}{k}}.$$

## Special Case

When $n = m = k$, the identity reduces to

$$\sum_{j=0}^{n} \binom{n}{j} \binom{n}{n-j} = \binom{2n}{n}.$$

Since $\binom{n}{n-j} = \binom{n}{j}$, this becomes the well-known sum-of-squares identity:

$$\boxed{\sum_{j=0}^{n} \binom{n}{j}^2 = \binom{2n}{n}}.$$

$\square$
