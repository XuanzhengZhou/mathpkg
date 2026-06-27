---
role: proof
locale: en
of_concept: inversion-formula
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 3 (Inversion Formula)

Let $F = F(x)$ be a distribution function and $\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x)$ its characteristic function.

**(a)** For any pair of points $a$ and $b$ ($a < b$) at which $F = F(x)$ is continuous,

$$F(b) - F(a) = \lim_{c \to \infty} \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} \varphi(t) dt. \tag{25}$$

**(b)** If $\int_{-\infty}^{\infty} |\varphi(t)| dt < \infty$, the distribution function $F(x)$ has a density $f(x)$,

$$F(x) = \int_{-\infty}^{x} f(y) dy$$

and

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx} \varphi(t) dt. \tag{27}$$

## Proof

First, a heuristic motivation: if $F$ has density $f$, then

$$F(b) - F(a) = \int_{a}^{b} f(x) dx = \frac{1}{2\pi} \int_{a}^{b} \left[ \int_{-\infty}^{\infty} e^{-itx} \varphi(t) dt \right] dx$$
$$= \frac{1}{2\pi} \int_{-\infty}^{\infty} \varphi(t) \left[ \int_{a}^{b} e^{-itx} dx \right] dt$$
$$= \frac{1}{2\pi} \int_{-\infty}^{\infty} \varphi(t) \frac{e^{-ita} - e^{-itb}}{it} dt.$$

**(a)** Define

$$\Phi_c = \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} \varphi(t) dt$$
$$= \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} \left[ \int_{-\infty}^{\infty} e^{itx} dF(x) \right] dt$$
$$= \frac{1}{2\pi} \int_{-\infty}^{\infty} \left[ \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} e^{itx} dt \right] dF(x)$$
$$= \int_{-\infty}^{\infty} \Psi_c(x) dF(x),$$

where

$$\Psi_c(x) = \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} e^{itx} dt$$

and Fubini's theorem is applicable because

$$\left| \frac{e^{-ita} - e^{-itb}}{it} \cdot e^{itx} \right| = \left| \frac{e^{-ita} - e^{-itb}}{it} \right| \leq b - a.$$

Now,

$$\Psi_c(x) = \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{it(x-a)} - e^{it(x-b)}}{it} dt = \frac{1}{\pi} \int_{0}^{c} \frac{\sin t(x-a) - \sin t(x-b)}{t} dt.$$

Using the Dirichlet integral $\int_{0}^{\infty} \frac{\sin \alpha t}{t} dt = \frac{\pi}{2} \operatorname{sgn}(\alpha)$, we obtain, as $c \to \infty$:

$$\Psi_c(x) \to \Psi(x),$$

where

$$\Psi(x) = \begin{cases} 0, & x < a \text{ or } x > b, \\ \frac{1}{2}, & x = a \text{ or } x = b, \\ 1, & a < x < b. \end{cases}$$

There is a constant $C$ such that $|\Psi_c(x)| < C < \infty$ for all $c$ and $x$. Let $\mu$ be the measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ such that $\mu(a, b] = F(b) - F(a)$. By assumption $a$ and $b$ are continuity points of $F(x)$, hence $\mu\{a\} = \mu\{b\} = 0$. By the dominated convergence theorem,

$$\Phi_c = \int_{-\infty}^{\infty} \Psi_c(x) dF(x) \to \int_{-\infty}^{\infty} \Psi(x) dF(x)$$
$$= \mu(a, b) + \frac{1}{2}\mu\{a\} + \frac{1}{2}\mu\{b\} = F(b) - F(a).$$

Hence (25) is established.

**(b)** Let $\int_{-\infty}^{\infty} |\varphi(t)| dt < \infty$. Write

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx} \varphi(t) dt.$$

By the dominated convergence theorem, $f(x)$ is a continuous function of $x$. From part (a), for $a < b$,

$$F(b) - F(a) = \lim_{c \to \infty} \frac{1}{2\pi} \int_{-c}^{c} \frac{e^{-ita} - e^{-itb}}{it} \varphi(t) dt$$
$$= \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-ita} - e^{-itb}}{it} \varphi(t) dt$$
$$= \int_{a}^{b} \left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx} \varphi(t) dt \right] dx = \int_{a}^{b} f(x) dx.$$

Hence

$$F(x) = \int_{-\infty}^{x} f(y) dy, \quad x \in \mathbb{R},$$

and since $f(x)$ is continuous and $F(x)$ is nondecreasing, $f(x)$ is the density of $F(x)$. This completes the proof.
