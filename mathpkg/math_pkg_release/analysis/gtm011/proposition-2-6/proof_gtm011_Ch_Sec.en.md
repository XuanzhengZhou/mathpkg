---
role: proof
locale: en
of_concept: proposition-2-6
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. By considering $G_1 = \left\{ \frac{1}{r} (z - a) : z \in G \right\}$ and the function $g(z) = f(a + rz)$ we see that, without loss of generality, it may be assumed that $a = 0$ and $r = 1$. That is we may assume that $\bar{B}(0; 1) \subset G$.

Fix $z, |z| < 1$; it must be shown that

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w - z} dw$$

$$= \frac{1}{2\pi} \int_{0}^{2\pi} \frac{f(e^{is})e^{is}}{e^{is} - z} ds;$$

that is, we want to show that

$$0 = \int_{0}^{2\pi} \frac{f(e^{is})e^{is}}{e^{is} - z} ds - 2\pi f(z)$$

$$= \int_{0}^{2\pi} \left[ \frac{f(e^{is})e^{is}}{e^{is} - z} - f(z) \right] ds$$

We will apply Leibniz's rule by letting

$$\varphi(s, t) = \frac{f(z + t(e^{is} - z))e^{is}}{e^{is} - z} - f(z),$$

for $0 \leq t \leq 1$ and $0 \

Power series representation of analytic functions compute:

$$g(0) = \int_{0}^{2\pi} \varphi(s, 0) \, ds$$

$$= \int_{0}^{2\pi} \left[ \frac{f(z)e^{i s}}{e^{i s}-z} - f(z) \right] \, ds$$

$$= f(z) \int_{0}^{2\pi} \frac{e^{i s}}{e^{i s}-z} \, ds - 2\pi f(z)$$

$$= 0,$$

since we showed that $\int_{0}^{2\pi} \frac{e^{i s}}{e^{i s}-z} \, ds = 2\pi$ prior to the statement of this proposition.

To show that $g$ is constant compute $g'$. By Leibniz's rule, $g'(t) = \int_{0}^{2\pi} \varphi_{2}(s, t) \, ds$ where

$$\varphi_{2}(s, t) = e^{i s}f'(z + t(e^{i s}-z)).$$

However, for $0 < t \leq 1$ we have that $\Phi(s) = -it^{-1}f(z + t(e^{i s}-z))$ is a primitive of $\varphi_{2}(s, t)$. So $g'(t) = \Phi(2\pi) - \Phi(0) = 0$ for $0 < t \leq 1$. Since $g'$ is continuous we have $g' = 0$ and $g$ must be a constant.

How is this result used to get the power series expansion? The answer is that we use a geometric series. Let $|z-a| < r$ and suppose that $w$ is on the circle $|w-a| = r$. Then

$$\frac{1}{w-z} = \frac{1}{w-a} \cdot \frac{1}{1 - \left[ \frac{z-a}{w-a} \right]} = \frac{1}{(w-a)} \sum_{n=0}^{\infty} \left( \frac{z-a}{w-a} \right)^{n}$$

since $|z-a| < r =

Proof. Let $\epsilon > 0$; then there is an integer $N$ such that $|F_n(w) - F(w)| < \epsilon/V(\gamma)$ for all $w$ on $\{\gamma\}$ and $n \geq N$. But this gives, by Proposition 1.17(b),

$$\left| \int_{\gamma} F - \int_{\gamma} F_n \right| = \left| \int_{\gamma} (F - F_n) \right|$$
$$\leq \int_{\gamma} |F(w) - F_n(w)| |dw|$$
$$\leq \epsilon$$

whenever $n \geq N$.
