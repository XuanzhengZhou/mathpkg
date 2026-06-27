---
role: proof
locale: en
of_concept: "let-then-and"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.52"
---

Define $T$ on $\mathfrak{L}_1 \cap \mathfrak{L}_2$ by

$$Tf = f.$$

Since $\mathfrak{C}_{00} \subset \mathfrak{L}_1 \cap \mathfrak{L}_2$, it follows from (13.21) that $\mathfrak{L}_1 \cap \mathfrak{L}_2$ is dense in $\mathfrak{L}_2$. For $f \in \mathfrak{L}_2$, let $(f_n)$ be any sequence in $\mathfrak{L}_1 \cap \mathfrak{L}_2$ such that $\| f - f_n \|_2 \to 0$. Then $(f_n)$ is a Cauchy sequence in $\mathfrak{L}_2$, and so (21.52) implies that

$$\| Tf_n - Tf_m \|_2 = \| f_n - f_m \|_2 = \| f_n - f_m \|_2 \to 0 \text{ as } m, n \to \infty.$$

Thus $(Tf_n)$ is a Cauchy sequence in $\mathfrak{L}_2$ and, since $\mathfrak{L}_2$ is complete (13.11), there is a unique function $Tf \in \

Then we have

$$\langle f, T^* \varphi \rangle = \langle Tf, \varphi \rangle = (2\pi)^{-\frac{1}{2}} \int_R f(y) \overline{\varphi(y)} dy$$

$$= \frac{1}{2\pi} \int_R f(x) \exp(-iyx) dx \overline{\varphi(y)} dy$$

$$= \frac{1}{2\pi} \int_R f(x) \int_R \varphi(y) \exp(ixy) dy dx$$

$$= (2\pi)^{-\frac{1}{2}} \int_R f(x) \overline{g(x)} dx = \langle f, g \rangle,$$

(2)

the change of order being justified by Fubini's theorem [the integrand is in $\mathfrak{L}_1(R^2)$ because $f, \varphi \in \mathfrak{L}_1(R)$]. Since $\mathfrak{L}_1 \cap \mathfrak{L}_2$ is dense in $\mathfrak{L}_2$ and the mapping $f \rightarrow \langle f, h \rangle$ is continuous on $\mathfrak{L}_2$ for all $h \in \mathfrak{L}_2$, (1) and (2) imply that

$$[T^* \varphi](x) = (2\pi)^{-\frac{1}{2}} \int_R \varphi(y) \exp(ixy) dy = \hat{\varphi}(-x)$$

(3)

for all $\varphi \in \mathfrak{L}_1 \cap \mathfrak{L}_2$ and all $x \in R$. Let $\varphi, \psi$ be in $\mathfrak{L}_1 \cap \mathfrak{L}_2$ and write $f = T^* \varphi$, $g = T^* \psi$. Then (21.41) and (3) imply that

$$\widehat{\varphi * \psi}(x) = \hat{\varphi}(x) \hat{\psi}(x) = f(-x) g(-x)$$

(4)

for all $x \in R$. Since $f, g$ are in $\

for all $n \in N$, and (21.37) shows that

$$\lim_{n \to \infty} \| \varphi - \varphi * \psi_n \|_2 = 0;$$

hence, $rng T$ being closed in $\mathfrak{L}_2$, we have $\varphi \in rng T$. Thus $\mathfrak{L}_1 \cap \mathfrak{L}_2 \subset rng T$, and so $rng T$ is dense in $\mathfrak{L}_2$.

(21.54) Remarks. (a) The proof of (21.53) shows that if $\varphi, \psi \in \mathfrak{L}_1 \cap \mathfrak{L}_2$, then there exists a function $h \in \mathfrak{L}_1 \cap \mathfrak{C}_0$ such that $\hat{h} = \varphi * \psi$. In fact, $h = fg$ where $f = T^* \varphi$ and $g = T^* \psi$.

(b) Theorem (21.53) is the analogue for the line of the RIESZ-FISCHER theorem (16.39). It is of course much harder to prove than (16.39). This is accounted for by the fact that $\mathfrak{L}_1([- \pi, \pi]) \supset \mathfrak{L}_2([- \pi, \pi])$, while $\mathfrak{L}_2(R)$ neither contains nor is contained in $\mathfrak{L}_1(R)$.

(21.55) Example. PLANCHEREL's theorem can be used to evaluate certain integrals. We illustrate by integrating FEJÉR's kernel (21.45.b). For $\alpha > 0$, it is obvious that

$$\| \xi_{[-\alpha,\alpha]} \|_2^2 = (2\pi)^{-\frac{1}{2}} \int_{[-\alpha,\alpha]} (x) dx = \left(\frac{2}{\pi}\right)^{\frac{1}{2}} \alpha.$$

By (21.52.i), we have

$$

(21.56) Exercise [W. H. Young]. Let $p, q,$ and $r$ be real numbers such that $p > 1, q > 1,$ and also $\frac{1}{p} + \frac{1}{q} - 1 = \frac{1}{r} > 0.$ Suppose that $f \in \mathfrak{L}_p(R)$ and $g \in \mathfrak{L}_q(R).$ Prove that the convolution $f * g$ is in $\mathfrak{L}_r(R)$ and that $\|f * g\|_r \leq \|f\|_p \cdot \|g\|_q.$ [Hints. Let $a, b,$ and $c$ be real numbers such that $a = r, \frac{1}{p} = \frac{1}{a} + \frac{1}{b},$ and $\frac{1}{q} = \frac{1}{a} + \frac{1}{c}.$ Note that $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = 1,$ and use the generalized Hölder inequality (13.26) on the product

$$\left( |f(x - y)|^p |g(y)|^q \right) \left( |f(x - y)|^p \left( \frac{1}{p} - \frac{1}{a} \right) \right) \left( |g(y)|^q \left( \frac{1}{q} - \frac{1}{a} \right) \right).$$

(21.57) Exercise. (a) For $f \in \mathfrak{L}_1(R)$ and $a \in R,$ let $f_a(x) = f(x + a).$ Prove that $(f_a)(y) = f(y) \exp(iax)$ for all $y \in R.$

(b) Prove that if $f \in \mathfrak{L}_1(R), a \in R,$ and $g(x) = \exp(-iax),$ then $\hat{f}g(y) = (\hat{f})_a(y)$ for all $y \in R.$

(c

(21.60) Exercise. Define $f$ on $R$ by $f(x) = \exp \left( -\frac{x^2}{2} \right)$. Use (21.59.a) to prove that $f = f$. Hints. Write $f = \varphi$. By (21.59.a) we have

$$\varphi'(y) = i(2\pi)^{-\frac{1}{2}} \int_{R} (-x) \exp \left( -\frac{x^2}{2} \right) \exp (-iyx) dx.$$

Integrate by parts to obtain $\varphi'(y) = -y\varphi(y)$ for all $y \in R$. Conclude that $\frac{d}{dy} \left[ \varphi(y) \exp \left( \frac{y^2}{2} \right) \right] = 0$ for all $y \in R$. Show that $\varphi(0) = 1$ by noticing that

$$2\pi \varphi(0)^2 = \left( \int_{R} \exp \left( -\frac{x^2}{2} \right) dx \right) \left( \int_{R} \exp \left( -\frac{y^2}{2} \right) dy \right)$$

$$= \int_{R > R} \exp \left( -\frac{(x^2 + y^2)}{2} \right) d(x, y)$$

$$= \int_{0}^{2\pi} \int_{0}^{\infty} \exp \left( -\frac{r^2}{2} \right) r dr d\theta = 2\pi.$$

(21.61) Exercise. (a) Let $\varphi \in \mathfrak{L}_1(R)$. Suppose that $\varphi$ is twice differentiable on $R$, that $\varphi', \varphi''$ are in $\mathfrak{L}_1(R)$, and that $\varphi$ and $\varphi'$ are absolutely continuous on $R$. Prove that there exists a function $f \in \mathfrak{L}_1(R)$ such that $f = \varphi$. [Use (21.59.b) to show that $\

(b) Compute

$$\int_R \left[ \frac{\sin(ay)}{y} \right]^3 dy.$$

[Use (21.53.ii), (a), and (21.55).]

(c) Evaluate

$$\int_R \left[ \frac{\sin(ay)}{y} \right]^n dy$$

for $a \in R$ and $n \in \{5, 6, 7, \ldots\}$.

(21.64) Exercise. Some rudimentary facts about analytic functions are needed in this exercise$^1$.

(a) Let $f$ and $g$ be functions in $\mathfrak{L}_1(R)$ such that $f(x) = g(x) = 0$ for all $x < 0$. Suppose that $f * g = 0$ a. e. Prove that $f = 0$ a. e. or $g = 0$ a. e. [Hints. Consider a complex number $z = s + it$ with $t \leq 0$. The Fourier transform $f$ can be extended to

$$f(z) = (2\pi)^{-\frac{1}{2}} \int_0^\infty \exp(-izx) f(x) dx.$$

Show that $f$ is an analytic function in $\{z : \operatorname{Im}z < 0\}$ and a continuous function in $\{z : \operatorname{Im}z \leq 0\}$. Show that

$$\hat{f * g}(z) = \hat{f}(z) \hat{g}(z) \quad \text{for} \quad \operatorname{Im}z \leq 0.$$

Thus the analytic function $\hat{f} \hat{g}$ vanishes identically in $\{z : \operatorname{Im}z < 0\}$, and this implies that $\hat{f} = 0$ or $\hat{g} = 0$, in $\{z : \operatorname{Im}z < 0\}$. If $\hat{f} = 0$, then $\hat{f}(s) = 0$ as well for all $s \in R$, and the uniqueness theorem

If $f$ is orthogonal to all of the Hermite functions, then we have

$$F^{(n)}(0) = (2\pi)^{-\frac{1}{2}} (-i)^n \int_R x^n \exp \left( -\frac{x^2}{2} \right) \overline{f(x)} \, dx = 0$$

for all $n \in \{0, 1, 2, \ldots\}$, and so $F$ itself must vanish identically. For real $z$, this yields

$$0 = F(s + i 0) = (2\pi)^{-\frac{1}{2}} \int_R \exp (-i s x) \exp \left( -\frac{x^2}{2} \right) \overline{f(x)} \, dx$$

and so by (21.47), $\exp \left( -\frac{x^2}{2} \right) f(x) = 0$ a. e. Therefore $f = 0$ a. e.]

(21.65) Exercise: More on the structure of $\mathfrak{L}_1(R)$. In this exercise, we point out some algebraic properties of the Banach algebra $\mathfrak{L}_1(R)$ analogous to those obtained in (20.52) for $\mathfrak{C}_0(X)$.

(a) Let $\mathfrak{I}$ be a closed ideal in $\mathfrak{L}_1(R)$ [for the definition, see (20.52)]. Prove that $f \in \mathfrak{I}$ and $a \in R$ imply $f_a \in \mathfrak{I}$. [Hints. For $g$, $h \in \mathfrak{L}_1(R)$ and $a \in R$, check that

$$(g_a) * h = g * (h_a) = (g * h)_a.$$

Now if $(u^{(n)})$ is an approximate unit in $\mathfrak{L}_1(R)$ (21.36), the relations

$$u^{(n)} * (f_a) \rightarrow f_a, \quad (u_a^{(n)}) * f \in \mathfrak{I

and by (13.24) we have $\lim_{y \to 0} |\chi(x + y) - \chi(x)| = 0$. Thus $\chi$ is continuous. Also $|\chi(x)| = |M(f_x)| \leq \|f_x\|_1 = \|f\|_1$, so that $\chi$ is bounded. This implies that $|\chi| = 1.$

(e) Let $M$ and $\chi$ be as in parts (b) and (d). Then we have

$$M(f) = (2\pi)^{-\frac{1}{2}} \int_R \overline{\chi(x)} f(x) dx$$

for all $f \in \mathfrak{L}_1(R)$. [Hints. By (20.19), there is an $h \in \mathfrak{L}_\infty(R)$ such that $M(f) = (2\pi)^{-\frac{1}{2}} \int_R fh d\lambda$ for all $f \in \mathfrak{L}_1(R)$. Take $g \in \mathfrak{L}_1(R)$ such that $M(g) = 1$. Then for all $y \in R$,

$$\overline{\chi(y)} = M(g_y) = (2\pi)^{-\frac{1}{2}} \int_R g(x - y) h(x) dx.$$

For an arbitrary $f \in \mathfrak{L}_1(R)$, we thus have

$$(2\pi)^{-\frac{1}{2}} \int_R f(y) \overline{\chi(y)} dy = (2\pi)^{-1} \int_R g(x - y) h(x) dx f(y) dy$$

$$= (2\pi)^{-1} \int_R g(x - y) f(y) dy h(x) dx$$

$$= (2\pi)^{-\frac{1}{2}} \int_R g * f(x) h(x) dx$$

$$= M(g * f)$$

$$= M(f).$$

(f) Every multiplicative linear functional $M$ on the Banach algebra $\mathfrak{L}_1(R)$ has the form

$$M(f) = (2\pi)^{-

see W. RUDIN, Fourier Analysis on Groups [Interscience Publishers, New York, 1962], Chapter 7.

We now turn to a quite different application of Fubini's theorem, obtaining a formula for integration by parts under very general circumstances.
