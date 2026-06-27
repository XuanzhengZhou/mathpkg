---
role: proof
locale: en
of_concept: bochner-martinelli-integral-representation
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.1"
---
# Proof of Theorem 13.1 (Bochner-Martinelli Integral Representation)

**Theorem 13.1.** Assume that $K$ is given by (1) and satisfies (4), (5), and (6). Then, for each $f \in A(D) \cap \mathcal{C}^1(\bar{D})$, we have

$$c_0 f(z) = \int_{\partial D} f(\zeta) K(\zeta, z), \quad z \in D.$$

**Proof.** Fix $\epsilon > 0$ and put $D_\epsilon = D \setminus \{|\zeta - z| \leq \epsilon\}$. On $\overline{D}_\epsilon$, consider the differential form $f(\zeta)K(\zeta,z)$. We compute

$$d(fK) = df \wedge K + f dK.$$

By condition (4), $dK = 0$ on $D \setminus \{z\}$, so $dK = 0$ on $D_\epsilon$. Since $f$ is holomorphic on $D$, its differential $df$ contains only $d\zeta_j$ terms (no $d\bar{\zeta}_j$ terms). Specifically,

$$df = \sum_{j=1}^{n} \frac{\partial f}{\partial \zeta_j} d\zeta_j.$$

Now $K$ is a form of bidegree $(n, n-1)$ in $\zeta$. Since $df$ is of bidegree $(1, 0)$, the wedge product $df \wedge K$ is a form of bidegree $(n+1, n-1)$ on $\mathbb{C}^n$, and such a form must vanish identically because the $\zeta$-space has complex dimension $n$, so any form with more than $n$ holomorphic differentials $d\zeta_j$ is zero. Therefore $d(fK) = 0$ on $D_\epsilon$.

Applying Stokes' Theorem,

$$0 = \int_{D_\epsilon} d(fK) = \int_{\partial D_\epsilon} fK.$$

Now $\partial D_\epsilon = \partial D \cup \{|\zeta - z| = \epsilon\}$, where the sphere is oriented as the inner boundary. Hence

$$\int_{\partial D} fK - \int_{|\zeta - z| = \epsilon} fK = 0,$$

so

$$\int_{\partial D} fK = \int_{|\zeta - z| = \epsilon} fK. \tag{8}$$

We now decompose the integral over the sphere:

$$\int_{|\zeta - z| = \epsilon} f(\zeta)K = \int_{|\zeta - z| = \epsilon} (f(\zeta) - f(z))K + f(z) \int_{|\zeta - z| = \epsilon} K.$$

By condition (5), $\int_{|\zeta - z| = \epsilon} K = c_0$, a constant independent of $z$ and $\epsilon$.

By condition (6), there exists a constant $M$ such that

$$\left| \int_{|\zeta - z| = \epsilon} (f(\zeta) - f(z)) K \right| \leq M \max_{|\zeta - z| = \epsilon} |f(\zeta) - f(z)|.$$

Since $f$ is continuous at $z$,

$$\lim_{\epsilon \to 0} \max_{|\zeta - z| = \epsilon} |f(\zeta) - f(z)| = 0,$$

and consequently

$$\lim_{\epsilon \to 0} \left[ \int_{|\zeta - z| = \epsilon} (f(\zeta) - f(z)) K \right] = 0.$$

It follows from (8), letting $\epsilon \to 0$, that

$$\int_{\partial D} f K = c_0 f(z).$$

Thus (7) is proved. $\square$
