---
role: proof
locale: en
of_concept: clearing-denominators
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Clearing Denominators for Algebraic Numbers

**Theorem (Theorem 63).** Every algebraic number $\alpha$ can be transformed into an algebraic integer by multiplication by a suitable nonzero rational integer. That is, there exists a positive integer $m$ such that $m\alpha$ is an algebraic integer.

*Proof.* Since $\alpha$ is an algebraic number, it satisfies a polynomial equation with rational integer coefficients:

$$c_0 x^n + c_1 x^{n-1} + \cdots + c_{n-1} x + c_n = 0, \qquad c_0 \neq 0.$$

Rewrite this as

$$c_0 \alpha^n + c_1 \alpha^{n-1} + \cdots + c_n = 0.$$

Multiply through by $c_0^{n-1}$:

$$c_0^n \alpha^n + c_1 c_0^{n-1} \alpha^{n-1} + c_2 c_0^{n-1} \alpha^{n-2} + \cdots + c_n c_0^{n-1} = 0.$$

Let $y = c_0 \alpha$. Then $y^k = c_0^k \alpha^k$ for each $k$, and the equation becomes

$$y^n + c_1 y^{n-1} + c_2 c_0 y^{n-2} + \cdots + c_n c_0^{n-1} = 0.$$

Each coefficient $c_k c_0^{k-1}$ (with $c_0^0 = 1$) is a rational integer. Therefore $y$ satisfies a monic polynomial with rational integer coefficients. By Theorem 60, $y = c_0 \alpha$ is an algebraic integer. Taking $m = c_0$ (or $m = |c_0|$ for a positive integer) yields the desired scaling factor. ∎
