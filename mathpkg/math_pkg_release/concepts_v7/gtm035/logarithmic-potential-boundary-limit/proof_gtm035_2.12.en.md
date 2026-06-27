---
role: proof
locale: en
of_concept: logarithmic-potential-boundary-limit
source_book: gtm035
source_chapter: "Chapter 2"
source_section: "2.12"
---

# Proof of Logarithmic Potential Boundary Limit Lemma

**Lemma 2.12.** Let $E$ be a component of $\mathbb{C} \setminus X$ and let $z_0 \in \partial E$. Let $\alpha$ be a real measure on $E$ satisfying

$$\int_E \left|\log\left|\frac{1}{z_0 - \zeta}\right|\right| d|\alpha|(\zeta) < \infty.$$

Then

$$\lim_{t \to 0} \int \alpha^* \, d\sigma_t(z) = \alpha^*(z_0),$$

where $\alpha^*$ denotes the logarithmic potential of $\alpha$ and $\sigma_t$ is a suitably constructed probability measure.

*Proof.* We may assume without loss of generality that $z_0 = 0$. Fix $t > 0$. Since $0 \in \partial E$ and $\mathbb{C} \setminus E$ is connected, there exists a probability measure $\sigma_t$ carried on $\mathbb{C} \setminus E$ such that

$$\sigma_t\{z \mid r_1 < |z| < r_2\} = \frac{1}{t}(r_2 - r_1) \quad \text{for } 0 < r_1 < r_2 \leq t$$

and $\sigma_t = 0$ outside $|z| \leq t$.

(If some line segment with $0$ as one endpoint and length $t$ happens to lie in $\mathbb{C} \setminus E$, we may of course take $\sigma_t$ as $\frac{1}{t}$ times linear measure on that segment. In the general case, one constructs $\sigma_t$ by a suitable limiting argument.)

Then for all $\zeta \in \mathbb{C}$ we have

$$\int \log\left|\frac{1}{z - \zeta}\right| d\sigma_t(z) \leq \int \log\left|\frac{1}{|z| - |\zeta|}\right| d\sigma_t(z)$$

$$= \frac{1}{t} \int_0^t \log\frac{1}{|r - |\zeta||} \, dr$$

$$= \log\frac{1}{|\zeta|} + \frac{1}{t} \int_0^t \log\frac{1}{|1 - r/|\zeta||} \, dr.$$

The last term is bounded above by a constant $A$ independent of $t$ and $|\zeta|$. Indeed, the integral $\frac{1}{t} \int_0^t \log\frac{1}{|1 - r/|\zeta||} \, dr$ converges uniformly as the integrand has only an integrable logarithmic singularity at $r = |\zeta|$.

Hence we have

$$\int \log\left|\frac{1}{z - \zeta}\right| d\sigma_t(z) \to \log\frac{1}{|\zeta|}$$

as $t \to 0$, with the convergence being dominated. Consequently,

$$\lim_{t \to 0} \int \alpha^*(z) \, d\sigma_t(z) = \int \left(\lim_{t \to 0} \int \log\left|\frac{1}{z - \zeta}\right| d\sigma_t(z)\right) d\alpha(\zeta) = \int \log\frac{1}{|\zeta|} \, d\alpha(\zeta) = \alpha^*(0).$$

This completes the proof. $\square$
