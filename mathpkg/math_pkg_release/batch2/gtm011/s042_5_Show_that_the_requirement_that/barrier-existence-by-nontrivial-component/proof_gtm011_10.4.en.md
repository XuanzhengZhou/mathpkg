---
role: proof
locale: en
of_concept: barrier-existence-by-nontrivial-component
source_book: gtm011
source_chapter: "X"
source_section: "4"
---

*Proof.* Let $S$ be the component of $\mathbb{C}_\infty - G$ which contains $a$. By hypothesis $S$ is not a single point. By Lemma 4.8 we may assume that $\mathbb{C}_\infty - G$ is a closed connected set $S$ with $\infty \in S$ and $S \cap \partial_\infty G = \{a\}$. Further, we may assume $a = 0$ by a suitable translation.

Let $S$ be written as the complement of a union of disjoint open intervals on the imaginary axis. That is, by the Riemann Mapping Theorem, there is a conformal equivalence $\ell$ of $G$ onto the right half plane $H = \{z : \text{Re } z > 0\}$ with the property that $\ell(z) \to \infty$ as $z \to 0$. Moreover, $\ell$ maps $\partial G - \{0\}$ onto the imaginary axis. Let $(i\alpha_k, i\beta_k)$ be the complementary intervals of the image of $\partial G - \{0\}$ on the imaginary axis, so that $\sum_{k=1}^{\infty} (\beta_k - \alpha_k) \leq 2\pi$.

For each $k \geq 1$, define $h_k(z)$ to be the harmonic measure of the interval $(i\alpha_k, i\beta_k)$ in the right half plane. Each $h_k$ is harmonic in the right half plane and $0 < h_k(z) < \pi$ for $\text{Re } z > 0$ (see Exercise III.3.19). Moreover,

$$h_k(x + iy) = \int_{\alpha_k}^{\beta_k} \frac{x}{x^2 + (y - t)^2} \, dt$$

for $x > 0$. From this representation it follows that

$$\sum_{k=1}^{n} h_k(x + iy) \leq \int_{-\infty}^{\infty} \frac{x}{x^2 + (y - t)^2} \, dt = \pi.$$

Since each $h_k \geq 0$, Harnack's Theorem gives that $h = \sum_{k=1}^{\infty} h_k$ is harmonic in the right half plane. For each $r > 0$, define

$$\psi_r(z) = \frac{1}{\pi} h\left(-\ell_r(z)\right)$$

where $\ell_r(z) = \ell(z)$ for an appropriate rescaling to $G(0; r)$. Then $\psi_r$ is harmonic in $G(0; r)$.

It remains to verify the barrier properties. To show $\lim_{z \to 0} \psi_r(z) = 0$, note that $\text{Re}[-\ell_r(z)] \to +\infty$ as $z \to 0$. Using the integral representation, for $x > 0$:

$$h(x + iy) = \sum_{k=1}^{\infty} h_k(x + iy) = \sum_{k=1}^{\infty} \int_{\alpha_k}^{\beta_k} \frac{1/x}{1 + (y - t)^2/x^2} \, dt \leq \frac{1}{x} \sum_{k=1}^{\infty} (\beta_k - \alpha_k) \leq \frac{2\pi}{x}.$$

Hence $\lim_{x \to +\infty} h(x + iy) = 0$ uniformly in $y$, giving $\lim_{z \to 0} \psi_r(z) = 0$.

To prove $\lim_{z \to w} \psi_r(z) = 1$ for $w \in G \cap \partial B(0; r)$, we proceed as follows. For a fixed $k$, split $h$ as $h = h_k + \sum_{j \neq k} h_j$. A geometric argument (translating the complementary intervals along the imaginary axis) shows that:

**Claim.** If $z = x + iy$ with $x > 0$ and $\alpha_k < y < \beta_k$, then

$$\sum_{j:\, \alpha_j \geq \beta_k} h_j(z) \leq v(z), \qquad \sum_{j:\, \beta_j \leq \alpha_k} h_j(z) \leq u(z)$$

where $u$ and $v$ are harmonic functions in the right half plane such that $u(z) \to 0$ as $z \to ic$ for $c > \beta_k$ and $v(z) \to 0$ as $z \to ic$ for $c < \alpha_k$.

From the Claim it follows that $\lim [h(z) - h_k(z)] = 0$ as $z \to ic$ with $\alpha_k < c < \beta_k$ (i.e., as $z$ approaches the interval $(i\alpha_k, i\beta_k)$). But

$$h_k(x + iy) = \arctan\left(\frac{y - \alpha_k}{x}\right) - \arctan\left(\frac{y - \beta_k}{x}\right),$$

so $\lim h_k(z) = \pi$ as $z \to ic$ with $\alpha_k < c < \beta_k$. Combining these facts gives $\lim h(z) = \pi$ as $z$ approaches any point of the imaginary axis that lies in a complementary interval. Hence, by composition with $-\ell_r$, $\lim_{z \to w} \psi_r(z) = 1$ for $w \in G \cap \partial B(0; r)$.

Thus $\{\psi_r : r > 0\}$ is a barrier for $G$ at $0$. $\square$
