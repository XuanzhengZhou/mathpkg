---
role: proof
locale: en
of_concept: epimorphism-preserves-csa
source_book: gtm009
source_chapter: "15"
source_section: "15.4"
---

Obviously $\phi(H)$ is nilpotent, being the homomorphic image of a nilpotent algebra. Let $A = \operatorname{Ker} \phi$, and identify $L'$ with $L/A$.

If $x + A$ normalizes $H + A$ in $L'$, then $[x, H + A] \subset H + A$, which means $x \in N_L(H + A)$. But $H + A$ includes a CSA (since $H$ is a minimal Engel subalgebra by Theorem 15.3, and $H \subset H + A$, so $H + A$ contains a minimal Engel subalgebra which is a CSA). Therefore the subalgebra $H + A$ is self-normalizing by Lemma B of (15.2).

Hence $x \in H + A$, which means $x + A \in \phi(H)$. Thus $\phi(H)$ is self-normalizing in $L'$, and together with nilpotence this shows $\phi(H)$ is a CSA of $L'$.
