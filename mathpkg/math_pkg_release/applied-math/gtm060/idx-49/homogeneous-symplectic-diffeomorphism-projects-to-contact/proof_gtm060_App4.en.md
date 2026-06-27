---
role: proof
locale: en
of_concept: homogeneous-symplectic-diffeomorphism-projects-to-contact
source_book: gtm060
source_chapter: "Appendix 4"
source_section: "Contact Structures"
---
Every diffeomorphism which commutes with the action of the multiplicative group projects onto some diffeomorphism of the contact manifold. To show that this is a contact diffeomorphism it is sufficient to prove the second assertion of the theorem (since only those vectors for which $$\alpha(\xi) = 0$$ project onto the contact plane).

To prove the second assertion we express the integral of the 1-form $$\alpha$$ along any path $$\gamma$$ in terms of the symplectic structure $$d\alpha$$:

$$\int_{\gamma} \alpha = \lim_{\varepsilon \to 0} \iint_{\sigma(\varepsilon)} d\alpha,$$

where the 2-chain $$\sigma(\varepsilon)$$ is obtained from $$\gamma$$ by multiplication by all numbers in the interval $$[\varepsilon, 1]$$. The boundary of $$\sigma$$ contains, besides $$\gamma$$, two vertical intervals and the path $$\varepsilon\gamma$$. The integrals of $$\alpha$$ over the vertical intervals are equal to zero, and the integral over $$\varepsilon\gamma$$ approaches 0 as $$\varepsilon$$ does.

Now from the invariance of the 2-form $$d\alpha$$ and the commutativity of our diffeomorphism $$F$$ with multiplication by numbers it follows that for any path $$\gamma$$

$$\int_{F\gamma} \alpha = \int_{\gamma} \alpha,$$

and thus the diffeomorphism $$F$$ preserves the 1-form $$\alpha$$.
