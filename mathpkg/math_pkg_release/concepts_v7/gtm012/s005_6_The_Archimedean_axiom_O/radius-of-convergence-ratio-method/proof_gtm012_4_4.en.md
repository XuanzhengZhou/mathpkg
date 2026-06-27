---
role: proof
locale: en
of_concept: radius-of-convergence-ratio-method
source_book: gtm012
source_chapter: "4"
source_section: "4. Series"
---

# Proof of Radius of convergence via ratio method (Theorem 4.9)

**Theorem 4.9.** Suppose $a_n \neq 0$ for $n \geq N$, and suppose $\lim_{n \to \infty} |a_{n+1}/a_n|$ exists. Then the radius of convergence $R$ of the power series $\sum_{n=0}^{\infty} a_n (z - z_0)^n$ is given by

$$R = \left( \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| \right)^{-1} \quad \text{if } \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| > 0,$$

$$R = \infty \quad \text{if } \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = 0.$$

**Proof.** Apply the ratio test (Proposition 4.4) to the series $\sum_{n=0}^{\infty} a_n (z - z_0)^n$. For $z \neq z_0$,

$$\left| \frac{a_{n+1}(z - z_0)^{n+1}}{a_n(z - z_0)^n} \right| = \left| \frac{a_{n+1}}{a_n} \right| \cdot |z - z_0|.$$

Let $L = \lim_{n \to \infty} |a_{n+1}/a_n|$.

- If $L > 0$, then $\lim_{n \to \infty} |a_{n+1}(z - z_0)^{n+1} / a_n(z - z_0)^n| = L \cdot |z - z_0|$. By the ratio test, the series converges absolutely when $L \cdot |z - z_0| < 1$, i.e., $|z - z_0| < 1/L$, and diverges when $L \cdot |z - z_0| > 1$, i.e., $|z - z_0| > 1/L$. Therefore $R = 1/L = (\lim |a_{n+1}/a_n|)^{-1}$.

- If $L = 0$, then $\lim |a_{n+1}(z - z_0)^{n+1} / a_n(z - z_0)^n| = 0 \cdot |z - z_0| = 0 < 1$ for every $z \in \mathbb{C}$. By the ratio test, the series converges absolutely for all $z$, so $R = \infty$.

(Note: the case $\lim |a_{n+1}/a_n| = \infty$ would give $R = 0$, but the theorem statement only considers the finite limit case.) $\square$

**Remark.** This theorem is a special case of the Cauchy–Hadamard formula $R = (\limsup |a_n|^{1/n})^{-1}$. The ratio method is often easier to compute in practice, but the root test (Corollary 4.5) is more general since the limit $\lim |a_{n+1}/a_n|$ need not exist while $\limsup |a_n|^{1/n}$ always does (provided the sequence is bounded).
