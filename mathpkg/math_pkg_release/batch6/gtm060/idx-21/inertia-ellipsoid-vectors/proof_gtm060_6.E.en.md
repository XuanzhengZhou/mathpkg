---
role: proof
locale: en
of_concept: inertia-ellipsoid-vectors
source_book: gtm060
source_chapter: "6"
source_section: "E"
---

Set $\Omega = \mathbf{e}/\sqrt{I_e}$. Then by the kinetic energy formula for rotation about the $\mathbf{e}$ axis:

$$T = \frac{1}{2} I_e \Omega^2 = \frac{1}{2} I_e \cdot \frac{1}{I_e} = \frac{1}{2}.$$

On the other hand, from the quadratic form representation $T = \frac{1}{2}(A\Omega, \Omega)$. Therefore:

$$(A\Omega, \Omega) = 1.$$

Thus the set $\{\Omega = \mathbf{e}/\sqrt{I_e} : \mathbf{e} \in S^2\}$ is precisely the level set $\{\Omega \in K : (A\Omega, \Omega) = 1\}$ of the positive-definite symmetric quadratic form defined by the inertia operator $A$. By the spectral theorem, this level set is an ellipsoid.
