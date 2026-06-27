---
role: proof
locale: en
of_concept: fibonacci-numbers-closed-form
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of the Closed Form of Fibonacci Numbers

## Step 1: Recurrence and generating function

Let $F_n$ be the Fibonacci numbers with $F_0 = 0$, $F_1 = 1$, satisfying

$$F_{n+2} = F_{n+1} + F_n, \qquad n \geq 0.$$

Define the generating function

$$G(x) = \sum_{n=0}^{\infty} F_n x^n = F_0 + F_1 x + F_2 x^2 + \cdots.$$

## Step 2: Derive an equation for $G(x)$

Multiply the recurrence by $x^{n+2}$ and sum over $n \geq 0$:

$$\sum_{n=0}^{\infty} F_{n+2} x^{n+2} = x\sum_{n=0}^{\infty} F_{n+1} x^{n+1} + x^2\sum_{n=0}^{\infty} F_n x^n.$$

Recognize the sums in terms of $G(x)$:

$$\sum_{n=0}^{\infty} F_{n+2} x^{n+2} = G(x) - F_0 - F_1 x = G(x) - x,$$
$$\sum_{n=0}^{\infty} F_{n+1} x^{n+1} = G(x) - F_0 = G(x),$$
$$\sum_{n=0}^{\infty} F_n x^n = G(x).$$

Substituting, we obtain

$$G(x) - x = x G(x) + x^2 G(x).$$

Solving for $G(x)$:

$$G(x) - x G(x) - x^2 G(x) = x,$$
$$G(x)(1 - x - x^2) = x,$$

$$\boxed{G(x) = \frac{x}{1 - x - x^2}}.$$

## Step 3: Factor the denominator

The denominator $1 - x - x^2$ has roots

$$\alpha = \frac{-1 + \sqrt{5}}{2}, \qquad \beta = \frac{-1 - \sqrt{5}}{2}.$$

Note that $\alpha\beta = -1$ and $\alpha - \beta = \sqrt{5}$. Moreover, $1/\alpha = (\sqrt{5}+1)/2 = \phi$ (the golden ratio) and $-1/\beta = (\sqrt{5}-1)/2 = 1/\phi$.

We can write $1 - x - x^2 = (1 - \phi^{-1} x)(1 + \beta^{-1} x)$ or equivalently

$$1 - x - x^2 = -(x - \alpha)(x - \beta).$$

## Step 4: Partial fraction decomposition

Decompose $G(x)$ using partial fractions:

$$G(x) = \frac{x}{1 - x - x^2} = \frac{1}{\alpha - \beta}\left[\frac{1}{1 - \alpha^{-1}x} - \frac{1}{1 - \beta^{-1}x}\right].$$

Since $\alpha - \beta = \sqrt{5}$, and noting that $\phi = (1+\sqrt{5})/2 = -1/\beta$ and $\psi = (1-\sqrt{5})/2 = -1/\alpha$,

$$G(x) = \frac{1}{\sqrt{5}}\left[\frac{1}{1 - \phi x} - \frac{1}{1 - \psi x}\right].$$

## Step 5: Expand as power series

Expand each term as a geometric series:

$$\frac{1}{1 - \phi x} = \sum_{n=0}^{\infty} \phi^n x^n, \qquad \frac{1}{1 - \psi x} = \sum_{n=0}^{\infty} \psi^n x^n.$$

Therefore

$$G(x) = \frac{1}{\sqrt{5}} \sum_{n=0}^{\infty} (\phi^n - \psi^n) x^n.$$

## Step 6: Extract coefficients

Comparing with $G(x) = \sum_{n=0}^{\infty} F_n x^n$, we obtain Binet's closed-form formula:

$$\boxed{F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]}.$$

This formula expresses the $n$th Fibonacci number as an explicit combination of powers of the golden ratio $\phi = (1+\sqrt{5})/2$ and its conjugate $\psi = (1-\sqrt{5})/2$. $\square$
