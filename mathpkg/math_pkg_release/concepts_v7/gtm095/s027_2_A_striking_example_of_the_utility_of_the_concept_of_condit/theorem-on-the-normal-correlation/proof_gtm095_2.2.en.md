---
role: proof
locale: en
of_concept: theorem-on-the-normal-correlation
source_book: gtm095
source_chapter: "Chapter 2"
source_section: "§2. Optimal estimation, normal correlation theorem"
---

# Proof of Theorem 2 (Theorem on the Normal Correlation)

Let $(\xi, \eta)$ be a Gaussian vector with $\text{Var}\,\xi > 0$. Denote

$$m_1 = E\xi, \quad m_2 = E\eta, \quad \sigma_1^2 = \text{Var}\,\xi > 0, \quad \sigma_2^2 = \text{Var}\,\eta, \quad \rho = \frac{\text{Cov}(\xi, \eta)}{\sigma_1 \sigma_2}.$$

The joint density of $(\xi, \eta)$ is

$$f_{\xi, \eta}(x, y) = \frac{1}{2\pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \exp\left\{-\frac{1}{2(1 - \rho^2)}\left[\frac{(x - m_1)^2}{\sigma_1^2} - 2\rho \frac{(x - m_1)(y - m_2)}{\sigma_1 \sigma_2} + \frac{(y - m_2)^2}{\sigma_2^2}\right]\right\}.$$

The conditional density of $\eta$ given $\xi = x$ is

$$f_{\eta \mid \xi}(y \mid x) = \frac{f_{\xi, \eta}(x, y)}{f_\xi(x)},$$

where $f_\xi(x) = \frac{1}{\sqrt{2\pi}\sigma_1} \exp\{-\frac{(x - m_1)^2}{2\sigma_1^2}\}$ is the marginal density of $\xi$.

A direct computation yields that the conditional distribution is also normal:

$$\eta \mid \xi = x \sim \mathcal{N}\bigl(m(x), \sigma_2^2(1 - \rho^2)\bigr),$$

where

$$m(x) = m_2 + \frac{\sigma_2}{\sigma_1} \rho \cdot (x - m_1).$$

By the Corollary of Theorem 3, Sect. 7 (which characterizes conditional expectation via the conditional density),

$$E(\eta \mid \xi = x) = \int_{-\infty}^{\infty} y \, f_{\eta \mid \xi}(y \mid x) \, dy = m(x).$$

Therefore

$$E(\eta \mid \xi) = m_2 + \frac{\sigma_2}{\sigma_1} \rho \cdot (\xi - m_1) = E\eta + \frac{\text{Cov}(\xi, \eta)}{\text{Var}\,\xi}(\xi - E\xi).$$

For the error, compute the conditional variance:

$$\text{Var}(\eta \mid \xi = x) \equiv E\bigl[(\eta - E(\eta \mid \xi = x))^2 \mid \xi = x\bigr] = \int_{-\infty}^{\infty} (y - m(x))^2 f_{\eta \mid \xi}(y \mid x) \, dy = \sigma_2^2(1 - \rho^2).$$

Note that the conditional variance $\text{Var}(\eta \mid \xi = x)$ is independent of $x$. Hence, by Theorem 1 with $\varphi^*(\xi) = E(\eta \mid \xi)$,

$$\Delta \equiv E[\eta - E(\eta \mid \xi)]^2 = \sigma_2^2(1 - \rho^2) = \text{Var}\,\eta - \frac{\text{Cov}^2(\xi, \eta)}{\text{Var}\,\xi}.$$

Formulas (9) and (11) were obtained under the assumption that $\text{Var}\,\xi > 0$ and $\text{Var}\,\eta > 0$. If $\text{Var}\,\xi > 0$ and $\text{Var}\,\eta = 0$, they are still evidently valid, since then $\text{Cov}(\xi, \eta) = 0$ and $E(\eta \mid \xi) = E\eta$ almost surely. $\square$
