---
role: proof
locale: en
of_concept: injective-omega-homomorphism
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of (4.24).** Let $f: (X, \delta) \longrightarrow (Y, \gamma)$ be an injective $\Omega$-homomorphism. The image $Xf = \{xf : x \in X\}$ is a subset of $Y$.

First, we show $Xf$ is an $\Omega$-subalgebra of $(Y, \gamma)$. For any $\omega \in \Omega_n$ and $x_1f, \ldots, x_nf \in Xf$, we have:

$$(x_1f, \ldots, x_nf) \gamma_\omega = (x_1, \ldots, x_n) \delta_\omega f \in Xf$$

since $f$ is an $\Omega$-homomorphism and $(x_1, \ldots, x_n) \delta_\omega \in X$. Thus $Xf$ is closed under all $\Omega$-operations, making it a subalgebra.

Now define $g: X \longrightarrow Xf$ by $xg = xf$. Since $f$ is injective, $g$ is a bijection onto its image. Moreover, $g$ inherits the $\Omega$-homomorphism property from $f$: for any $\omega$,

$$(x_1, \ldots, x_n) \delta_\omega g = (x_1, \ldots, x_n) \delta_\omega f = (x_1f, \ldots, x_nf) \gamma_\omega = (x_1g, \ldots, x_ng) \gamma_\omega$$

Since $g$ is a bijective $\Omega$-homomorphism, its inverse is also an $\Omega$-homomorphism, so $g$ is an isomorphism. (For a hint on verifying the inverse property, see 4.32.) $\square$
