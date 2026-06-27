---
role: proof
locale: en
of_concept: density-transformation-formula
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Density Transformation Formula

Let $\xi$ be a random variable with distribution function $F_\xi(x)$ (and density $f_\xi(x)$, if it exists). Let $\varphi = \varphi(x)$ be a Borel function, and define $\eta = \varphi(\xi)$.

We wish to express the distribution function $F_\eta(y)$ (and density $f_\eta(y)$, when it exists) in terms of $F_\xi$ and $\varphi$.

**Proof.** Let $I_y = (-\infty, y]$. By definition of the distribution function,

$$
F_\eta(y) = P(\eta \leq y) = P(\varphi(\xi) \in I_y) = P(\xi \in \varphi^{-1}(I_y)).
$$

The last probability is, by definition of the distribution of $\xi$, the integral of the measure induced by $F_\xi$ over the set $\varphi^{-1}(I_y)$:

$$
\boxed{F_\eta(y) = \int_{\varphi^{-1}(I_y)} F_\xi(dx)}.
$$

This is the fundamental formula relating the distribution of $\eta = \varphi(\xi)$ to that of $\xi$.

**Special cases.** When $\xi$ has a density $f_\xi$ and $\varphi$ is sufficiently regular (e.g., continuously differentiable and strictly monotone), one can differentiate this formula to obtain the density $f_\eta(y)$. The resulting formulas are:

- **Linear transformation:** If $\eta = a\xi + b$ with $a > 0$, then $\varphi^{-1}(I_y) = (-\infty, (y-b)/a]$, and
  $$
  F_\eta(y) = F_\xi\!\left(\frac{y-b}{a}\right), \qquad
  f_\eta(y) = \frac{1}{|a|}\,f_\xi\!\left(\frac{y-b}{a}\right) \text{ (if the density exists)}.
  $$

- **Square:** If $\eta = \xi^2$, then for $y \geq 0$,
  $$
  F_\eta(y) = P(-\sqrt{y} \leq \xi \leq \sqrt{y}) = F_\xi(\sqrt{y}) - F_\xi(-\sqrt{y}) + P(\xi = -\sqrt{y}),
  $$
  and $F_\eta(y) = 0$ for $y < 0$.

- **Strictly monotone transformation (Formula (22)):** If $\varphi$ is continuously differentiable and strictly monotone on the range $(a,b)$ of $\xi$, with inverse $h$, then
  $$
  f_\eta(y) = f_\xi(h(y))\,|h'(y)|.
  $$

- **Piecewise monotone transformation (Formula (24)):** If $\varphi$ is piecewise strictly monotone on intervals $I_k = (a_k, b_k)$ with inverses $h_k$, then
  $$
  f_\eta(y) = \sum_{k=1}^{n} f_\xi(h_k(y))\,|h'_k(y)| \cdot I_{D_k}(y),
  $$
  where $D_k = \varphi(I_k)$.

This general framework unifies all the specific density transformation formulas derived in this section.
