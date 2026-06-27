---
role: exercise
locale: en
chapter: "4"
section: "4.2"
exercise_number: 15
---

This exercise is devoted to the proof that cyclotomic integers satisfy no relations other than those found in the text. Let $f(\alpha) = 0$ be any relation of the type in question; that is, let $f(X)$ be a polynomial in one variable with integer coefficients which becomes zero when the complex number $\alpha$ is substituted for the variable $X$. Because $\alpha^\lambda = 1$, $\alpha^{\lambda+1} = \alpha$, etc., it can obviously be assumed that $f(X)$ has degree at most $\lambda-1$. It is to be shown that $f(X)$ must be a multiple of $X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$. Let $h(X) = X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$. There is an integer $a$ such that $f(X) - a h(X)$ has degree less than $\lambda-1$ and is zero when $X = \alpha$. Thus it will suffice to show that if $f(X)$ has degree less than $\lambda-1$ and $f(\alpha) = 0$ then $f(X)$ must be the polynomial $0$. Assume not. That is, assume $f(X) \neq 0$, $f(X)$ has degree less than $\lambda-1$, and $f(\alpha) = 0$. Then $a h(X) = q(X)f(X) + r(X)$ where $a$ is an integer, $q(X)$ and $r(X)$ are polynomials with integer coefficients, and $r(X)$ is of lower degree than $f(X)$. If $r(X) \neq 0$ replace $f(X)$ by $r(X)$ and repeat. Since the degree decreases at each step, eventually $r(X) = 0$. Then $a h(X) = q(X)f(X)$. Substituting $X = \alpha$ and using $f(\alpha) = 0$ gives $a h(\alpha) = 0$. But $h(\alpha) = 0$, so this gives no information about $a$. Instead, use the irreducibility of $h(X)$ over $\mathbb{Q}$ (for prime $\lambda$) to conclude that a contradiction arises unless $f(X)$ is identically zero. Conclude that $f(X)$ must be a multiple of $h(X)$.
