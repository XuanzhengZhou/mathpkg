---
role: proof
locale: en
of_concept: convolution-densities
source_book: gtm095
source_chapter: "2"
source_section: "8. Random Variables: II"
---

# Proof of Convolution Formula for Densities

Let $\xi$ and $\eta$ be independent random variables with distribution functions $F_\xi$, $F_\eta$ and densities $f_\xi$, $f_\eta$, respectively. Set $\zeta = \xi + \eta$.

**Step 1: Distribution function of the sum.** From the general formula for the distribution of a function of two variables (equation (29)),

$$
F_\zeta(z) = \iint_{\{(x,y): x+y \leq z\}} dF_\xi(x)\,dF_\eta(y).
$$

Since $\xi$ and $\eta$ are independent, their joint distribution factorizes. Using Fubini's theorem,

$$
\begin{aligned}
F_\zeta(z) &= \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{z-x} dF_\eta(y) \right] dF_\xi(x) \\
&= \int_{-\infty}^{\infty} F_\eta(z-x)\,dF_\xi(x). \tag{30}
\end{aligned}
$$

By symmetry, exchanging the roles of $\xi$ and $\eta$,

$$
F_\zeta(z) = \int_{-\infty}^{\infty} F_\xi(z-y)\,dF_\eta(y). \tag{31}
$$

The function $H(z) = \int_{-\infty}^{\infty} F(z-x)\,dG(x)$ is called the **convolution** of the distribution functions $F$ and $G$, denoted $F * G$. Thus

$$
F_\zeta = F_\xi * F_\eta.
$$

It is straightforward to verify that $F_\xi * F_\eta = F_\eta * F_\xi$, i.e., convolution of distribution functions is commutative.

**Step 2: Density of the sum.** Since $\xi$ and $\eta$ possess densities, $dF_\xi(x) = f_\xi(x)\,dx$ and $dF_\eta(y) = f_\eta(y)\,dy$. Substituting into (30),

$$
F_\zeta(z) = \int_{-\infty}^{\infty} F_\eta(z-x)\,f_\xi(x)\,dx.
$$

Differentiating with respect to $z$ under the integral sign (justified by the dominated convergence theorem, since $f_\eta$ is integrable and $f_\xi$ is integrable),

$$
\begin{aligned}
f_\zeta(z) &= \frac{d}{dz} F_\zeta(z)
= \int_{-\infty}^{\infty} \frac{d}{dz} F_\eta(z-x)\,f_\xi(x)\,dx \\
&= \int_{-\infty}^{\infty} f_\eta(z-x)\,f_\xi(x)\,dx. \tag{32}
\end{aligned}
$$

Similarly, from (31) we obtain the symmetric form

$$
\boxed{f_\zeta(z) = \int_{-\infty}^{\infty} f_\xi(z-y)\,f_\eta(y)\,dy = \int_{-\infty}^{\infty} f_\eta(z-x)\,f_\xi(x)\,dx}. \tag{33}
$$

The density of the sum of two independent random variables is the **convolution** of their densities:

$$
f_{\xi+\eta} = f_\xi * f_\eta.
$$

**Remark.** The same result extends by induction to the sum of $n$ independent random variables with densities; the density of the sum is the $n$-fold convolution of the individual densities.
