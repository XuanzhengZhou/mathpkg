---
role: proof
locale: en
of_concept: proposition-18-14
source_book: gtm055
source_chapter: "18-19"
source_section: "Section 20_Section_20"
---

Proof. Let us denote by $\mathcal{L}$ the linear submanifold of $\mathcal{C}(K)$ consisting of (the restrictions to $K$ of) those rational functions having their poles in $P$. We are to show that $f$ belongs to $\mathcal{L}^-$, and by Proposition 14.10 (a consequence of the Hahn–Banach theorem) it suffices to show that if a bounded linear functional $\varphi$

by assumption, this shows that $h$ vanishes identically on the disc $D_d(\alpha)$, and hence on all of $V$ by the identity theorem (Th. 5.2). Thus $h \equiv 0$ on $\mathbb{C} \setminus K$. (If the only point of $P$ in the unbounded component of $\hat{\mathbb{C}} \setminus K$ is the point at infinity, then the argument must be modified on that component in that the series (8) is replaced by

$$-\sum_{n=0}^{\infty} \frac{\zeta^n}{\lambda^{n+1}}, \quad |\lambda| > R,$$

where $R$ is chosen large enough so that $K \subset D_R$.)

Now let $\gamma$ be an oriented envelope of $K$ in $U$ (Prob. 5K), so that

$$f(\lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} d\zeta$$

for all $\lambda$ in some neighborhood of $K$ by the Cauchy integral formula (Prob. 5O). Then

$$\int_K f d\xi = \frac{1}{2\pi i} \int_K \left[ \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} d\zeta \right] d\xi(\lambda)$$

$$= \frac{1}{2\pi i} \int_{\gamma} f(\zeta) \left[ \int_K \frac{d\xi(\lambda)}{\zeta - \lambda} \right] d\zeta$$

$$= \frac{-1}{2\pi i} \int_{\gamma} f(\zeta) h(\zeta) d\zeta = 0$$

by the Fubini theorem for complex measures (see Problem 9F).

**Example J.** Let $K$ be a compact subset of the unit circle $Z$ such that $K \neq Z$. Then the function $\bar{\lambda}$ possesses an analytic extension (namely $1/\lambda$) to a neighborhood of $K$, and $\mathbb{C} \setminus K$ is connected. Hence

$\gamma$ is an oriented envelope of $K$ in $U$, then any suitably chosen Riemann sum approximating the Cauchy integral

$$\frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} d\zeta$$

will approximate $f$ as closely as desired in $\mathcal{C}(K)$. The fact that Proposition 18.14 permits us to place the poles of the approximating rational functions in a specified set (provided this set contains at least one point of each component of $\hat{\mathbb{C}} \setminus K$) is particularly useful.
