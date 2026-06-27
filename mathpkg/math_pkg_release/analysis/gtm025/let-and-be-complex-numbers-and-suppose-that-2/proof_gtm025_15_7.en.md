---
role: proof
locale: en
of_concept: "let-and-be-complex-numbers-and-suppose-that-2"
source_book: gtm025
source_chapter: "Lp Spaces"
source_section: "15.7"
---

If $z = 0$ or $w = 0$, (i) is obvious. Otherwise, we may suppose that $0 < |z| \leq |w|$. The desired inequality is thus equivalent to the inequality

$$\left| 1 + \frac{z}{w} \right|^{p'} + \left| -1 + \frac{z}{w} \right|^{p'} \leq 2 \left( \left| \frac{z}{w} \right|^p + 1 \right)^{\frac{1}{p-1}}.$$

(1)

Write (1) in the form

$$|1 + r \exp(i\theta)|^{p'} + |-1 + r \exp(i\theta)|^{p'} \leq 2(r^p + 1)^{\frac{1}{p-1}},$$

(2)

where $\frac{z}{w} = r \exp(i\theta)$, $0 < r \leq 1$, and $0 \leq \theta < 2\pi$. For $\theta = 0$, the inequality (2) is just (15.6.i). Just as in the proof of (15.4.2), one shows that the expression on the left in (2) attains its maximum on $\left[ 0, \frac{\pi}{2} \right]$ at $\theta = 0$. Thus (2) holds for all $\theta$.

(15.8) Clarkson's inequality for $1 < p < 2$. For functions $f$ and $g$ in $\mathfrak{L}_p$, the inequality

(i) $$\left\| \frac{f + g}{2} \right\|_p^{p'} + \left\| \frac{f - g}{2} \right\|_p^{p'} \leq \left[ \frac{1}{2} \|f\|_

Proof. The definition (14.1) of $\|L\|$ shows that there is a sequence $(\varphi_n')_{n=1}^{\infty}$ in $\mathfrak{L}_p$ such that $\|\varphi_n'\|_p = 1$, $|L(\varphi_n')| > \frac{1}{2} \|L\|$, and $\lim_{n \to \infty} |L(\varphi_n')| = \|L\|$. Let $\varphi_n = \text{sgn} \left[ \overline{L(\varphi_n')} \right] \varphi_n'$. Then we obviously have:

$$L(\varphi_n) = |L(\varphi_n')| > \frac{1}{2} \|L\| > 0;$$

$$\|\varphi_n\|_p = 1;$$

$$\lim_{n \to \infty} L(\varphi_n) = \|L\|.$$

We will show that $(\varphi_n)$ is a Cauchy sequence in $\mathfrak{L}_p$. In the contrary case, there are a positive number $\alpha$ and subsequences $(\varphi_n_k)_{k=1}^{\infty}$ and $(\varphi_m_k)_{k=1}^{\infty}$ such that $\|\varphi_n_k - \varphi_m_k\|_p > \alpha$ for $k = 1, 2, \ldots$. For $p \geq 2$, we use CLARKSON's inequality (15.5) to write

$$\left\| \frac{\varphi_m_k + \varphi_n_k}{2} \right\|_p^p + \left\| \frac{\varphi_m_k - \varphi_n_k}{2} \right\|_p^p \leq \frac{1}{2} \|\varphi_n_k\|_p^p + \frac{1}{2} \|\varphi_m_k\|_p^p = 1.$$

For $1 < p < 2$, we use CLARKSON's inequality (15.8) to write

$$\left\| \frac{\varphi_m_k + \varphi_n_k}{2} \right\|_p^{p'} + \left\| \frac{\varphi_m_k - \varphi_n_k}{2}

By (3) we have $\lim_{k \to \infty} L(\varphi_m_k) = \lim_{k \to \infty} L(\varphi_n_k) = \|L\|$. Thus (10) implies that

$$\lim_{k \to \infty} L(g_k) \geq \frac{1}{1 - \beta} \|L\|.$$

Since $\|g_k\|_p = 1$, this is an evident contradiction. Therefore $(\varphi_n)$ is a Cauchy sequence in $\mathfrak{L}_p$ and so has a limit $\varphi_0$ in $\mathfrak{L}_p$ (13.11). It is clear from (3) that $\lim_{n \to \infty} L(\varphi_n) = L(\varphi_0) = \|L\|.$
