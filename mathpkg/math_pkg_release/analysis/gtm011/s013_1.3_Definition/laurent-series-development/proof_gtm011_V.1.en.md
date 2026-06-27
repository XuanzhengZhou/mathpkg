---
role: proof
locale: en
of_concept: laurent-series-development
source_book: gtm011
source_chapter: "V"
source_section: "1"
---

If $R_1 < r_1 < r_2 < R_2$ and $\gamma_1$, $\gamma_2$ are the circles $|z-a| = r_1$, $|z-a| = r_2$ respectively, then $\gamma_1 \sim \gamma_2$ in $\operatorname{ann}(a; R_1, R_2)$. By Cauchy's Theorem we have that for any function $g$ analytic in $\operatorname{ann}(a; R_1, R_2)$, $\int_{\gamma_1} g = \int_{\gamma_2} g$. In particular the integral appearing in the formula for $a_n$ is independent of $r$ so that for each integer $n$, $a_n$ is a constant.

Moreover, define $f_2: B(a; R_2) \to \mathbb{C}$ by the formula
$$f_2(z) = \frac{1}{2\pi i} \int_{|w-a|=r_2} \frac{f(w)}{w-z} \, dw,$$
where $|z-a| < r_2$, $R_1 < r_2 < R_2$. By Lemma IV.5.1, $f_2$ is analytic in $B(a; r_2)$. Similarly, if $G = \{z : |z-a| > R_1\}$, define $f_1: G \to \mathbb{C}$ for $|z-a| > r_1$ (where $R_1 < r_1 < |z-a|$) by
$$f_1(z) = -\frac{1}{2\pi i} \int_{|w-a|=r_1} \frac{f(w)}{w-z} \, dw.$$

Consider the cycle $\gamma = \gamma_2 - \lambda - \gamma_1 + \lambda$ (with suitable connecting segment $\lambda$), which is homotopic to zero in the annulus. Since $n(\gamma_2; z) = 1$ and $n(\gamma_1; z) = 0$ for $z$ between the two circles, Cauchy's Integral Formula gives
$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} \, dw
= \frac{1}{2\pi i} \int_{\gamma_2} \frac{f(w)}{w-z} \, dw - \frac{1}{2\pi i} \int_{\gamma_1} \frac{f(w)}{w-z} \, dw
= f_2(z) + f_1(z).$$

Now expand $f_1$ and $f_2$ in power series ($f_1$ having negative powers of $(z-a)$); adding them together will give the Laurent series development of $f(z)$. Since $f_2$ is analytic in the disk $B(a; R_2)$ it has a power series expansion about $a$. Using Lemma IV.5.1 to calculate $f_2^{(n)}(a)$,
$$f_2(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$$
where the coefficients $a_n$ are given by the integral formula.

Now define $g(z)$ for $0 < |z| < 1/R_1$ by $g(z) = f_1(a + 1/z)$, so $z = 0$ is an isolated singularity. We claim that $z = 0$ is a removable singularity for $g$. In fact, if $r > R_1$ then let $\rho(z) = d(z, C)$ where $C$ is the circle $\{w : |w-a| = r\}$; also put $M = \max\{|f(w)| : w \in C\}$. Then for $|z-a| > r$,
$$|f_1(z)| \leq \frac{Mr}{\rho(z)}.$$
But $\lim_{z \to \infty} \rho(z) = \infty$, so $\lim_{z \to \infty} f_1(z) = 0$. Consequently $\lim_{z \to 0} g(z) = 0$, which proves that $z = 0$ is a removable singularity for $g$ with $g(0) = 0$.

Hence $g$ is analytic at $0$ and has a power series expansion $g(z) = \sum_{n=1}^{\infty} b_n z^n$. Substituting back $z = 1/(\zeta-a)$ yields
$$f_1(\zeta) = \sum_{n=1}^{\infty} b_n (\zeta-a)^{-n} = \sum_{n=-\infty}^{-1} a_n (\zeta-a)^n,$$
where $a_{-n} = b_n$ for $n \geq 1$.

Adding the two series, we obtain
$$f(z) = f_1(z) + f_2(z) = \sum_{n=-\infty}^{-1} a_n (z-a)^n + \sum_{n=0}^{\infty} a_n (z-a)^n = \sum_{n=-\infty}^{\infty} a_n (z-a)^n.$$

The absolute and uniform convergence on compact subsets follows from standard estimates on the power series for $f_1$ and $f_2$. Uniqueness follows because if $f(z) = \sum_{n} a_n (z-a)^n = \sum_{n} b_n (z-a)^n$ on the annulus, then multiplying by $(z-a)^{-k-1}$ and integrating over a circle $\gamma$ yields $a_k = b_k$ for all $k \in \mathbb{Z}$.
