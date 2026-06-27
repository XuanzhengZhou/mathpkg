---
role: proof
locale: en
of_concept: random-variable-19
source_book: gtm095
source_chapter: "II"
source_section: "4"
---

# Proof of Corollary (Conditional Expectation via Density)

**Corollary.** Let $\mathcal{G} = \mathcal{G}_\eta$, where $\eta$ is a random variable, and let the pair $(\xi, \eta)$ have a probability distribution with density $f_{\xi,\eta}(x, y)$. Let $E|g(\xi)| < \infty$. Then

$$E(g(\xi) \mid \eta = y) = \int_{-\infty}^{\infty} g(x) \, f_{\xi \mid \eta}(x \mid y) \, dx,$$

where $f_{\xi \mid \eta}(x \mid y)$ is the density of the conditional distribution (see (18)).

*Proof.* By Theorem 3 (or the definition of conditional expectation via regular conditional probabilities), for any $B \in \mathcal{B}(R)$,

$$\int_{\{\omega : \eta \in B\}} g(\xi) \, dP = \int_B E(g(\xi) \mid \eta = y) \, P_\eta(dy).$$

On the other hand, by the formula for change of variable in Lebesgue integrals and the definition of the joint density,

$$\int_{\{\omega : \eta \in B\}} g(\xi) \, dP = \iint_{R \times B} g(x) \, f_{\xi,\eta}(x, y) \, dx \, dy = \int_B \left( \int_{-\infty}^{\infty} g(x) \, f_{\xi,\eta}(x, y) \, dx \right) dy.$$

Since $P_\eta(dy) = f_\eta(y) \, dy$, where $f_\eta(y) = \int_{-\infty}^{\infty} f_{\xi,\eta}(x, y) \, dx$, and $f_{\xi \mid \eta}(x \mid y) = f_{\xi,\eta}(x, y) / f_\eta(y)$ (with the convention $f_{\xi \mid \eta}(x \mid y) = 0$ when $f_\eta(y) = 0$), we have

$$\int_{-\infty}^{\infty} g(x) \, f_{\xi,\eta}(x, y) \, dx = f_\eta(y) \int_{-\infty}^{\infty} g(x) \, f_{\xi \mid \eta}(x \mid y) \, dx.$$

Hence

$$\int_{\{\omega : \eta \in B\}} g(\xi) \, dP = \int_B \left( \int_{-\infty}^{\infty} g(x) \, f_{\xi \mid \eta}(x \mid y) \, dx \right) P_\eta(dy).$$

Comparing with the first equality, since $B \in \mathcal{B}(R)$ is arbitrary, we obtain

$$E(g(\xi) \mid \eta = y) = \int_{-\infty}^{\infty} g(x) \, f_{\xi \mid \eta}(x \mid y) \, dx \quad (P_\eta\text{-a.s.}),$$

as required.
