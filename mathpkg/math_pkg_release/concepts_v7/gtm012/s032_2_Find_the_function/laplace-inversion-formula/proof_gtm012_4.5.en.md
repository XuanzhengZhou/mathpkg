---
role: proof
locale: en
of_concept: laplace-inversion-formula
source_book: gtm012
source_chapter: "4"
source_section: "§5"
---

# Proof of Laplace inversion formula

Let $b > \max\{a,0\}$ and let $C$ be the vertical line $\{z \in \mathbb{C} \mid \operatorname{Re} z = b\}$. By the estimate from Theorem 5.1, $g = Lf$ is bounded on $C$:

$$|g(z)| \leq K \, (b - a)^{-1} \, \exp(M(a - b)), \qquad z \in C.$$

Therefore the integral
$$F(t) = \frac{1}{2\pi i} \int_{C} e^{zt} z^{-2} g(z) \, dz$$

converges absolutely for every $t$, since the factor $z^{-2}$ gives $O(|z|^{-2})$ decay as $|\operatorname{Im} z| \to \infty$.

For each $N > 0$, define the truncated Laplace transform
$$g_N(z) = \int_{-N}^{N} e^{-zt} f(t) \, dt.$$

The functions $g_N$ are entire and converge uniformly to $g$ on the line $C$ (by the exponential bound on $f$ and the fact that $b > a$). Moreover, $|g_N(z)| \leq C (1+|z|)^{-1}$ uniformly in $N$ on $C$.

Define
$$F_N(t) = \frac{1}{2\pi i} \int_{C} e^{zt} z^{-2} g_N(z) \, dz.$$

Then $F_N(t) \to F(t)$ as $N \to \infty$ for each $t$. Substituting the definition of $g_N$ and interchanging the order of integration (justified by absolute convergence):

$$F_N(t) = \frac{1}{2\pi i} \int_{C} e^{zt} z^{-2} \int_{-N}^{N} e^{-zs} f(s) \, ds \, dz$$
$$= \int_{-N}^{N} \left\{ \frac{1}{2\pi i} \int_{C} e^{z(t-s)} z^{-2} \, dz \right\} f(s) \, ds.$$

We now evaluate the inner contour integral
$$I(t-s) = \frac{1}{2\pi i} \int_{C} e^{z(t-s)} z^{-2} \, dz.$$

**Case 1: $s > t$.** The integrand $e^{z(t-s)} z^{-2}$ is holomorphic in the right half-plane $\operatorname{Re} z > b$ (the exponential factor $e^{z(t-s)}$ decays exponentially since $t-s < 0$). By Cauchy's theorem, closing the contour to the right gives $I(t-s) = 0$.

**Case 2: $s < t$.** Let $C_R$ be the semicircle of radius $R$ to the left of $C$, and let $C'_R$ be its reflection about the line $C$. For $R > b$, the residue theorem gives:

$$\frac{1}{2\pi i} \int_{C'_R} e^{z(t-s)} z^{-2} \, dz = \operatorname{Res}_{z=0}\left( e^{z(t-s)} z^{-2} \right) = \frac{d}{dz} e^{z(t-s)} \Big|_{z=0} = t - s.$$

Taking the limit as $R \to \infty$, the contribution from the semicircular arc vanishes (by the Jordan lemma estimate: $|e^{z(t-s)}| = e^{\operatorname{Re} z (t-s)} \to 0$ as $\operatorname{Re} z \to -\infty$ when $t-s > 0$). Therefore
$$I(t-s) = t - s, \qquad s < t.$$

Combining both cases, we obtain
$$\frac{1}{2\pi i} \int_{C} e^{z(t-s)} z^{-2} \, dz = \begin{cases} t - s, & s < t, \\ 0, & s > t. \end{cases}$$

Thus
$$F(t) = \lim_{N \to \infty} F_N(t) = \int_{-\infty}^{t} (t-s) f(s) \, ds.$$

Differentiating twice with respect to $t$, we get $D^{2} F(t) = f(t)$. In the sense of distributions, $D^{2} F = f$, i.e. the second distributional derivative of $F$ recovers the original function $f$. $\square$
