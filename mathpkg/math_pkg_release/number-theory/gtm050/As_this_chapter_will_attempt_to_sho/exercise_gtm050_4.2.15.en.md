---
role: exercise
locale: en
chapter: "4"
section: "4.2"
exercise_number: 15
---

This exercise is devoted to the proof that cyclotomic integers satisfy no relations other than those found in the text. Let $f(\alpha) = 0$ be any relation of the type in question; that is, let $f(X)$ be a polynomial in one variable with integer coefficients which becomes zero when the complex number $\alpha$ is substituted for the variable $X$. Because $\alpha^{\lambda} = 1$, it can obviously be assumed that $f(X)$ has degree at most $\lambda - 1$. It is to be shown that $f(X)$ must be a multiple of $X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$.

Let $h(X) = X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$. There is an integer $a$ such that $f(X) - a h(X)$ has degree less than $\lambda - 1$ and is zero when $X = \alpha$. Thus it will suffice to show that if $f(X)$ has degree less than $\lambda - 1$ and $f(\alpha) = 0$, then $f(X)$ must be the zero polynomial. Assume not; that is, assume $f(X) \not\equiv 0$, $f(X)$ has degree less than $\lambda - 1$, and $f(\alpha) = 0$. Then $a h(X) = q(X)f(X) + r(X)$ where $a$ is an integer, $q(X)$ and $r(X)$ are polynomials with integer coefficients, and $r(X)$ is of lower degree than $f(X)$. If $r(X) \not\equiv 0$, replace $f(X)$ by $r(X)$ and repeat the process. This is the Euclidean algorithm, which must terminate, producing a contradiction because it would yield a nonzero polynomial of degree $0$ vanishing at $\alpha$. Therefore $f(X)$ must be the zero polynomial.
