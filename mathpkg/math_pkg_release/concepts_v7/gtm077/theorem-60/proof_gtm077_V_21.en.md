---
role: proof
locale: en
of_concept: theorem-60
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 60

**Theorem (Theorem 60).** If $\alpha$ satisfies any equation at all with integral coefficients whose leading coefficient is equal to $1$, then $\alpha$ is an integer.

*Proof.* Let

$$\varphi(x) = x^N + a_1 x^{N-1} + \cdots + a_N$$

with rational integral $a_i$ and $\varphi(\alpha) = 0$. Moreover let

$$f(x) = c_0 x^n + c_1 x^{n-1} + \cdots + c_n$$

be the irreducible polynomial in $k(1)$ which has $\alpha$ as a root and in which the $c_i$ are already assumed to be relatively prime rational integers, with $c_0 > 0$. By Theorem 49 we have $f(x) \mid \varphi(x)$. Thus

$$\frac{\varphi(x)}{f(x)} = \frac{b' g(x)}{b}$$

is a rational polynomial over $k(1)$ where we may assume the polynomial $g(x)$ to be integral with relatively prime coefficients, by suitable choice of the rational integers $b$ and $b'$. It follows from

$$b \varphi(x) = b' f(x) g(x)$$

that $b = b'$, since, by Theorem 13a, $f(x) \cdot g(x)$, as a product of two primitive polynomials, is again primitive, and $\varphi(x)$ is also primitive (its coefficients are integers with leading coefficient $1$, hence relatively prime). Moreover, by comparing leading coefficients we learn from $\varphi(x) = f(x) g(x)$ that $c_0$ must divide the leading coefficient of $\varphi$, which is $1$; hence $c_0 = 1$, completing the proof. ∎
