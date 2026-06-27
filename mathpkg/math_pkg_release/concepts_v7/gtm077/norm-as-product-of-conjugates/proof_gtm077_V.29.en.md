---
role: proof
locale: en
of_concept: norm-as-product-of-conjugates
source_book: gtm077
source_chapter: "V"
source_section: "29"
---
# Proof of Theorem 88: Norm as Product of Conjugate Ideals

Let $\mathfrak{a} = (\alpha_1, \ldots, \alpha_r)$ be an ideal of the number field $K$ of degree $n$. Form the polynomial

$$P(x) = \alpha_1 x + \alpha_2 x^2 + \cdots + \alpha_r x^r$$

from a new variable $x$, where $\alpha = (\alpha_1, \ldots, \alpha_r)$ denotes the ideal with the GCD of the coefficients equal to $\mathfrak{a}$.

The product of the conjugate polynomials

$$f(x) = \prod_{i=1}^{n} (\alpha_1^{(i)} x + \cdots + \alpha_r^{(i)} x^r)$$

is a polynomial with rational integral coefficients. Let $a$ be the GCD of these coefficients, so that $a$ is a rational integer. Since $1$ is a linear combination of the coefficients of $(1/a)f(x)$, the ideal $(a)$ is also the GCD of the coefficients taken as an ideal in $K$. Hence, by Theorem 87,

$$\mathfrak{a}^{(1)} \mathfrak{a}^{(2)} \cdots \mathfrak{a}^{(n)} = (a).$$

Now the conjugates all have equal norm, so applying

$$N(\mathfrak{a}^{(1)}) \cdots N(\mathfrak{a}^{(n)}) = N(\mathfrak{a}^{(i)})^n = N((a)) = |a|^n$$

we obtain

$$N(\mathfrak{a}^{(i)}) = \pm a, \quad (N(\mathfrak{a}^{(i)})) = (a) = \mathfrak{a}^{(1)} \cdots \mathfrak{a}^{(n)}$$

for each $i$. This completes the proof.

In particular, for a prime ideal $\mathfrak{p}$ of degree $f$,

$$p^f = N(\mathfrak{p}) = \mathfrak{p}^{(1)} \cdots \mathfrak{p}^{(n)}.$$

Consequently, no prime ideals other than the conjugate prime ideals divide $p$. Furthermore, if $p$ is not divisible by the square of any prime ideal, then among the $n$ conjugates $\mathfrak{p}^{(1)}, \ldots, \mathfrak{p}^{(n)}$ each distinct one is repeated $f$ times, and $p$ is the product of the $k = n/f$ distinct prime ideals.
