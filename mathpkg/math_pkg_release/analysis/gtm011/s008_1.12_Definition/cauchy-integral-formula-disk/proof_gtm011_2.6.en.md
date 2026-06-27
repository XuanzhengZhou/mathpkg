---
role: proof
locale: en
of_concept: cauchy-integral-formula-disk
source_book: gtm011
source_chapter: "2"
source_section: "2.6"
---

By considering $G_1 = \left\{ \frac{1}{r} (z - a) : z \in G \right\}$ and the function $g(z) = f(a + rz)$, without loss of generality assume $a = 0$ and $r = 1$, i.e., $\bar{B}(0; 1) \subset G$.

Fix $z$ with $|z| < 1$. We must show

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w - z} dw = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{f(e^{is})e^{is}}{e^{is} - z} ds.$$

Equivalently,

$$0 = \int_{0}^{2\pi} \left[ \frac{f(e^{is})e^{is}}{e^{is} - z} - f(z) \right] ds.$$

Apply Leibniz's rule (Proposition 2.15) by defining

$$\varphi(s, t) = \frac{f(z + t(e^{is} - z))e^{is}}{e^{is} - z} - f(z),$$

for $0 \leq t \leq 1$ and $0 \leq s \leq 2\pi$. Set

$$g(t) = \int_{0}^{2\pi} \varphi(s, t) \, ds.$$

Compute $g(0)$:

$$g(0) = \int_{0}^{2\pi} \left[ \frac{f(z)e^{is}}{e^{is} - z} - f(z) \right] ds = f(z) \int_{0}^{2\pi} \frac{e^{is}}{e^{is} - z} ds - 2\pi f(z) = 0,$$

since $\int_{0}^{2\pi} \frac{e^{is}}{e^{is} - z} ds = 2\pi$ (shown prior to the proposition).

To show $g$ is constant, compute $g'(t) = \int_{0}^{2\pi} \varphi_2(s, t) ds$ where $\varphi_2(s, t) = e^{is} f'(z + t(e^{is} - z))$. For $0 < t \leq 1$, the function $\Phi(s) = -it^{-1} f(z + t(e^{is} - z))$ is a primitive of $\varphi_2(s, t)$. Hence $g'(t) = \Phi(2\pi) - \Phi(0) = 0$ for $0 < t \leq 1$. By continuity of $g'$, $g' = 0$ everywhere, so $g$ is constant.

Since $g(1) = 0$ (as $g$ is constant and $g(0) = 0$), we obtain

$$\int_{0}^{2\pi} \left[ \frac{f(e^{is})e^{is}}{e^{is} - z} - f(z) \right] ds = 0,$$

which is exactly the desired equality.
