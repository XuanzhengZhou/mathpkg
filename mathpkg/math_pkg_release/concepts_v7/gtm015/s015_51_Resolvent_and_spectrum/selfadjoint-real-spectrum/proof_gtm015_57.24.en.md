---
role: proof
locale: en
of_concept: selfadjoint-real-spectrum
source_book: gtm015
source_chapter: "57"
source_section: "57.24"
---

# Proof of Self-adjoint operators have real spectrum

(57.24) Lemma. If $H$ is a Hilbert space and $T \in \mathcal{L}(H)$ is self-adjoint, then $\sigma(T) \subset \mathbb{R}$.

Proof. Assuming $\mu \in \mathbb{C}$ has Cartesian form $\mu = \alpha + i\beta$ with $\beta \neq 0$, it is to be shown that $T - \mu I$ is invertible. Since
$$T - \mu I = (T - \alpha I) - i\beta I = -\beta[-\beta^{-1}(T - \alpha I) + iI]$$
where $-\beta^{-1}(T - \alpha I)$ is also self-adjoint, it clearly suffices (after a change of notation) to show that $T + iI$ is invertible. Indeed,
$$(T + iI)^*(T + iI) = (T + iI)(T + iI)^* = T^2 + I$$
is invertible by (57.23).
