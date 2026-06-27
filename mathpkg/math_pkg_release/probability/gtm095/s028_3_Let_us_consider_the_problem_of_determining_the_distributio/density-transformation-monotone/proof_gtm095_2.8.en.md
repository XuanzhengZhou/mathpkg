---
role: proof
locale: en
of_concept: density-transformation-monotone
source_book: gtm095
source_chapter: "2"
source_section: "8. Random Variables: II"
---

# Proof of Density Transformation Formula (Monotone Case)

Let $\xi$ be a random variable whose range is a (finite or infinite) open interval $I = (a, b)$, with density $f_\xi(x)$. Let $\varphi = \varphi(x)$ be a continuously differentiable function on $(a, b)$ that is either strictly increasing or strictly decreasing, and let $\varphi'(x) \neq 0$ for $x \in (a, b)$. Denote by $h = h(y)$ the inverse function of $\varphi$, so that $h(\varphi(x)) = x$ for all $x \in (a, b)$.

We must determine the density $f_\eta(y)$ of $\eta = \varphi(\xi)$.

**Case 1: $\varphi$ is strictly increasing.** Then $\varphi'(x) > 0$ and $h'(y) > 0$. Since $\varphi$ is increasing,

$$
F_\eta(y) = P(\eta \leq y) = P(\varphi(\xi) \leq y) = P(\xi \leq h(y)) = F_\xi(h(y)).
$$

Differentiating with respect to $y$, we obtain

$$
f_\eta(y) = \frac{d}{dy} F_\xi(h(y)) = f_\xi(h(y)) \, h'(y).
$$

Since $h'(y) > 0$, we have $h'(y) = |h'(y)|$, and therefore

$$
f_\eta(y) = f_\xi(h(y)) \, |h'(y)|.
$$

**Case 2: $\varphi$ is strictly decreasing.** Then $\varphi'(x) < 0$ and $h'(y) < 0$. Since $\varphi$ is decreasing,

$$
\begin{aligned}
F_\eta(y) &= P(\eta \leq y) = P(\varphi(\xi) \leq y) = P(\xi \geq h(y)) \\
&= 1 - P(\xi < h(y)) = 1 - F_\xi(h(y)) + P(\xi = h(y)).
\end{aligned}
$$

Because $\xi$ possesses a density, $P(\xi = h(y)) = 0$, so $F_\eta(y) = 1 - F_\xi(h(y))$.

Differentiating with respect to $y$,

$$
f_\eta(y) = \frac{d}{dy}\bigl[1 - F_\xi(h(y))\bigr] = -f_\xi(h(y)) \, h'(y).
$$

Since $h'(y) < 0$ in the decreasing case, $-h'(y) = |h'(y)|$, and we again obtain

$$
f_\eta(y) = f_\xi(h(y)) \, |h'(y)|.
$$

Hence in either case

$$
\boxed{f_{\eta}(y) = f_{\xi}(h(y))\,|h'(y)|}. \tag{22}
$$

This is the density transformation formula for a strictly monotone transformation of a random variable.

**Example.** If $\eta = a\xi + b$ with $a \neq 0$, then $\varphi(x) = ax + b$, $h(y) = (y - b)/a$, and $h'(y) = 1/a$, so

$$
f_\eta(y) = \frac{1}{|a|}\, f_\xi\!\left(\frac{y - b}{a}\right).
$$
