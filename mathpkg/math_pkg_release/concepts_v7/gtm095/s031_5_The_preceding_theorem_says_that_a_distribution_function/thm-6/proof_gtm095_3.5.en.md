---
role: proof
locale: en
of_concept: thm-6
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 6 (Decomposition formulas for moments and semi-invariants)

**Theorem 6.** Let $\xi = (\xi_1, \ldots, \xi_k)^*$ be a random vector with $E|\xi_i|^n < \infty$ for $i = 1, \ldots, k$ and some $n \geq 1$. Then for all $\nu = (\nu_1, \ldots, \nu_k)$ with $|\nu| = \nu_1 + \cdots + \nu_k \leq n$, the following decomposition formulas hold:

$$m_{\xi}^{(\nu)} = \sum_{\substack{q \geq 1 \\ \lambda^{(1)} + \cdots + \lambda^{(q)} = \nu}} \frac{1}{q!} \frac{\nu!}{\lambda^{(1)}! \cdots \lambda^{(q)}!} \prod_{j=1}^{q} s_{\xi}^{(\lambda^{(j)})}, \tag{40}$$

$$s_{\xi}^{(\nu)} = \sum_{\substack{q \geq 1 \\ \lambda^{(1)} + \cdots + \lambda^{(q)} = \nu}} \frac{(-1)^{q-1}}{q} \frac{\nu!}{\lambda^{(1)}! \cdots \lambda^{(q)}!} \prod_{j=1}^{q} m_{\xi}^{(\lambda^{(j)})}, \tag{41}$$

where $\lambda^{(j)} = (\lambda_1^{(j)}, \ldots, \lambda_k^{(j)})$ are vectors with nonnegative integer components, $|\lambda^{(j)}| \geq 1$.

## Proof

From the Taylor expansion of the characteristic function (see Subsection 8) and the existence of moments up to order $n$, we have:

$$\varphi_{\xi}(t) = \sum_{|\nu| \leq n} \frac{i^{|\nu|}}{\nu!} m_{\xi}^{(\nu)} t^{\nu} + o(|t|^n), \tag{37}$$

$$\log \varphi_{\xi}(t) = \sum_{|\nu| \leq n} \frac{i^{|\nu|}}{\nu!} s_{\xi}^{(\nu)} t^{\nu} + o(|t|^n). \tag{38}$$

Since $\varphi_{\xi}(t) = \exp(\log \varphi_{\xi}(t))$, we write:

$$\varphi_{\xi}(t) = \exp\left( \sum_{1 \leq |\lambda| \leq n} \frac{i^{|\lambda|}}{\lambda!} s_{\xi}^{(\lambda)} t^{\lambda} + o(|t|^n) \right)$$
$$= \sum_{q=0}^{n} \frac{1}{q!} \left( \sum_{1 \leq |\lambda| \leq n} \frac{i^{|\lambda|}}{\lambda!} s_{\xi}^{(\lambda)} t^{\lambda} \right)^q + o(|t|^n). \tag{42}$$

Expanding the $q$-th power and collecting terms in $t^{\nu}$, we have for the coefficient of $t^{\nu}$ on the right-hand side of (42):

$$\sum_{q \geq 1} \frac{1}{q!} \sum_{\lambda^{(1)} + \cdots + \lambda^{(q)} = \nu} \frac{i^{|\lambda^{(1)}| + \cdots + |\lambda^{(q)}|}}{\lambda^{(1)}! \cdots \lambda^{(q)}!} \prod_{j=1}^{q} s_{\xi}^{(\lambda^{(j)})}$$
$$= i^{|\nu|} \sum_{\substack{q \geq 1 \\ \lambda^{(1)} + \cdots + \lambda^{(q)} = \nu}} \frac{1}{q!} \frac{1}{\lambda^{(1)}! \cdots \lambda^{(q)}!} \prod_{j=1}^{q} s_{\xi}^{(\lambda^{(j)})}.$$

Comparing this with the coefficient $\frac{i^{|\nu|}}{\nu!} m_{\xi}^{(\nu)}$ from (37) yields (40).

For (41), we write

$$\log \varphi_{\xi}(t) = \log\left[ 1 + \sum_{1 \leq |\lambda| \leq n} \frac{i^{|\lambda|}}{\lambda!} m_{\xi}^{(\lambda)} t^{\lambda} + o(|t|^n) \right].$$

Using the expansion $\log(1 + z) = \sum_{q=1}^{n} \frac{(-1)^{q-1}}{q} z^q + o(z^n)$ for small $z$, and comparing coefficients with (38), we obtain (41).
