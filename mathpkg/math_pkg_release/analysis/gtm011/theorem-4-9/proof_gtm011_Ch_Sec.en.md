---
role: proof
locale: en
of_concept: theorem-4-9
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $S$ be the component

is harmonic in the right half plane and $0 < h_k(z) < \pi$ for $\text{Re } z > 0$ (see Exercise III.3.19). Moreover

4.11 $h_k(x + iy) = \int_{\alpha_k}^{\beta_k} \frac{x}{x^2 + (y - t)^2} \, dt$

if $x > 0$. From (4.11) it follows that

$$\sum_{k=1}^{n} h_k(x + iy) \leq \int_{-\infty}^{\infty} \frac{x}{x^2 + (y - t)^2} \, dt = \pi.$$

Since each $h_k \geq 0$, Harnack's Theorem gives that $h = \sum_{k=1}^{\infty} h_k$ is harmonic in the right half plane. Hence

$$\psi_r(z) = \frac{1}{\pi} h\left(-\ell_r(z)\right)$$

is harmonic in $G(0; r)$. It will be shown that $\{\psi_r\}$ is a barrier at 0.

Fix $r > 0$; then $\lim_{\text{Re } [-\ell_r(z)] = +\infty}$. So it suffices to show that $h(z) \to 0$ as $\text{Re } z \to +\infty$. Using (4.11) and (4.10) it follows that for $x > 0$,

$$h(x + iy) = \sum_{k=1}^{\infty} h_k(x + iy)$$

$$= \sum_{k=1}^{\infty} \int_{\alpha_k}^{\beta_k} \frac{1/x}{1 + (y - t)^2/x^2} \, dt$$

$$\leq \frac{1}{x} \sum_{k=1}^{\infty} \left(\beta_k - \alpha_k\right)$$

$$\leq \frac{2\pi}{x}.$$

So, indeed, $\lim_{x \to +\infty} h(x + iy) = 0$ uniformly in $y$; this gives that $\lim_{\text{Re } z \to 0} \psi_r(z) = 0$.

To prove

then $x > 0$ and $\alpha_k < y < \beta_k$ implies $0 \leq h(x+iy) - h_k(x+iy) \leq u(x+iy) + v(x+iy)$.

Once 4.13 is established, Equation 4.12 is proved as follows. From Exercise III.3.19,

$$v(x+iy) = \arctan \left( \frac{y-\beta_k}{x} \right) - \arctan \left( \frac{y-\beta_k}{x} \right).$$

so if $x+iy \rightarrow ic$, $c < \beta_k < \beta$, then $v(x+iy) \rightarrow 0$.

Similarly $u(x+iy) \rightarrow 0$ as $x+iy \rightarrow ic$, with $\alpha < \alpha_k < c$.

Hence, Claim 4.13 yields

4.14 $$\lim [h(z) - h_k(z)] = 0.$$

But

$$h_k(x+iy) = \arctan \left( \frac{y-\alpha_k}{x} \right) - \arctan \left( \frac{y-\beta_k}{x} \right),$$

so $\lim h_k(z) = \pi$; this combined with (4.14) implies Equation (4.12).

It remains to substantiate Claim 4.13; we argue geometrically. Recall (Exercise III.3.19) that $h_j(z)$ is the angle in the figure. Consider all the intervals $(i\alpha_j, i\beta_j)$ lying above $(i\alpha_k, i\beta_k)$ and translate them downward along the imaginary axis, keeping them above $(i\alpha_k, i\beta_k)$ until their endpoints coincide and such that one of the endpoints coincides with $i\beta_k$. Since $\sum (\beta_j - \alpha_j) \leq 2\pi$ there is a number $\beta < (\beta_k + 2\pi)$ such that each of the translated intervals lies in $(i\beta_k, i\beta)$. Now if $z = x+iy$, $x > 0$ and $\alpha_k < y

then the angle $h_j(z)$ increases as the interval $(i\alpha_j, i\beta_j)$ is translated downward. Hence $\alpha_k < \text{Im } z < \beta_k$ implies

4.15 $$\sum_j h_j(z) \leq v(z),$$

where $v$ is as in the statement of the claim and the sum is over all $j$ such that $\alpha_j \geq \beta_k$. By performing a similar upward translation of the intervals $(i\alpha_j, i\beta_j)$ with $\beta_j \leq \alpha_k$, there is a number $\alpha < (\alpha_k - 2\pi)$ such that the translates lie in the interval $(i\alpha, i\alpha_k)$. So if $u$ is as in the claim and $\alpha_k < \text{Im } z < \beta_k$,

4.16 $$\sum_j h_j(z) \leq u(z)$$

where the sum is over all $j$ with $\beta_j \leq \alpha_k$. By combining (4.15) and (4.16) the claim is established.
