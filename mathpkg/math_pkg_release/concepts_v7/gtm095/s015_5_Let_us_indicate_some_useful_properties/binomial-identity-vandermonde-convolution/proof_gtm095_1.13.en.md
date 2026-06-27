---
role: proof
locale: en
of_concept: binomial-identity-vandermonde-convolution
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Vandermonde's Convolution Identity via Generating Functions

## Statement

For nonnegative integers $n$, $m$, and $k$,

$$\sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j} = \binom{n+m}{k}.$$

## Proof

Start from the elementary identity

$$(1+x)^n(1+x)^m = (1+x)^{n+m}.$$

Expand each factor using the binomial theorem:

$$(1+x)^n = \sum_{j=0}^{n} \binom{n}{j} x^j, \qquad
(1+x)^m = \sum_{\ell=0}^{m} \binom{m}{\ell} x^\ell.$$

By the convolution property of generating functions (Section 5, equation (9)), the coefficient of $x^k$ in the product $(1+x)^n(1+x)^m$ is the convolution of the two binomial coefficient sequences:

$$[x^k]\,(1+x)^n(1+x)^m = \sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j},$$

with the understanding that $\binom{n}{j} = 0$ for $j > n$ and $\binom{m}{k-j} = 0$ for $k-j > m$.

On the other hand,

$$[x^k]\,(1+x)^{n+m} = \binom{n+m}{k}.$$

Equating the two expressions for the coefficient of $x^k$ yields Vandermonde's identity:

$$\boxed{\sum_{j=0}^{k} \binom{n}{j} \binom{m}{k-j} = \binom{n+m}{k}}.$$

## Corollary: Sum of squares of binomial coefficients

Setting $n = m = k$ and using $\binom{n}{n-j} = \binom{n}{j}$, we obtain the special case

$$\boxed{\sum_{j=0}^{n} \binom{n}{j}^2 = \binom{2n}{n}}.$$

This remarkable identity has a natural combinatorial interpretation: $\binom{2n}{n}$ counts the number of ways to select $n$ elements from a set of $2n$ elements, and the left-hand side partitions these selections according to how many elements are chosen from the first $n$ elements (say, $j$) and how many from the remaining $n$ (namely $n-j$). $\square$
