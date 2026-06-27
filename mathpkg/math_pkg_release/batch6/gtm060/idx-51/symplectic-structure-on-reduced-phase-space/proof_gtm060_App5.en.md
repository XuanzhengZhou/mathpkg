---
role: proof
locale: en
of_concept: symplectic-structure-on-reduced-phase-space
source_book: gtm060
source_chapter: "Appendix 5"
source_section: "Dynamical systems with symmetries"
---
We look at the following two spaces in the tangent space to $M$ at $x$:

$T(M_p)$, the tangent space to the level manifold $M_p$,
and $T(Gx)$, the tangent space to the orbit of the group $G$.

**Lemma.** These two spaces are skew-orthogonal complements to one another in $TM$.

*Proof of the Lemma.* A vector $\zeta$ lies in the skew-orthogonal complement to the tangent plane of an orbit of the group $G$ if and only if the skew-scalar product of $\zeta$ with velocity vectors of the hamiltonian flow of $G$ is equal to zero (by definition). But these skew-scalar products are equal to the derivatives of the corresponding hamiltonian functions in the direction $\zeta$. Therefore, the vector $\zeta$ lies in the skew-orthogonal complement to the orbit of $G$ if and only if the derivative of the momentum in the direction $\zeta$ is equal to zero, i.e., if $\zeta$ lies in $T(M_p)$.

Now, the representatives $\xi'$ and $\eta'$ are defined up to addition of a vector from the tangent plane to the orbit of the group $G_p$. But this tangent plane is the intersection of the tangent planes to the orbit $Gx$ and to the manifold $M_p$. Consequently, the addition to $\xi'$ of a vector from $T(G_p x)$ does not change the skew-scalar product with any vector $\eta'$ from $T(M_p)$ (since by the lemma $T(G_p x)$ is skew-orthogonal to $T(M_p)$). Thus we have shown independence from the representatives $\xi'$ and $\eta'$, establishing the symplectic structure on $F_p$.
