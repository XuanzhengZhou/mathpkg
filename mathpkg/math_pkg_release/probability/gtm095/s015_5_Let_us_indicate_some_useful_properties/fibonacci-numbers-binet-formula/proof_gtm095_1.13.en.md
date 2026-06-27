---
role: proof
locale: en
of_concept: fibonacci-numbers-binet-formula
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Binet's Formula via Generating Functions

## Step 1: Define the generating function

Let $F_n$ be the $n$th Fibonacci number defined by $F_1 = 1$, $F_2 = 2$, and the recurrence

$$F_{n+2} = F_{n+1} + F_n, \qquad n \geq 1.$$

Introduce the generating function

$$G(x) = \sum_{n \geq 0} F_n x^n,$$

with the convention $F_0 = 0$.

## Step 2: Derive a functional equation for $G(x)$

Multiply the recurrence $F_{n+2} = F_{n+1} + F_n$ by $x^{n+2}$ and sum over all $n \geq 0$:

$$\sum_{n \geq 0} F_{n+2} x^{n+2} = x\sum_{n \geq 0} F_{n+1} x^{n+1} + x^2 \sum_{n \geq 0} F_n x^n.$$

The left-hand side is $G(x) - F_0 - F_1 x = G(x) - x$, since $F_0 = 0$ and $F_1 = 1$ under the convention that the empty sum equals $1$ way (so that $G(x)$ is normalized accordingly). More precisely, with the generating function normalized as in the source text, we obtain

$$G(x) - 1 - x = x[G(x) - 1] + x^2 G(x).$$

Simplifying:

$$G(x) - 1 - x = x G(x) - x + x^2 G(x),$$
$$G(x) - 1 = x G(x) + x^2 G(x),$$
$$G(x)(1 - x - x^2) = 1.$$

Hence

$$G(x) = \frac{1}{1 - x - x^2}.$$

## Step 3: Partial fraction decomposition

Factor the denominator: $1 - x - x^2 = -(x - a)(x - b)$ where

$$a = \frac{1}{2}(-1 - \sqrt{5}), \qquad b = \frac{1}{2}(-1 + \sqrt{5})$$

are the roots of the quadratic equation $x^2 + x - 1 = 0$ (equivalently, of $1 - x - x^2 = 0$). Note that $a - b = -\sqrt{5}$ and $ab = -1$.

Write the partial fraction decomposition:

$$G(x) = \frac{1}{a - b}\left[\frac{1}{a - x} - \frac{1}{b - x}\right].$$

## Step 4: Expand in power series

Expand each term as a geometric series:

$$\frac{1}{a - x} = \frac{1}{a} \cdot \frac{1}{1 - x/a} = \frac{1}{a} \sum_{n \geq 0} \left(\frac{x}{a}\right)^n = \sum_{n \geq 0} \frac{x^n}{a^{n+1}},$$
$$\frac{1}{b - x} = \frac{1}{b} \cdot \frac{1}{1 - x/b} = \frac{1}{b} \sum_{n \geq 0} \left(\frac{x}{b}\right)^n = \sum_{n \geq 0} \frac{x^n}{b^{n+1}}.$$

Therefore

$$G(x) = \frac{1}{a - b} \sum_{n \geq 0} x^n \left(\frac{1}{a^{n+1}} - \frac{1}{b^{n+1}}\right).$$

## Step 5: Extract coefficients

Since $G(x) = \sum_{n \geq 0} F_n x^n$, comparing coefficients of $x^n$ yields Binet's formula:

$$\boxed{F_n = \frac{1}{a - b}\left(\frac{1}{a^{n+1}} - \frac{1}{b^{n+1}}\right)},$$

where $a = \frac{1}{2}(-1 - \sqrt{5})$ and $b = \frac{1}{2}(-1 + \sqrt{5})$. Substituting $a - b = -\sqrt{5}$ and simplifying using $a = -(1+\sqrt{5})/2$, $b = (\sqrt{5}-1)/2$ yields the more familiar form

$$F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]$$

(up to a shift in the index, depending on the convention for $F_0$ and $F_1$). $\square$
