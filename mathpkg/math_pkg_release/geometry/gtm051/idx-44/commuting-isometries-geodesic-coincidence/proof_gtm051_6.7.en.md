---
role: proof
locale: en
of_concept: commuting-isometries-geodesic-coincidence
source_book: gtm051
source_chapter: "6"
source_section: "6.7"
---

**Proof.** Suppose $\gamma$ and $\gamma'$ are nontrivial commuting elements in $\Gamma$, with $K < 0$. Let $\tilde{c}(t)$, $t \in \mathbb{R}$, and $\tilde{c}'(t)$, $t \in \mathbb{R}$, be the corresponding invariant geodesics in $\tilde{M}$. By Theorem 6.7.1(iii), they are unique up to choice of initial points.

Consider the geodesic $\gamma' \circ \tilde{c}$. Since $\gamma$ and $\gamma'$ commute,

$$\gamma(\gamma' \tilde{c}(t)) = \gamma'(\gamma \tilde{c}(t)) = \gamma' \tilde{c}(t + \omega).$$

Thus $\gamma' \circ \tilde{c}$ is also a $\gamma$-invariant geodesic in $\tilde{M}$ (with the same period $\omega$). By the uniqueness result of Theorem 6.7.1(iii), $\gamma' \circ \tilde{c}$ must coincide with $\tilde{c}$ up to a parameter translation:

$$\gamma' \tilde{c}(t) = \tilde{c}(t + \tau)$$

for some $\tau \in \mathbb{R}$. But this means that $\tilde{c}$ is also $\gamma'$-invariant (with period $\tau$). Again by uniqueness of the $\gamma'$-invariant geodesic (Theorem 6.7.1(iii) applied to $\gamma'$), the geodesics $\tilde{c}$ and $\tilde{c}'$ must coincide up to parameter translation:

$$\tilde{c}'(t) = \tilde{c}(t + t_0)$$

for some $t_0 \in \mathbb{R}$.
