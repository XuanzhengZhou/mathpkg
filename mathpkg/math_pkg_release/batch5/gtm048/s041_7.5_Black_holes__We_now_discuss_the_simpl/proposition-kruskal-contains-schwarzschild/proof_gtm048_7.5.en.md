---
role: proof
locale: en
of_concept: proposition-kruskal-contains-schwarzschild
source_book: gtm048
source_chapter: "7"
source_section: "7.5.2"
---

**Proof.** Let $t = 2\mu[\ln u - \ln(-v)]|_{M_I}$. Then $t$ is $C^\infty$ and maps $M_I$ onto $(-\infty, \infty)$. Let $\psi: M_I \to (-\infty, \infty) \times (2\mu, \infty) \times \mathcal{S}^2$ be given by $\psi n = (tn, rn, Pn)$ for every $n \in M_I$. $\psi$ is onto and there is a $C^\infty$ inverse determined by $u = (r - 2\mu)\exp[(r - 2\mu + t)/4\mu]$, $v = (r - 2\mu)\exp[(r - 2\mu - t)/4\mu]$.

Thus $\psi$ is a diffeomorphism. Moreover, $dt = 2\mu(dv/v - du/u)$ and $dr = 2\mu(1 - 2\mu/r)(dv/v + du/u)$ on $M_I$, so that
$$-(1 - 2\mu/r)dt \otimes dt + (1 - 2\mu/r)^{-1}dr \otimes dr = 4\mu^2(1 - 2\mu/r)(dv \otimes dv + dv \otimes du),$$
which matches the Kruskal metric restricted to $M_I$, establishing the isometry.
