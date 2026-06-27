---
role: proof
locale: en
of_concept: rational-approximation-with-specified-poles
source_book: gtm055
source_chapter: "18"
source_section: "20"
---

Let $\mathcal{L}$ denote the linear submanifold of $\mathcal{C}(K)$ consisting of (the restrictions to $K$ of) those rational functions having their poles in $P$. We are to show that $f$ belongs to $\mathcal{L}^-$, and by Proposition 14.10 (a consequence of the Hahn-Banach theorem) it suffices to show that if a bounded linear functional $\varphi$ on $\mathcal{C}(K)$ annihilates $\mathcal{L}$, then $\varphi(f) = 0$.

By the Riesz representation theorem, $\varphi$ is given by integration against a regular complex Borel measure $\xi$ on $K$: $\varphi(g) = \int_K g \, d\xi$ for $g \in \mathcal{C}(K)$. For any $\lambda \notin K$, define $h(\lambda) = \int_K \frac{d\xi(\zeta)}{\zeta - \lambda}$, which is analytic on $\mathbb{C} \setminus K$.

If $\lambda \in P \setminus K$, then $\zeta \mapsto 1/(\zeta - \lambda)$ belongs to $\mathcal{L}$, and since $\varphi$ annihilates $\mathcal{L}$, we have $h(\lambda) = 0$. Let $V$ be a connected component of $\mathbb{C} \setminus K$. Since $P$ contains at least one point of $V \cup \{\infty\}$ (in $\hat{\mathbb{C}} \setminus K$), the function $h$ vanishes at that point. The series expansion shows $h$ vanishes identically on a disc about that point, and hence on all of $V$ by the identity theorem (Theorem 5.2). Thus $h \equiv 0$ on $\mathbb{C} \setminus K$. (If the only point of $P$ in the unbounded component is $\infty$, the series is modified to $-\sum_{n=0}^{\infty} \zeta^n/\lambda^{n+1}$ for $|\lambda| > R$ with $K \subset D_R$.)

Now let $\gamma$ be an oriented envelope of $K$ in $U$ (Problem 5K), so that $f(\lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} \, d\zeta$ for all $\lambda$ in some neighborhood of $K$. Then
$$\int_K f \, d\xi = \frac{1}{2\pi i} \int_K \left[ \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} \, d\zeta \right] d\xi(\lambda) = \frac{1}{2\pi i} \int_{\gamma} f(\zeta) \left[ \int_K \frac{d\xi(\lambda)}{\zeta - \lambda} \right] d\zeta$$
$$= \frac{-1}{2\pi i} \int_{\gamma} f(\zeta) h(\zeta) \, d\zeta = 0$$
by Fubini's theorem for complex measures (Problem 9F). Thus $\varphi(f) = \int_K f \, d\xi = 0$, completing the proof.
