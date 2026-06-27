---
role: proof
locale: en
of_concept: integer-root-of-monic-polynomial
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 60: Monic Integer Polynomial Implies Integer Root

**Theorem.** If a number satisfies any equation with rational integer coefficients and leading coefficient $1$, then it is an algebraic integer.

*Proof.* Let $\alpha$ satisfy

$$\varphi(x) = x^N + a_1 x^{N-1} + \cdots + a_N = 0$$

where the $a_i$ are rational integers. Let

$$f(x) = c_0 x^n + c_1 x^{n-1} + \cdots + c_n$$

be the irreducible polynomial in $k(1)$ which has $\alpha$ as a root, where the $c_i$ are relatively prime rational integers and $c_0 > 0$. By Theorem 49 (Gauss's Lemma on divisibility of polynomials), $f(x)$ divides $\varphi(x)$ in $k(1)[x]$. Thus

$$\frac{\varphi(x)}{f(x)} = \frac{b' g(x)}{b}$$

with rational integers $b, b'$ and $g(x)$ a primitive polynomial with integer coefficients. From $b\varphi(x) = b' f(x) g(x)$ we obtain $b = b'$, since both $f(x)g(x)$ (as a product of primitive polynomials, Theorem 13a) and $\varphi(x)$ (monic with integer coefficients) are primitive. Hence $\varphi(x) = f(x) g(x)$. Comparing leading coefficients, $c_0$ times the leading coefficient of $g(x)$ equals $1$, so $c_0 = 1$. Therefore $\alpha$ satisfies a monic irreducible polynomial with rational integer coefficients, i.e., $\alpha$ is an algebraic integer. ∎
