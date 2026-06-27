---
role: proof
locale: en
of_concept: dgamma1-commutative-diagram
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Let $\eta$ be a vector field on $Y$ with compact support representing $[\eta]_q$, and let $\phi_t$ be the one-parameter group whose infinitesimal generator is $\eta$. By definition, $(d\gamma_1)(\eta) = (dc/dt)|_{t=0}$ where $c(t) = j^k \phi_t(q) \cdot \sigma$.

On the other hand, $\lambda \cdot f^* \cdot \pi_k^\infty(\eta) = \lambda(j^k(f^*\eta))$. A deformation of $f$ corresponding to $f^*\eta$ is given by $F_t = \phi_t \circ f$. Indeed,
$$\frac{d}{dt}F_t\big|_{t=0} = \frac{d}{dt}(\phi_t \circ f)\big|_{t=0} = \eta \circ f = f^*\eta.$$

Now compute:
$$\lambda \cdot f^* \cdot \pi_k^\infty(\eta) = \frac{d}{dt} j^k(\phi_t \circ f)(p)\big|_{t=0} = \frac{d}{dt} j^k \phi_t(q) \cdot \sigma\big|_{t=0} = (d\gamma_1)(\eta).$$

The middle equality holds because $j^k(\phi_t \circ f)(p) = j^k \phi_t(f(p)) \cdot j^k f(p) = j^k \phi_t(q) \cdot \sigma$ by the chain rule for jets.
