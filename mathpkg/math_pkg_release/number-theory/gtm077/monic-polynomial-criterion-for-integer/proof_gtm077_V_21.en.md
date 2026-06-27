---
role: proof
locale: en
of_concept: monic-polynomial-criterion-for-integer
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of the Monic Polynomial Criterion for Algebraic Integers

**Theorem (Theorem 60).** If $\alpha$ satisfies any equation with rational integral coefficients whose leading coefficient is $1$, then $\alpha$ is an algebraic integer. This criterion avoids verifying irreducibility of the defining polynomial.

*Proof.* Suppose $\varphi(x) = x^N + a_1 x^{N-1} + \cdots + a_N$ has rational integer coefficients and $\varphi(\alpha) = 0$. Let

$$f(x) = c_0 x^n + c_1 x^{n-1} + \cdots + c_n$$

be the irreducible polynomial in $k(1)$ having $\alpha$ as a root, with $c_i$ relatively prime rational integers and $c_0 > 0$. By Theorem 49, $f(x) \mid \varphi(x)$ in $k(1)[x]$. Writing the quotient as a rational function and clearing denominators:

$$\frac{\varphi(x)}{f(x)} = \frac{b' g(x)}{b}$$

with $b, b'$ rational integers and $g(x)$ primitive with integer coefficients. Then

$$b \varphi(x) = b' f(x) g(x).$$

Since $f(x)$ and $g(x)$ are primitive, their product is primitive (Theorem 13a); $\varphi(x)$ is also primitive (monic with integer coefficients). Hence $b = b'$ and $\varphi(x) = f(x) g(x)$. Comparing leading coefficients, $c_0$ must divide the leading coefficient $1$ of $\varphi$, so $c_0 = 1$. Thus the irreducible polynomial for $\alpha$ is monic with rational integer coefficients, i.e., $\alpha$ is an algebraic integer. ∎
