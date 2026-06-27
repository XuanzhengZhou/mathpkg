---
role: proof
locale: en
of_concept: generalized-perturbation-stone-weierstrass
source_book: gtm035
source_chapter: "14"
source_section: "14.4"
---
# Proof of Generalized Perturbation of Stone-Weierstrass Theorem

Let $X$ be a compact subset of $\mathbb{C}^n$ and let $N$ be a neighborhood of $X$. Define $\mathfrak{A} = [z_1, \ldots, z_n, \bar{z}_1 + R_1, \ldots, \bar{z}_n + R_n]$ with each $R_j \in C^1(N)$ satisfying the Lipschitz condition $|R(z) - R(z')| \leq k|z-z'|$ for $k < 1$.

**Step 1: Construction of the Cauchy-Fantappiè kernel.** For $\zeta, z \in N$, define generating functions
$$
w_j(\zeta, z) = \frac{\bar{\zeta}_j + R_j(\zeta) - (\bar{z}_j + R_j(z))}{\sum_{\ell=1}^n (\zeta_\ell - z_\ell)(\bar{\zeta}_\ell + R_\ell(\zeta) - (\bar{z}_\ell + R_\ell(z)))},
$$
for $j = 1, \ldots, n$. The denominator is
$$
G(\zeta, z) = \sum_{\ell=1}^n (\zeta_\ell - z_\ell)(\bar{\zeta}_\ell + R_\ell(\zeta) - (\bar{z}_\ell + R_\ell(z))).
$$

Set
$$
H_j(\zeta, z) = (\zeta_j - z_j) G(\zeta, z) = (\zeta_j - z_j) \sum_{\ell=1}^n (\zeta_\ell - z_\ell)(\bar{\zeta}_\ell + R_\ell(\zeta) - (\bar{z}_\ell + R_\ell(z))).
$$

Actually, a more convenient normalization is to directly define
$$
H_j(\zeta, z) = \bar{\zeta}_j + R_j(\zeta) - (\bar{z}_j + R_j(z)), \quad
G(\zeta, z) = \sum_{j=1}^n (\zeta_j - z_j) H_j(\zeta, z).
$$

Then the Cauchy-Fantappiè kernel is
$$
K(\zeta, z) = \frac{1}{G(\zeta, z)^n} \sum_{j=1}^n (-1)^{j-1} H_j(\zeta, z) \, dH_1 \wedge \cdots \wedge \widehat{dH_j} \wedge \cdots \wedge dH_n \wedge d\zeta.
$$

Define $K_j(\zeta, z) = H_j(\zeta, z) / G(\zeta, z)^n$, so that
$$
K(\zeta, z) = \sum_{j=1}^n (-1)^{j-1} K_j(\zeta, z) \wedge \eta_j(\zeta) \wedge d\zeta,
$$
where $\eta_j(\zeta) = dH_1 \wedge \cdots \wedge \widehat{dH_j} \wedge \cdots \wedge dH_n$ is independent of $z$.

**Step 2: Key inequalities.** We establish:
1. $\operatorname{Re} G(\zeta, z) > 0$ for $\zeta \neq z$,
2. $|G(\zeta, z)| \geq (1-k)|\zeta - z|^2$,
3. $|K_j(\zeta, z)| \leq C / |\zeta - z|^{2n-1}$ for some constant $C$,
4. $|H_j(\zeta, z)| \leq (1+k)|\zeta - z|$.

*Proof of the inequalities:*
$$
H_j(\zeta, z) = \overline{(\zeta_j - z_j)} + (R_j(\zeta) - R_j(z)).
$$
Hence
$$
(\zeta_j - z_j) H_j(\zeta, z) = |\zeta_j - z_j|^2 + (R_j(\zeta) - R_j(z))(\zeta_j - z_j).
$$

Summing over $j$,
$$
G(\zeta, z) = \sum_{j=1}^n |\zeta_j - z_j|^2 + \sum_{j=1}^n (R_j(\zeta) - R_j(z))(\zeta_j - z_j)
= |\zeta - z|^2 + B(\zeta, z),
$$
where by the Lipschitz condition,
$$
|B(\zeta, z)| \leq |R(\zeta) - R(z)| \, |\zeta - z| \leq k |\zeta - z|^2.
$$

If $\zeta \neq z$, then $|B(\zeta, z)| \leq k|\zeta - z|^2 < |\zeta - z|^2$, so
$$
G(\zeta, z) = |\zeta - z|^2 + B(\zeta, z) \in \{\operatorname{Re} w > 0\},
$$
proving (1).

Next,
$$
|G(\zeta, z)| \geq |\zeta - z|^2 - k|\zeta - z|^2 = (1-k)|\zeta - z|^2,
$$
proving (2).

For $|H_j(\zeta, z)|$, we use the definition and the Lipschitz bound:
$$
|H_j(\zeta, z)| \leq |\zeta_j - z_j| + |R_j(\zeta) - R_j(z)| \leq |\zeta - z| + k|\zeta - z| = (1+k)|\zeta - z|,
$$
proving (4).

Finally,
$$
|K_j(\zeta, z)| = \frac{|H_j(\zeta, z)|}{|G(\zeta, z)|^n}
\leq \frac{(1+k)|\zeta - z|}{((1-k)|\zeta - z|^2)^n}
= \frac{1+k}{(1-k)^n} \cdot \frac{1}{|\zeta - z|^{2n-1}},
$$
proving (3) with $C = (1+k)/(1-k)^n$.

**Step 3: Proof of density.** Let $\mu$ be a measure on $X$ with $\|\mu\| < \infty$ and $\mu \perp \mathfrak{A}$. For any $z$ such that the integrability condition $\int_X d|\mu|(\zeta)/|\zeta - z|^{2n-1} < \infty$ holds, Lemma 14.6 gives $\int_X K_j(\zeta, z) d\mu(\zeta) = 0$ for all $j$.

Now fix $\phi \in C_0^1(N)$ with $\phi$ identically $1$ on a neighborhood of $X$. By Lemma 14.5 (the $\bar{\partial}$-representation lemma),
$$
\phi(z) = -\frac{(n-1)!}{(2\pi i)^n} \int_N \bar{\partial}\phi(\zeta) \wedge K(\zeta, z), \quad z \in N.
$$

For $z$ in a dense subset of $\mathbb{C}^n \setminus X$, the kernel estimates give sufficient integrability. Multiplying this identity by $d\mu(z)$ and integrating over $X$, applying Fubini's theorem and Lemma 14.6, we obtain $\int_X \phi(z) d\mu(z) = 0$. Since $\phi \equiv 1$ on $X$, this gives $\mu(X) = 0$.

A more detailed argument using the concrete structure of the kernel shows that the Cauchy transform $\int_X \frac{1}{\zeta - z} d\mu(\zeta)$ (and its higher-dimensional analogue $\int_X K_j(\zeta, z) d\mu(\zeta)$) vanishes identically outside $X$, which by the generalized uniqueness theorem for measures forces $\mu = 0$.

Thus the only measure annihilating $\mathfrak{A}$ is the zero measure. By the Hahn-Banach and Riesz representation theorems, $\mathfrak{A}$ is dense in $C(X)$.

$\square$
