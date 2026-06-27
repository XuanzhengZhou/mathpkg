---
role: proof
locale: en
of_concept: martinelli-bochner-kernel-estimate
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.2"
---
# Proof of Lemma 13.2 (Martinelli-Bochner Kernel Estimate)

**Lemma 13.2.** $K_{MB}$ satisfies conditions (4), (5), and (6) on each smoothly bounded domain $D \subseteq \mathbb{C}^n$. The constant $c_0$ in (5) equals $\frac{(2\pi i)^n}{(n-1)!}$.

Recall

$$K_{MB}(\zeta, z) = \sum_{j=1}^{n} \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^{2n}} \; d\bar{\zeta}_1 \wedge d\zeta_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_j} \wedge d\zeta_j \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_n. \tag{9}$$

**Proof.** For each $j$, $1 \leq j \leq n$, we put

$$\omega_j = d\bar{\zeta}_1 \wedge d\zeta_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_j} \wedge d\zeta_j \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_n, \tag{10}$$

and

$$\beta = d\bar{\zeta}_1 \wedge d\zeta_1 \wedge d\bar{\zeta}_2 \wedge d\zeta_2 \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_n. \tag{11}$$

Note that

$$d\bar{\zeta}_j \wedge \omega_j = \beta \quad \text{for each } j.$$

**Verification of (4).** We compute $dK_{MB}$:

$$dK_{MB} = \sum_{j=1}^{n} d\left[\frac{\bar{\zeta}_j - \bar{z}_j}{(|\zeta - z|^2)^{n}}\right] \wedge \omega_j$$

$$= \sum_{j=1}^{n} \left[\frac{|\zeta - z|^{2n} d\bar{\zeta}_j - (\bar{\zeta}_j - \bar{z}_j) n(|\zeta - z|^2)^{n-1} d(|\zeta - z|^2)}{|\zeta - z|^{4n}}\right] \wedge \omega_j.$$

Now,

$$d(|\zeta - z|^2) = d\left[\sum_{k=1}^{n} (\zeta_k - z_k)(\bar{\zeta}_k - \bar{z}_k)\right] = \sum_{k=1}^{n} \left[(\zeta_k - z_k) d\bar{\zeta}_k + (\bar{\zeta}_k - \bar{z}_k) d\zeta_k\right].$$

Since $\omega_j$ contains each $d\zeta_k$ as a factor, $d\zeta_k \wedge \omega_j = 0$ for all $k$. Similarly, $d\bar{\zeta}_k \wedge \omega_j = 0$ unless $j = k$. Finally, $d\bar{\zeta}_j \wedge \omega_j = \beta$ by (11). Hence

$$dK_{MB} = \frac{1}{|\zeta - z|^{4n}} \sum_{j=1}^{n} \left[|\zeta - z|^{2n} d\bar{\zeta}_j \wedge \omega_j - |\zeta_j - z_j|^2 n(|\zeta - z|^{2n-2}) d\bar{\zeta}_j \wedge \omega_j\right]$$

$$= \frac{1}{|\zeta - z|^{4n}} \left[n |\zeta - z|^{2n} \beta - n |\zeta - z|^{2n-2} \sum_{j=1}^{n} |\zeta_j - z_j|^2 \beta\right]$$

Since $\sum_{j=1}^{n} |\zeta_j - z_j|^2 = |\zeta - z|^2$, the bracket becomes

$$n |\zeta - z|^{2n} \beta - n |\zeta - z|^{2n-2} |\zeta - z|^2 \beta = 0.$$

Thus $dK_{MB} = 0$ on $\mathbb{C}^n \setminus \{z\}$, verifying (4).

**Verification of (5).** We evaluate $\int_{|\zeta-z|=\epsilon} K_{MB}$ by reducing to the unit sphere. After the change of variable $\zeta = z + \epsilon b$, each component of the integral contributes

$$\int_{|\zeta-z|=\epsilon} \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^{2n}} \omega_j = \frac{1}{\epsilon^{2n}} \int_{|\zeta-z|=\epsilon} (\bar{\zeta}_j - \bar{z}_j) \omega_j.$$

With $\zeta = z + \epsilon b$, we have $\bar{\zeta}_j - \bar{z}_j = \epsilon \bar{b}_j$ and $\omega_j$ becomes $\epsilon^{2n-1}$ times the analogous form in $b$. Hence

$$\int_{|\zeta-z|=\epsilon} K_{MB} = \sum_{j=1}^{n} \int_{|b|=1} \bar{b}_j \; d\bar{b}_1 \wedge db_1 \wedge \cdots \wedge \widehat{d\bar{b}_j} \wedge db_j \wedge \cdots \wedge d\bar{b}_n \wedge db_n.$$

Each summand equals $(2i)^n \pi^n / n!$, so the sum over $j$ gives

$$\int_{|\zeta-z|=\epsilon} K_{MB} = n(2i)^n \frac{\pi^n}{n!} = \frac{(2\pi i)^n}{(n-1)!}.$$

Thus (5) holds with $c_0 = \frac{(2\pi i)^n}{(n-1)!}$.

**Verification of (6).** Let $g$ be a continuous function on $\mathbb{C}^n$. Fix $z \in \mathbb{C}^n$, $\epsilon > 0$:

$$\int_{|\zeta-z|=\epsilon} g K_{MB} = \sum_{j=1}^{n} \frac{1}{\epsilon^{2n}} \int_{|\zeta-z|=\epsilon} g(\zeta)(\bar{\zeta}_j - \bar{z}_j) \omega_j.$$

Make the change of variable $\zeta = z + \epsilon b$, where $b \in \mathbb{C}^n$ lies on the unit sphere $S = \{b : \sum |b_j|^2 = 1\}$. Then

$$\int_{|\zeta-z|=\epsilon} g(\zeta)(\bar{\zeta}_j - \bar{z}_j) \omega_j = \int_S g(z + \epsilon b) (\epsilon \bar{b}_j) (\epsilon^{2n-1}) \sigma_j,$$

where $\sigma_j$ is a $(2n-1)$-form in $b$, independent of $z$ and $\epsilon$. Hence

$$\int_{|\zeta-z|=\epsilon} g K_{MB} = \sum_{j=1}^{n} \int_S g(z + \epsilon b) \bar{b}_j \sigma_j.$$

For each $j$, there exists a constant $k_j$ such that

$$\left| \int_S h(b) \sigma_j \right| \leq k_j \max_S |h(b)|,$$

by continuity of the linear functional $h \mapsto \int_S h \sigma_j$ on $C(S)$. Taking $M = \sum_j k_j$, we obtain

$$\left| \int_{|\zeta-z|=\epsilon} g(\zeta) K_{MB}(\zeta,z) \right| \leq M \max_{|\zeta-z|=\epsilon} |g(\zeta)|.$$

This verifies (6) and completes the proof. $\square$

**Remark.** It follows immediately from (4) and Stokes' Theorem that $\int_{\partial D} K_{MB}(\zeta, z) = 0$ if $z \in \mathbb{C}^n \setminus \bar{D}$.
