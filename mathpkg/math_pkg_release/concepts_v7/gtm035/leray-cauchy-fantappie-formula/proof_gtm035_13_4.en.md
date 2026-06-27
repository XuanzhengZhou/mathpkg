---
role: proof
locale: en
of_concept: leray-cauchy-fantappie-formula
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.4"
---
# Proof of Theorem 13.4 (Leray's Cauchy-Fantappie Formula)

Let $D \subseteq \mathbb{C}^n$ be a smoothly bounded domain. Fix functions $w_1(\zeta,z), \ldots, w_n(\zeta,z)$, defined and smooth on $\bar{D} \times \bar{D} \setminus \{\zeta = z\}$, satisfying

$$\sum_{j=1}^{n} w_j(\zeta, z)(\zeta_j - z_j) = 1, \quad \zeta \in \bar{D}, \; z \in \bar{D}, \; \zeta \neq z. \tag{13}$$

Define the Cauchy-Fantappie form

$$K_w(\zeta, z) = \sum_{j=1}^{n} (-1)^{j-1} w_j \; dw_1 \wedge \cdots \wedge \widehat{dw_j} \wedge \cdots \wedge dw_n \wedge d\zeta_1 \wedge \cdots \wedge d\zeta_n. \tag{14}$$

**Theorem 13.4 (Leray's Formula).** For each $f \in A(D) \cap \mathcal{C}^1(\bar{D})$ and $z \in D$,

$$f(z) = a_0 \int_{\partial D} f(\zeta) K_w(\zeta, z), \tag{15}$$

where $a_0 = \frac{(-1)^{n(n-1)/2}(n-1)!}{(2\pi i)^n}$.

**Proof.** We begin by introducing new variables $Z = (Z_1, \ldots, Z_n)$ and $W = (W_1, \ldots, W_n)$ in $\mathbb{C}^{2n}$ and consider the complex manifold $\Sigma_0$ defined by

$$\Sigma_0 = \{(Z, W) \in \mathbb{C}^{2n} : \sum_{k=1}^{n} W_k Z_k = 1, \; Z \in D\}. \tag{16}$$

$\Sigma_0$ is a $(2n-1)$-dimensional complex manifold (in fact, a domain in a complex hypersurface in $\mathbb{C}^{2n}$).

We first need a lemma concerning holomorphic forms on a complex submanifold.

**Lemma 13.5.** Let $\Sigma$ be a $k$-dimensional complex submanifold of $\mathbb{C}^N$ and let $\alpha$ be a holomorphic $k$-form on $\mathbb{C}^N$. If we denote by $\alpha|_\Sigma$ the form on $\Sigma$ obtained by restricting $\alpha$ to $\Sigma$, then

$$d\alpha|_\Sigma = 0 \quad \text{on } \Sigma.$$

*Proof of Lemma 13.5.* Let $j : \Sigma \to \mathbb{C}^N$ be the (holomorphic) inclusion map. Then $\alpha|_\Sigma = j^*(\alpha)$ is the pullback. By a standard property of pullbacks, $d(j^*(\alpha)) = j^*(d\alpha)$. Hence $d\alpha|_\Sigma$ is a holomorphic $(k+1)$-form on $\Sigma$, being the pullback of the holomorphic $(k+1)$-form $d\alpha$ on $\mathbb{C}^N$. Since there are no nonzero holomorphic $(k+1)$-forms on a complex $k$-dimensional manifold, we conclude that $d\alpha|_\Sigma = 0$ on $\Sigma$.

We now continue with the proof of Theorem 13.4. Fix $f \in A(D) \cap \mathcal{C}^1(\bar{D})$ and define a form $\alpha$ on $\mathbb{C}^{2n} \cap \{Z \in D\}$ by

$$\alpha = f(Z) \sum_{k=1}^{n} (-1)^{k-1} W_k \; dW_1 \wedge \cdots \wedge \widehat{dW_k} \wedge \cdots \wedge dW_n \wedge dZ_1 \wedge \cdots \wedge dZ_n. \tag{17}$$

Then $\alpha$ is a holomorphic $(2n-1)$-form on $\mathbb{C}^{2n} \cap \{Z \in D\}$ (here $f(Z)$ is independent of $W$, so $df \wedge \cdots$ vanishes by type considerations). We restrict $\alpha$ to $\Sigma_0$. By Lemma 13.5, $d(\alpha|_{\Sigma_0}) = 0$.

We next make a particular choice of functions $w_j$ by putting

$$\tilde{w}_j(\zeta, z) = \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^2}.$$

This choice satisfies (13) because $\sum_{j=1}^{n} \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^2} (\zeta_j - z_j) = \frac{|\zeta-z|^2}{|\zeta - z|^2} = 1$. The corresponding Cauchy-Fantappie form $K_{\tilde{w}}$ is related to the Bochner-Martinelli kernel by

$$K_{\tilde{w}} = \frac{1}{|\zeta - z|^{2n}} \sum_{k=1}^{n} (-1)^{k-1} (\bar{\zeta}_k - \bar{z}_k) \; d\bar{\zeta}_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_k} \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_1 \wedge \cdots \wedge d\zeta_n.$$

**Exercise 13.4.** For $q_n = n(n-1)/2$,

$$K_{MB} = (-1)^{q_n} K_{\tilde{w}}.$$

We now define a family of maps $\chi_t$, $0 \leq t \leq 1$, from $\partial D$ into $\mathbb{C}^{2n}$, given by

$$\chi_t(\zeta) = \left(\zeta, \; t \frac{\bar{\zeta} - \bar{z}}{|\zeta - z|^2} + (1-t)w(\zeta, z)\right), \quad \zeta \in \partial D.$$

For each $\zeta$, one checks that

$$\sum_{k=1}^{n} \left[ t \frac{\bar{\zeta}_k - \bar{z}_k}{|\zeta - z|^2} + (1-t) w_k(\zeta,z) \right] (\zeta_k - z_k) = t \cdot 1 + (1-t) \cdot 1 = 1,$$

so $\chi_t$ maps $\partial D$ into $\Sigma_0$ for each $t$.

We now integrate $\alpha$ over the image of $\partial D$ under $\chi_t$. Since $d\alpha|_{\Sigma_0} = 0$, by Stokes' Theorem the integral is independent of $t$. In particular,

$$\int_{\chi_0(\partial D)} \alpha = \int_{\chi_1(\partial D)} \alpha. \tag{18}$$

From the definition of $\alpha$ and of the maps $\chi_0$ and $\chi_1$, we have

$$\int_{\chi_0(\partial D)} \alpha = \int_{\partial D} f(\zeta) \sum_{k=1}^{n} (-1)^{k-1} w_k \; dw_1 \wedge \cdots \wedge \widehat{dw_k} \wedge \cdots \wedge dw_n \wedge d\zeta = \int_{\partial D} f(\zeta) K_w(\zeta, z),$$

and similarly

$$\int_{\chi_1(\partial D)} \alpha = \int_{\partial D} f(\zeta) K_{\tilde{w}}(\zeta, z).$$

By (18), the two integrals over $\partial D$ are equal. Using Exercise 13.4,

$$K_{\tilde{w}}(\zeta, z) = (-1)^{q_n} K_{MB}(\zeta, z).$$

Therefore

$$\int_{\partial D} f(\zeta) K_w(\zeta, z) = (-1)^{q_n} \int_{\partial D} f(\zeta) K_{MB}(\zeta, z).$$

By Theorem 13.3 (the Martinelli-Bochner formula),

$$\int_{\partial D} f(\zeta) K_{MB}(\zeta, z) = \frac{(2\pi i)^n}{(n-1)!} f(z).$$

Hence

$$\int_{\partial D} f(\zeta) K_w(\zeta, z) = (-1)^{q_n} \frac{(2\pi i)^n}{(n-1)!} f(z).$$

Since $q_n = n(n-1)/2$, we have $(-1)^{q_n} = (-1)^{n(n-1)/2}$, and solving for $f(z)$ yields

$$f(z) = \frac{(-1)^{n(n-1)/2} (n-1)!}{(2\pi i)^n} \int_{\partial D} f(\zeta) K_w(\zeta, z).$$

Setting $a_0 = \frac{(-1)^{n(n-1)/2} (n-1)!}{(2\pi i)^n}$ gives (15). $\square$
