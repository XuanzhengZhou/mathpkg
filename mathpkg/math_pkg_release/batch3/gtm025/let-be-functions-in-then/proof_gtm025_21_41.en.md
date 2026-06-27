---
role: proof
locale: en
of_concept: "let-be-functions-in-then"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.41"
---

For all $y \in R$ we have

$$\widehat{f * g}(y) = (2\pi)^{-\frac{1}{2}} \int_R f * g(x) \exp(-iyx) dx$$

$$= (2\pi)^{-\frac{1}{2}} \int_R (2\pi)^{-\frac{1}{2}} \int_R f(x-t) g(t) dt \exp(-iyx) dx$$

$$= \frac{1}{2\pi} \int_R g(t) \int_R f(x-t) \exp(-iyx) dx dt$$

$$= \frac{1}{2\pi} \int_R g(t) \int_R f(u) \exp(-i(t+u)y) du dt$$

$$= \frac{1}{2\pi} \int_R g(t) \exp(-iyt) \int_R f(u) \exp(-iyu) du dt$$

$$= f(y) \cdot \hat{g}(y);$$

we have made free use of FUBINI's theorem and of (12.44).

We next take up the problem of reconstructing a function from its Fourier transform. The analogous problem for Fourier series was treated in (18.29) and (18.47) supra. The following lemma points up the close connection between this problem and that of approximating a function by convolving it with an approximate

Proof. Let $x \in R$. Since the function $(s, t) \rightarrow f(s) k(t)$ is in $\mathfrak{L}_1(R \times R)$, Fubini's theorem can be applied in the following computation:

$(2\pi)^{-\frac{1}{2}} \int \limits_R f(y) k(y) \exp(ixy) dy$

$= \frac{1}{2\pi} \int \limits_R f(t) \exp(-iyt) dt k(y) \exp(ixy) dy$

$= \frac{1}{2\pi} \int \limits_R f(t) \int \limits_R k(y) \exp(-i(t-x)y) dy dt$

$= (2\pi)^{-\frac{1}{2}} \int \limits_R f(t) \hat{k}(t-x) dt$

$= (2\pi)^{-\frac{1}{2}} \int \limits_R f(t) u(x-t) dt$

$= u * f(x) = f * u(x).$

(21.43) Pointwise summability Theorem. Let $(k_n)_{n=1}^{\infty}$ be a sequence of functions in $\mathfrak{L}_1(R)$ and write $u_n = \hat{k}_n$. Suppose that for each $n \in N$ we have $u_n \in \mathfrak{L}_1(R)$, $(2\pi)^{-\frac{1}{2}} \int \limits_R u_n(t) dt = 1$, and $u_n(-t) = u_n(t)$ for all $t \in R$.

Furthermore, suppose that there is a function $u$ such that:

(i) $u \in \mathfrak{L}_1^+([0, \infty])$;

(ii) $u$ is nonincreasing and absolutely continuous on $[0, \infty]$;

(iii) $|u_n(t)| \leq nu(nt)$ for all $t \geq 0$ and all $n \in N$.

Then if $f$ is a function in $\mathfrak{L}_1(R)$ and $x$ is a Lebesgue point for $f$,

As in (18.29), we write $\varphi(t) = f(x + t) + f(x - t) - 2f(x)$. Since $|u_n(t)| \leq nu(nt)$ for all $t \geq 0$ and all $n \in N$, (1) yields

$$|f * u_n(x) - f(x)| \leq (2\pi)^{-\frac{1}{2}} \int_0^\infty |\varphi(t)| nu(nt) dt.$$

Thus we need only to show that the right side of (2) has limit zero as $n \to \infty$. To this end, let $\varepsilon > 0$ be given and write

$$c = 6\varepsilon + 6u(0) + 3 \int_0^\infty u(y) dy + 6 \|f\|_1 + 6|f(x)| + 1.$$

For $h > 0$, set

$$\Phi(h) = \int_0^h |\varphi(t)| dt.$$

Since $x$ is a Lebesgue point (18.6) for $f$, there exists a number $\alpha \in ]0, 1]$ such that

$$\frac{1}{h} \Phi(h) < \frac{\varepsilon}{c} \quad \text{for} \quad h \in ]0, \alpha].$$

Since $u$ is nonincreasing and in $\mathfrak{L}_1^+([0, \infty[$), it follows at once from dominated convergence (12.24) that there exists an integer $n_0$ such that if $n > n_0$, then

$$\int_ {n \alpha}^\infty u(y) dy < \frac{\varepsilon}{c},$$

and also

$$nu(n\alpha) = \frac{2}{\alpha} \frac{n\alpha}{2} u(n\alpha) \leq \frac{2}{\alpha} \int_ {\frac{n\alpha}{2}}^\infty u(y) dy$$

$$\leq \frac{2}{\alpha} \int_ {\frac{n\alpha}{2}}^\infty u(y) dy < \frac{\varepsilon}{c}.$$

Now let

We apply (3) to $I_1$ and find that

$$I_1 \leq \int_0^{1/n} |\varphi(t)| n u(0) dt = n \Phi\left(\frac{1}{n}\right) u(0) < u(0) \frac{\varepsilon}{c} < \frac{\varepsilon}{3}. \tag{7}$$

To majorize $I_2$, we integrate by parts (18.19), use (3) and (5), and integrate by parts again. This yields the following estimates:

$$I_2 = \int_1/n^\alpha |\varphi(t)| n u(n\alpha) - \Phi\left(\frac{1}{n}\right) n u(1) - \int_1/n^\alpha \Phi(t) n^2 u'(nt) dt$$

$$\leq \frac{1}{\alpha} \Phi(\alpha) n u(n\alpha) + n \Phi\left(\frac{1}{n}\right) u(0) - \int_1/n^\alpha \Phi(t) n^2 u'(nt) dt$$

$$< \frac{\varepsilon^2}{c^2} + \frac{\varepsilon}{c} u(0) - \int_1/n^\alpha t \frac{\varepsilon}{c} n^2 u'(nt) dt^1$$

$$= \frac{\varepsilon^2}{c^2} + \frac{\varepsilon}{c} u(0) - \frac{\varepsilon}{c} \left[ n\alpha u(n\alpha) - u(1) \right] + \frac{\varepsilon n}{c} \int_1/n^\alpha u(nt) dt$$

$$< \frac{\varepsilon^2}{c} + \frac{\varepsilon}{c} u(0) + \frac{\varepsilon^2}{c} + \frac{\varepsilon}{c} u(0) + \frac{\varepsilon}{c} \int_1^n\alpha u(y) dy$$

$$< \frac{\varepsilon}{c} \left(2\varepsilon + 2u(0) + \int_0^\infty u(y) dy \right) < \frac{\varepsilon}{3}.

if $n > n_1$. Since every point of continuity of $f$ is a Lebesgue point of $f$, our last assertion also holds. $\square$

(21.44) Notes. The reader may well have noticed the similarity between the proofs of (21.43) and (18.29) [(18.47) is different]. It would be no trouble to generalize (18.29) to a class of kernels $(u_n)_{n=1}^{\infty}$ of period $2\pi$ satisfying hypotheses like those imposed on $(u_n)_{n=1}^{\infty}$ in (21.43). The only essential difference in the arguments of (21.43) and (18.29) is that we need FUBINI's theorem to interchange the order of integration in the former, while only sums and integrals are involved in the latter. [Of course equalities $\sum \int = \int \sum$ are special cases of FUBINI's theorem.]

There are many sequences $(k_n)_{n=1}^{\infty}$ that satisfy the hypotheses of (21.43). We will now give three classical examples of such sequences. The reader should check in each case that the hypotheses of (21.43) hold.

(21.45) Examples. (a) Let $k_n(y) = \exp \left( -\frac{|y|}{n} \right)$. For each $\alpha > 0$, we have

$$\int_R \exp \left( -\alpha |y| \right) \exp \left( -i t y \right) dy = \int_0^\infty \exp \left( (\alpha - i t) y \right) dy + \int_0^\infty \exp \left( (-\alpha - i t) y \right) dy$$

$$= \lim_{A \to \infty} \left[ \frac{1}{\alpha - i t} - \frac{1}{\alpha - i t} \exp \left( (-\alpha - i t) A \right) + \frac{1}{\alpha + i t} - \frac{1}{\alpha + i t} \exp \left( (-\alpha + i t) A

Hence

$$u_n(t) = \hat{k}_n(t) = (2\pi)^{-\frac{1}{2}} n \left[ \frac{\sin\left(\frac{1}{2} n t\right)}{\frac{1}{2} n t} \right]^2.$$

In this case, we may take $u(t) = \frac{4}{1+t^2}$. This sequence $(u_n)_{n=1}^{\infty}$ is known as FEJER's kernel. See also (21.55) infra.

(c) Let $k_n(y) = \exp\left(-\frac{y^2}{2n^2}\right)$. It is shown in (21.60) infra that

$$u_n(t) = \hat{k}_n(t) = n \exp\left(-\frac{n^2 t^2}{2}\right).$$

Here we take $u = u_1$. This sequence is called GAuss's kernel.

(21.46) Notes. (a) Theorem (21.43) and Examples (21.45) show why the factor $(2\pi)^{-\frac{1}{2}}$ is used in the integral defining $f$. With this factor, we use the same integral for integrating Fourier transforms that we use for integrating the original functions. This is convenient, and it becomes useful in some later developments (21.53).

(b) All of the kernels listed in (21.45) can plainly be taken to depend upon an arbitrary positive real number $\alpha$ instead of a positive integer $n$. The equality (21.43.iv) holds as $\alpha \to \infty$ for all three kernels.
