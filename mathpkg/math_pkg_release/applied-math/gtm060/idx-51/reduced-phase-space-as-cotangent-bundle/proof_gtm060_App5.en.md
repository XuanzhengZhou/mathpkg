---
role: proof
locale: en
of_concept: reduced-phase-space-as-cotangent-bundle
source_book: gtm060
source_chapter: "Appendix 5"
source_section: "Dynamical systems with symmetries"
---
Let $\pi: V \to W$ be the factorization map, and let $\omega \in T^*W$ be a 1-form on $W$ at the point $w = \pi(v)$. The pullback $\pi^*\omega$ on $V$ at the point $v$ belongs to $M_0$ (the zero momentum level set) because it annihilates vectors tangent to group orbits. It therefore projects to a point in the quotient $F_0 = M_0/G$.

Conversely, the elements of $F_0$ are invariant 1-forms on $V$ which vanish on the orbits; such forms define 1-forms on $W$ by descent. We have thus constructed a mapping $T^*W \to F_0$, and it is easy to verify that this mapping is a symplectic diffeomorphism with respect to the natural symplectic structures on both sides.

The case $p \neq 0$ is reduced to the case $p = 0$ as follows. Consider a $G$-invariant riemannian metric on $V$. The intersection of $M_p$ with the cotangent plane to $V$ at the point $v$ is a hyperplane. The quadratic form defined by the metric has a unique minimum point $S(v)$ in this hyperplane. Subtraction of the vector $S(v)$ carries the hyperplane $M_p \cap T^*V_v$ into $M_0 \cap T^*V_v$, giving a (possibly non-symplectic) diffeomorphism $F_p \to F_0$. The difference between the symplectic structures on $T^*W$ induced by $F_p$ and $F_0$ is a 2-form induced by a 2-form on $W$.
