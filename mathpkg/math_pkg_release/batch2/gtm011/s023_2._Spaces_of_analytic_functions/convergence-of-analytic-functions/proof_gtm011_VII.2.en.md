---
role: proof
locale: en
of_concept: convergence-of-analytic-functions
source_book: gtm011
source_chapter: "VII"
source_section: "2"
---

Suppose $\{f_n\} \subset H(G)$ and $f_n \to f$ in $C(G, \mathbb{C})$, i.e., uniformly on each compact subset of $G$. To show $f$ is analytic, it suffices to prove $f$ is analytic on each open disk whose closure lies in $G$.

Fix $a \in G$ and choose $R > 0$ such that $\overline{B}(a; R) \subset G$. For any $z \in B(a; R)$, Cauchy's Integral Formula gives

$$f_n(z) = \frac{1}{2\pi i} \int_{|\zeta - a| = R} \frac{f_n(\zeta)}{\zeta - z} \, d\zeta.$$

Since $f_n \to f$ uniformly on the compact set $\{\zeta : |\zeta - a| = R\}$, we may pass the limit inside the integral:

$$f(z) = \lim_{n \to \infty} f_n(z) = \lim_{n \to \infty} \frac{1}{2\pi i} \int_{|\zeta - a| = R} \frac{f_n(\zeta)}{\zeta - z} \, d\zeta = \frac{1}{2\pi i} \int_{|\zeta - a| = R} \frac{f(\zeta)}{\zeta - z} \, d\zeta.$$

The right-hand side is analytic in $z$ on $B(a; R)$ (it is a Cauchy-type integral). Hence $f$ is analytic on $B(a; R)$, and since $a$ was arbitrary, $f \in H(G)$.

For the derivatives, differentiate under the integral sign:

$$f_n^{(k)}(z) = \frac{k!}{2\pi i} \int_{|\zeta - a| = R} \frac{f_n(\zeta)}{(\zeta - z)^{k+1}} \, d\zeta.$$

Now

$$|f_n^{(k)}(z) - f^{(k)}(z)| = \left| \frac{k!}{2\pi i} \int_{|\zeta - a| = R} \frac{f_n(\zeta) - f(\zeta)}{(\zeta - z)^{k+1}} \, d\zeta \right|.$$

For $z$ in any smaller disk $\overline{B}(a; r)$ with $0 < r < R$, we have $|\zeta - z| \geq R - r > 0$ for $|\zeta - a| = R$. Hence

$$\sup_{|z-a| \leq r} |f_n^{(k)}(z) - f^{(k)}(z)| \leq \frac{k!}{2\pi} \cdot \frac{2\pi R}{(R-r)^{k+1}} \cdot \sup_{|\zeta - a| = R} |f_n(\zeta) - f(\zeta)| \to 0$$

as $n \to \infty$. Thus $f_n^{(k)} \to f^{(k)}$ uniformly on compact subsets of $G$.
