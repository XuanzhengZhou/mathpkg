---
role: proof
locale: en
of_concept: darboux-contact-local-equivalence
source_book: gtm060
source_chapter: "Appendix 4"
source_section: "Contact Structures"
---
It is clear that the first two formulations of Darboux's theorem follow from the third (the normal form). We deduce the third from the symplectic Darboux theorem (cf. Section 43).

We symplectify our contact manifold. Consider a point in the surface just constructed (in the symplectic manifold) lying over the point of the contact manifold we are interested in. In the symplectic manifold we can choose a local system of coordinates near this point such that

$$d\alpha = dp_0 \wedge dq_0 + \cdots + dp_n \wedge dq_n$$

and such that the coordinate surface $$p_0 = 0$$ coincides with our $$(2n + 1)$$-dimensional manifold (cf. Section 43, where in the proof of the symplectic Darboux theorem the first coordinate may be chosen arbitrarily).

We note now that the 1-form $$p_0 dq_0 + \cdots + p_n dq_n$$ has derivative $$d\alpha$$. Thus, locally,

$$\alpha = p_0 dq_0 + \cdots + p_n dq_n + dw,$$

where $$w$$ is a function which can be taken to be zero at the origin. In particular, on the surface $$p_0 = 0$$ the form $$\alpha$$ takes the form

$$\alpha|_{p_0=0} = p_1 dq_1 + \cdots + p_n dq_n + dw.$$

The projection $$\pi$$ allows us to carry the coordinates $$p_1, \ldots, p_n; q_0; q_1, \ldots, q_n$$ and the function $$w$$ onto the contact manifold. Defining $$x, y, z$$ by $$x_i = p_i$$, $$y_i = q_i$$, $$z = w$$, we obtain $$\omega = x\,dy + dz,$$ and it remains only to verify that $$(x_1, \ldots, x_n; y_1, \ldots, y_n; z)$$ form a coordinate system. For this it suffices to verify that the partial derivative of $$w$$ with respect to $$q_0$$ is not zero, i.e., that the 1-form $$\alpha$$ is not zero on a vector of the coordinate direction $$\partial/\partial q_0$$.
