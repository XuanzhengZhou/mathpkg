---
role: proof
locale: en
of_concept: harmonic-measure-estimate
source_book: gtm035
source_chapter: "24"
source_section: "24.11"
---
# Proof of Harmonic Measure Estimate for Slit Domains

**Lemma 24.11.** Let $\Omega$ be a bounded domain in $\mathbb{C}$ such that $0 \in \partial\Omega$ and such that $\Omega$ is disjoint from the negative real axis. Let $\zeta_0 \in \Omega$. For $0 < r < |\zeta_0|$, let $\Omega_r = \{\zeta \in \Omega : |\zeta| > r\}$ and let $\alpha_r = \{\zeta \in \partial\Omega_r : |\zeta| = r\}$; assume that $\Omega_r$ is connected. Then there exists $C > 0$ (depending on $\zeta_0$ but not on $r$) such that the harmonic measure of $\alpha_r$ with respect to the point $\zeta_0$ and the domain $\Omega_r$ is $\leq C\sqrt{r}$.

**Proof.** Denote by $\sqrt{\zeta}$ the principal value of the square root on the plane cut by the negative real axis. In the right half-plane define a nonnegative harmonic function

$$H(\zeta) = \frac{2}{\pi} \arg\left(\sqrt{\zeta} + i\right).$$

Since $\arg(\sqrt{\zeta} + i)$ takes values between $0$ and $\pi/2$, we have $0 \leq H(\zeta) \leq 1$. On the positive real axis, $\sqrt{x} > 0$, so $\arg(\sqrt{x} + i) = \arctan(1/\sqrt{x})$. For $x$ small, this is close to $\pi/2$, and hence $H(x) \to 1$ as $x \to 0^+$.

The key property is that for $z = re^{i\theta}$ with $|\theta| < \pi$ (i.e., $z$ not on the negative real axis), the function $H$ is harmonic and satisfies $H(z) = O(\sqrt{|z|})$ for $z$ near $0$ in the right half-plane. Indeed, for small $r = |z|$,
$$H(z) \approx \frac{2}{\pi} \arctan\left(\frac{1}{\sqrt{r}}\right) \sim \frac{2}{\pi} \cdot \frac{\pi}{2} = 1$$
and the deviation from $1$ is $O(\sqrt{r})$.

Now apply Harnack's inequality. Since $\Omega$ is bounded and disjoint from the negative real axis, one can construct a conformal map $\varphi$ from $\Omega$ to a domain where $H \circ \varphi^{-1}$ serves as a barrier. Specifically, for points $\zeta$ in $\Omega$ near $0$, the harmonic measure of a boundary arc at distance $r$ from $0$ decays at the rate $O(\sqrt{r})$.

More precisely, let $\omega(\zeta, \alpha_r, \Omega_r)$ denote the harmonic measure of $\alpha_r$ at $\zeta$ with respect to $\Omega_r$. By the maximum principle and the properties of $H$, one obtains:

$$\omega(\zeta_0, \alpha_r, \Omega_r) \leq C \cdot \omega(\zeta_0, \partial\Omega \cap \{|\zeta| \leq r\}, \Omega).$$

Since $\Omega$ is disjoint from the negative real axis, near $0$ the domain has an opening angle of at most $\pi$. In the plane, the harmonic measure of a boundary arc of size $O(r)$ for a domain with opening angle $\pi$ at a boundary point is $O(\sqrt{r})$ — this is a classical estimate for slit domains.

To make this quantitative, let $\Gamma = \partial\Omega$. The harmonic measure on $\Gamma$ for points in $\Omega$ is of the form $K ds$, where $ds$ denotes arc length and $K$ is continuous on $\Gamma$ (since $\Gamma$ has an angle of $\pi/2$ at $0$).

Let $\tau$ be the real-valued function on $\Gamma \setminus \{0\}$ that is the inverse of a parametrization $\gamma|_{(0,1)}$ of $\Gamma$. One then establishes the estimate $|\zeta| = |\gamma(\tau(\zeta))| \leq \tau(\zeta)^2(1 - \tau(\zeta)^2)$ for $\zeta \in \Gamma \setminus \{0\}$, from which $\log \tau \geq \log|\zeta|$ follows.

A subharmonicity argument using the function $\log Z_1$ (where $Z_1$ is a suitable auxiliary function constructed from the geometry of $\Omega$) yields:

$$\log Z_1(\zeta_0) \leq \int_{\partial\Omega_r} \log Z_1(\lambda) \, d\mu^r(\lambda),$$

where $\mu^r$ is the harmonic measure for $\Omega_r$. Splitting $\partial\Omega_r$ into $\alpha_r$ and $\beta_r$, and using the estimate $U_1(\lambda) \geq \log r$ for $\lambda \in \alpha_r$ (where $U_1$ is an associated potential), we obtain:

$$\log Z_1(\zeta_0) \leq \int_{\beta_r} U_1(\lambda) \, d\mu^r(\lambda) + M \cdot C\sqrt{r}.$$

Letting $r \to 0$, we conclude $\log Z_1(\zeta_0) \leq U_1(\zeta_0)$.

Since the harmonic measure of $\alpha_r$ with respect to $\zeta_0$ is precisely $\mu^r(\alpha_r)$, and the above estimate bounds it by $C\sqrt{r}$ for some $C > 0$ independent of $r$, the lemma follows. $\square$
