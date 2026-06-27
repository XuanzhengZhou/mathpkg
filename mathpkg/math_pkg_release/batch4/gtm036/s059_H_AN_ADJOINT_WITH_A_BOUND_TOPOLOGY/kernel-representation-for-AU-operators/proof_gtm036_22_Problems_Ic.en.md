---
role: proof
locale: en
of_concept: kernel-representation-for-AU-operators
source_book: gtm036
source_chapter: "22"
source_section: "Problems I(c)"
---
For the forward direction, let $T$ be a continuous linear mapping of $A(U)$ into itself. For each $z \in U$, define $v_z(\zeta) = (\zeta - z)^{-1}$, which is an element of $A(U)$ (as a function of $z$) for each fixed $\zeta$ with $|\zeta| \geq 1$. Let $T^*$ denote the adjoint of $T$, and set $u_z = T^*(v_z)$. Then define the kernel by $B(\zeta, z) = u_z(\zeta)$. One verifies that $B$ satisfies conditions (i)--(iii) using the continuity and linearity of $T^*$ together with properties of the Cauchy kernel $v_z$.

For the converse direction, given a kernel $B$ satisfying (i)--(iii), define $T$ by the integral formula. The main difficulty is proving that $T(f)$ is analytic in $U$ for each $f \in A(U)$. This is established using condition (ii) and Hartogs' lemma on separate analyticity: condition (ii) provides analyticity in $\zeta$, condition (iii) gives analyticity in $z$, and the joint continuity condition (i) allows one to apply Hartogs' theorem to conclude that $B(\zeta, z)$ is jointly analytic, from which the analyticity of $T(f)$ follows. The continuity of $T$ on $A(U)$ is then verified using the integral representation and standard estimates. Uniqueness follows from the uniqueness of the Cauchy integral representation.
