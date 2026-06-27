---
role: proof
locale: en
of_concept: random-variable-24
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Projection Theorem for Orthonormal Systems

Let $d = \inf \{ \|\xi - \zeta\| : \zeta \in \overline{\mathcal{L}} \}$ and choose a sequence $\zeta_1, \zeta_2, \ldots$ such that $\|\xi - \zeta_n\| \to d$. Let us show that this sequence is fundamental. A simple calculation shows that

$$\|\zeta_n - \zeta_m\|^2 = 2\|\zeta_n - \xi\|^2 + 2\|\zeta_m - \xi\|^2 - 4\left\|\frac{\zeta_n + \zeta_m}{2} - \xi\right\|^2.$$

It is clear that $(\zeta_n + \zeta_m)/2 \in \overline{\mathcal{L}}$; consequently $\|[ (\zeta_n + \zeta_m)/2] - \xi\|^2 \geq d^2$ and therefore $\|\zeta_n - \zeta_m\|^2 \to 0$, $n, m \to \infty$.

The space $L^2$ is complete (Theorem 7, Sect. 10). Hence there is an element $\hat{\xi}$ such that $\|\zeta_n - \hat{\xi}\| \to 0$. But $\overline{\mathcal{L}}$ is closed, so $\hat{\xi} \in \overline{\mathcal{L}}$. Moreover, $\|\zeta_n - \xi\| \to d$, and consequently $\|\xi - \hat{\xi}\| = d$, which establishes the existence of the required element.

Let us show that $\hat{\xi}$ is the only element of $\overline{\mathcal{L}}$ with the required property. Let $\tilde{\xi} \in \overline{\mathcal{L}}$ and let

$$\|\xi - \hat{\xi}\| = \|\xi - \tilde{\xi}\| = d.$$

Then by the parallelogram identity,

$$\|\hat{\xi} + \tilde{\xi} - 2\xi\|^2 + \|\hat{\xi} - \tilde{\xi}\|^2 = 2\|\hat{\xi} - \xi\|^2 + 2\|\tilde{\xi} - \xi\|^2 = 4d^2.$$

But

$$\|\hat{\xi} + \tilde{\xi} - 2\xi\|^2 = 4\left\|\frac{1}{2}(\hat{\xi} + \tilde{\xi}) - \xi\right\|^2 \geq 4d^2.$$

Consequently $\|\hat{\xi} - \tilde{\xi}\|^2 \leq 0$, i.e., $\hat{\xi} = \tilde{\xi}$ (P-a.s.).

To verify the representation $\hat{\xi} = \lim_{n\to\infty} \sum_{i=1}^{n} (\xi, \eta_i) \eta_i$, set $\hat{\xi}_n = \sum_{i=1}^{n} (\xi, \eta_i) \eta_i$. Then

$$\|\xi - \hat{\xi}_n\|^2 = \|\xi\|^2 - \sum_{i=1}^{n} |(\xi, \eta_i)|^2 \to \|\xi\|^2 - \sum_{i=1}^{\infty} |(\xi, \eta_i)|^2$$

as $n \to \infty$, and this limit equals $d^2 = \|\xi - \hat{\xi}\|^2$. Hence $\|\xi - \hat{\xi}_n\| \to \|\xi - \hat{\xi}\|$. Since $\hat{\xi}_n \in \overline{\mathcal{L}}$ and the projection is unique, we must have $\hat{\xi}_n \to \hat{\xi}$ in mean square. Therefore

$$\hat{\xi} = \lim_{n \to \infty} \sum_{i=1}^{n} (\xi, \eta_i) \eta_i.$$

The orthogonality $\xi - \hat{\xi} \perp \zeta$ for all $\zeta \in \overline{\mathcal{L}}$ follows from the minimal distance property.
