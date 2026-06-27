---
role: proof
locale: en
of_concept: symplectification-yields-symplectic-structure
source_book: gtm060
source_chapter: "Appendix 4"
source_section: "E. Symplectification of a contact manifold"
---

Since the assertion is local, it suffices to prove it in a small neighborhood. Fix a differential $1$-form $\omega$ on the contact manifold giving the field of contact planes. Over this neighborhood, represent the symplectified space as the direct product of the neighborhood and $\mathbb{R}^\times$, associating to $(x, \lambda)$ the contact form $\lambda \omega_x$. Then the canonical $1$-form is

$$\alpha = \lambda \pi^* \omega,$$

and its exterior derivative is

$$d\alpha = d\lambda \wedge \pi^* \omega + \lambda \pi^* d\omega.$$

To show nondegeneracy, take an arbitrary tangent vector $\xi$. If $\xi$ is not a contact vector (i.e., $\omega(\pi_*\xi) \neq 0$), choose a nonzero vertical vector $\eta$ (so $\pi_*\eta = 0$). Then

$$d\alpha(\xi, \eta) = -d\lambda(\eta) \omega(\pi_*\xi) \neq 0,$$

since $\eta$ is a nonzero vertical vector (meaning $d\lambda(\eta) \neq 0$) and $\omega(\pi_*\xi) \neq 0$.

If $\xi$ is a contact vector (i.e., $\omega(\pi_*\xi) = 0$), then the first term $d\lambda \wedge \pi^*\omega$ vanishes. By the nondegeneracy of the contact structure, there exists a horizontal contact vector $\eta$ such that $d\omega(\pi_*\xi, \pi_*\eta) \neq 0$. Then

$$d\alpha(\xi, \eta) = \lambda \, d\omega(\pi_*\xi, \pi_*\eta) \neq 0,$$

since $\lambda \neq 0$. This proves $d\alpha$ is nondegenerate in all cases.
