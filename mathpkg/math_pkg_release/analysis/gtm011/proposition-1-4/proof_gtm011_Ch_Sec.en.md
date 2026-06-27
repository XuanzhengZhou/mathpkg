---
role: proof
locale: en
of_concept: proposition-1-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. If $R_1 < r_1 < r_2 < R_2$ and $\gamma_1, \gamma_2$ are the circles $|z-a| = r_1, |z-a| = r_2$ respectively, then $\gamma_1 \sim \gamma_2$ in ann $(a; R_1, R_2)$. By Cauchy’s Theorem we have that for any function $g$ analytic in ann $(a; R_1, R_2)$, $\int_{\gamma_1} g = \int_{\gamma_2} g$. In particular the integral appearing in (1.12) is independent of $r$ so that for each integer $n$, $a_n$ is a constant. Moreover, $f_2: B(a; R_2) \to \mathbb{C}$ given by the formula

$$f_2(z) = \frac{1}{2\pi i} \int_{|w-a|=r_2} \frac{f(w)}{w-z} \, dw,$$

where $|z-a| < r_2$, $R_1 < r_2 < R_2$, is a well defined function. Also, by Lemma IV.5.1 $f_2$ is analytic in $B(a; r_2)$. Similarly, if $G = \{z: |z-a| > R_1\}$ then $f_1: G

$\gamma = \gamma_2 - \lambda - \gamma_1 + \lambda$ is homotopic to zero. Also $n(\gamma_2; z) = 1$ and $n(\gamma_1, z) = 0$ gives, by Cauchy's Integral Formula, that

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} dw$$

$$= \frac{1}{2\pi i} \int_{\gamma_2} \frac{f(w)}{w-z} dw - \frac{1}{2\pi i} \int_{\gamma_1} \frac{f(w)}{w-z} dw$$

$$= f_2(z) + f_1(z).$$

The plan now is to expand $f_1$ and $f_2$ in power series ($f_1$ having negative powers of $(z-a)$); then adding them together will give the Laurent series development of $f(z)$. Since $f_2$ is analytic in the disk $B(a; R_2)$ it has a power series expansion about $a$. Using Lemma IV. 5.1 to calculate $f_2^{(n)}(a)$,

$$f_2(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$$

where the coefficients $a_n$ are given by (1.12).

Now define $g(z)$ for

$$0 < |z| < \frac{1}{R_1} \text{ by } g(z) = f_1\left(a + \frac{1}{z}\right);$$

so $z = 0$ is an isolated singularity. We claim that $z = 0$ is a removable singularity. In fact, if $r > R_1$ then let $\rho(z) = d(z, C)$ where $C$ is the circle $\{w: |w-a| = r\}$; also put $M = \max \{|f(w)|: w \in C\}$. Then for $|z-a| > r$

$$|f_1(z)| \leq \frac{Mr}{\rho(z)}.$$

But $\lim_{z \to \infty} \rho(z) = \infty$
