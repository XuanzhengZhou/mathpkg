---
role: proof
locale: en
of_concept: lemma-af8dbb85d3
source_book: gtm077
source_chapter: "VIII"
source_section: "56"
---

# Proof of Lemma: Limit Behavior of the Theta Function

We prove: If the complex variables $t_1, \ldots, t_n$ simultaneously tend to zero in such a way that the real parts of $1/t_p$ tend to plus infinity, then

$$\lim_{t \to 0} \sqrt{t_1 \cdots t_n} \; \theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a}) \sqrt{d}},$$

independently of $z$.

**Proof.** From Theorem 159, the theta function admits the dual representation

$$\theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a})|\sqrt{d}| \sqrt{t_1 \cdots t_n}} \sum_{\lambda \in 1/\mathfrak{a}\mathfrak{b}} \exp\left\{ -\pi \sum_{p=1}^{n} \frac{\lambda^{(p)^2}}{t_p} - 2\pi i \sum_{p=1}^{n} \lambda^{(p)} z_p \right\}. \tag{179}$$

Multiplying both sides by $\sqrt{t_1 \cdots t_n}$, we obtain

$$\sqrt{t_1 \cdots t_n} \; \theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a})|\sqrt{d}|} \sum_{\lambda \in 1/\mathfrak{a}\mathfrak{b}} \exp\left\{ -\pi \sum_{p=1}^{n} \frac{\lambda^{(p)^2}}{t_p} - 2\pi i \sum_{p=1}^{n} \lambda^{(p)} z_p \right\}.$$

The term with $\lambda = 0$ (corresponding to $m_1 = \cdots = m_n = 0$) contributes exactly $1/(N(\mathfrak{a})|\sqrt{d}|)$. All other terms involve exponential factors whose magnitudes we now estimate.

Let $r$ denote the smallest of the $n$ numbers $\Re(1/t_p)$. Then for any $\lambda \in 1/\mathfrak{a}\mathfrak{b}$, $\lambda \neq 0$, we have

$$\left| \exp\left\{ -\pi \sum_{p=1}^{n} \frac{1}{t_p} \lambda^{(p)^2} \right\} \right| = \exp\left\{ -\pi \sum_{p=1}^{n} \Re\left(\frac{1}{t_p}\right) \lambda^{(p)^2} \right\} \leq \exp\left\{ -\pi r \sum_{p=1}^{n} \lambda^{(p)^2} \right\}.$$

By the estimate (172) from the theory of lattices in number fields, there exists a positive constant $c$, independent of the $t_p$, such that for all $\lambda = \sum_{k=1}^{n} \beta_k m_k \in 1/\mathfrak{a}\mathfrak{b}$ with integer coordinates $m_1, \ldots, m_n$,

$$\sum_{p=1}^{n} \lambda^{(p)^2} \geq c(m_1^2 + \cdots + m_n^2).$$

Hence each nonzero term is bounded by $\exp\{-\pi r c (m_1^2 + \cdots + m_n^2)\}$.

The sum over all $\lambda \neq 0$ in the right-hand side of (179) is thus bounded in absolute value by

$$\sum_{(m) \neq (0)} e^{-\pi r c (m_1^2 + \cdots + m_n^2)} = \left( \sum_{m=-\infty}^{\infty} e^{-\pi r c m^2} \right)^n - 1.$$

Since $e^{-\pi r c m^2} < e^{-\pi r c |m|}$ for $|m| \geq 1$ (as $m^2 \geq |m|$ for integers), we obtain

$$\sum_{m=-\infty}^{\infty} e^{-\pi r c m^2} < 1 + 2 \sum_{m=1}^{\infty} e^{-\pi r c m} = 1 + \frac{2e^{-\pi r c}}{1 - e^{-\pi r c}}.$$

Therefore

$$\left( \sum_{m=-\infty}^{\infty} e^{-\pi r c m^2} \right)^n - 1 < \left( 1 + \frac{2e^{-\pi r c}}{1 - e^{-\pi r c}} \right)^n - 1.$$

As $r \to +\infty$ (which is precisely the hypothesis that the real parts of $1/t_p$ tend to plus infinity), the quantity $e^{-\pi r c} \to 0$, and thus the entire bound tends to $0$.

Consequently, all terms with $\lambda \neq 0$ vanish in the limit, and we obtain

$$\lim_{t \to 0} \sqrt{t_1 \cdots t_n} \; \theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a}) |\sqrt{d}|} = \frac{1}{N(\mathfrak{a}) \sqrt{d}},$$

where we take the positive square root of the discriminant $d$ (which is positive since $k$ is totally real). The limit is independent of the parameters $z = (z_1, \ldots, z_n)$, because the exponential factor involving $z$ is bounded by $1$ in absolute value and does not affect the vanishing of the $\lambda \neq 0$ terms. $\square$
