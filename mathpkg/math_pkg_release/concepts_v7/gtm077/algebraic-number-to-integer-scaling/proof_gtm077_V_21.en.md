---
role: proof
locale: en
of_concept: algebraic-number-to-integer-scaling
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 63: Scaling an Algebraic Number to an Integer

**Theorem (Theorem 63).** Every algebraic number $\alpha$ can be transformed into an algebraic integer by multiplication by a suitable nonzero rational integer.

*Proof.* Let $\alpha$ satisfy the equation

$$c_0 x^n + c_1 x^{n-1} + \cdots + c_{n-1} x + c_n = 0$$

with rational integral coefficients and $c_0 \neq 0$. Multiply both sides of the equation by $c_0^{n-1}$:

$$c_0^{n-1}(c_0 \alpha^n + c_1 \alpha^{n-1} + \cdots + c_n) = 0.$$

Rewrite the terms. For $y = c_0 \alpha$, we have $y^k = c_0^k \alpha^k$. Then

$$c_0^{n-1} \cdot c_k \alpha^{n-k} = c_k \cdot c_0^{n-1} \alpha^{n-k} = c_k \cdot c_0^{k-1} \cdot (c_0 \alpha)^{n-k} = c_k c_0^{k-1} y^{n-k}.$$

Thus the equation becomes

$$c_0^{n-1} c_0 \alpha^n + c_0^{n-1} c_1 \alpha^{n-1} + \cdots + c_0^{n-1} c_n = 0,$$

that is,

$$y^n + c_1 y^{n-1} + c_2 c_0 y^{n-2} + \cdots + c_n c_0^{n-1} = 0.$$

This is a monic polynomial equation for $y = c_0 \alpha$ with rational integer coefficients. Hence by Theorem 60, $y = c_0 \alpha$ is an algebraic integer. The rational integer $c_0 \neq 0$ serves as the scaling factor. ∎
