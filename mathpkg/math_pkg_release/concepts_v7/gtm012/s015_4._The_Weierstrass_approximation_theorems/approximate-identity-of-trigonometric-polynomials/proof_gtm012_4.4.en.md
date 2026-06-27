---
role: proof
locale: en
of_concept: approximate-identity-of-trigonometric-polynomials
source_book: gtm012
source_chapter: "4"
source_section: "4. The Weierstrass approximation theorems"
---

# Proof of Lemma 4.1: Existence of an Approximate Identity of Trigonometric Polynomials

We want to choose a non-negative trigonometric polynomial $\varphi$ such that

$$\varphi(0) = \varphi(2\pi) = 1,$$
$$\varphi(x) < 1 \quad \text{for} \quad 0 < x < 2\pi.$$

Then successive powers of $\varphi$ will take values at points near $0$ and $2\pi$ which are relatively much greater than those taken at points between $0$ and $2\pi$.

We take

$$\varphi(x) = \frac{1}{2}(1 + \cos x)$$

and set

$$\varphi_n(x) = c_n(1 + \cos x)^n$$

where $c_n$ is chosen so that

$$\int_0^{2\pi} \varphi_n(x) \, dx = 2\pi.$$

We need to show that for each $0 < \delta < \pi$,

$$\int_{\delta}^{2\pi - \delta} \varphi_n(x) \, dx \to 0 \quad \text{as} \quad n \to \infty.$$

There is a number $r$, $0 < r < 1$, such that

$$1 + \cos x < r(1 + \cos y)$$

if

$$x \in [\delta, 2\pi - \delta], \quad y \in \left[0, \tfrac{1}{2}\delta\right].$$

Then these inequalities imply

$$\varphi_n(x) = c_n(1 + \cos x)^n \leq r^n \varphi_n(y),$$

so

$$\frac{1}{2}\delta \, \varphi_n(x) \leq r^n \int_0^{\frac{1}{2}\delta} \varphi_n(y) \, dy \leq 2\pi r^n,$$

or

$$\varphi_n(x) \leq 4\pi \delta^{-1} r^n, \quad x \in [\delta, 2\pi - \delta].$$

Thus $\varphi_n \to 0$ uniformly on $[\delta, 2\pi - \delta]$, which together with the normalization condition $\int_0^{2\pi} \varphi_n = 2\pi$ and the fact that each $\varphi_n$ is a non-negative trigonometric polynomial, shows that $(\varphi_n)_{1}^{\infty}$ is an approximate identity consisting of trigonometric polynomials.
