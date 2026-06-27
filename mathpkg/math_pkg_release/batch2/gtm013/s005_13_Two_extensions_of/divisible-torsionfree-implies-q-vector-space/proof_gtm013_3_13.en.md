---
role: proof
locale: en
of_concept: divisible-torsionfree-implies-q-vector-space
source_book: gtm013
source_chapter: "3"
source_section: "13"
---
*Proof.* This is Exercise 15(2) in the source text. For each $r/s \in Q$ (with $r, s \in R$, $s \neq 0$), define $\theta(r/s): M \to M$ as follows. Since $M$ is torsion-free, multiplication by $s$ is injective; since $M$ is divisible, multiplication by $s$ is also surjective, hence a bijection. Define $s^{-1} \in \operatorname{End}_{\mathbb{Z}}(M)$ as the inverse of the map $x \mapsto sx$. Then set $\theta(r/s)(x) = r(s^{-1}(x))$. This is well-defined because if $r/s = r'/s'$, then $rs' = r's$, and the definitions agree using the commutativity of $R$ and the $R$-module axioms. The map $\theta$ is a ring homomorphism uniquely determined by extending $\lambda$.
