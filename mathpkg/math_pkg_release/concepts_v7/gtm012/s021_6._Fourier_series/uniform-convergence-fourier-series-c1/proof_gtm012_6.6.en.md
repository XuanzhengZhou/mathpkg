---
role: proof
locale: en
of_concept: uniform-convergence-fourier-series-c1
source_book: gtm012
source_chapter: "6"
source_section: "§6. Fourier series"
---

# Proof of Uniform convergence of Fourier series for continuously differentiable periodic functions

**Proof.** Let $v = Du$ (the derivative of $u$). Integration by parts gives a relation between the Fourier coefficients of $v$ and those of $u$. Let $a_n = (u, e_n)$ and $b_n = (v, e_n)$. Then

$$b_n = (v, e_n) = \frac{1}{2\pi} \int_0^{2\pi} Du(x) \exp(-inx) \, dx$$

$$= \frac{1}{2\pi} \left[ u(x) \exp(-inx) \Big|_0^{2\pi} - \int_0^{2\pi} u(x) (-in) \exp(-inx) \, dx \right]$$

$$= \frac{in}{2\pi} \int_0^{2\pi} u(x) \exp(-inx) \, dx = in \, (u, e_n) = in a_n,$$

where the boundary terms vanish because $u$ is periodic: $u(0) = u(2\pi)$ and $\exp(-in \cdot 0) = \exp(-in \cdot 2\pi) = 1$.

Thus $|b_n| = |n| |a_n|$ for $n \neq 0$. Now we apply the Cauchy–Schwarz inequality for sequences to show $\sum |a_n| < \infty$:

$$\sum_{n=-\infty}^{\infty} |a_n| = |a_0| + \sum_{n \neq 0} |a_n| = |a_0| + \sum_{n \neq 0} \frac{|b_n|}{|n|}$$

$$\leq |a_0| + \left( \sum_{n \neq 0} \frac{1}{n^2} \right)^{1/2} \left( \sum_{n \neq 0} |b_n|^2 \right)^{1/2}$$

$$= |a_0| + \left( 2 \sum_{n=1}^{\infty} \frac{1}{n^2} \right)^{1/2} \|Du\| < \infty.$$

The finiteness follows from $\|Du\|^2 = \sum |b_n|^2 < \infty$ (by Bessel's inequality or Parseval's identity, since $Du \in \mathcal{C} \subset L^2$) and the convergence of $\sum n^{-2} = \pi^2/6$.

By Lemma 6.3, the absolute summability $\sum |a_n| < \infty$ implies that the partial sums of the Fourier series of $u$ converge uniformly to $u$:

$$u(x) = \sum_{n=-\infty}^{\infty} (u, e_n) \exp(inx), \quad \text{for all } x \in \mathbb{R}.$$

Now suppose $u \in \mathcal{P}$ (the space of periodic distributions), and let

$$u_N = \sum_{n=-N}^{N} a_n e_n.$$

Then relation $b_n = in a_n$ shows that

$$Du_N = \sum_{n=-N}^{N} in a_n e_n = \sum_{n=-N}^{N} b_n e_n.$$

The right-hand side is precisely the $N$-th symmetric partial sum of the Fourier series of $Du$. Since $Du \in \mathcal{P} \subset L^2$ (a periodic distribution whose derivative is in $L^2$), the partial sums converge to $Du$ in the sense of $L^2$. Because differentiation is continuous from $\mathcal{P}$ to $\mathcal{P}$, and $u_N \to u$ in $L^2$ hence in $\mathcal{P}$, we conclude that the partial sums $u_N$ converge to $u$ in the sense of $\mathcal{P}$. $\square$
