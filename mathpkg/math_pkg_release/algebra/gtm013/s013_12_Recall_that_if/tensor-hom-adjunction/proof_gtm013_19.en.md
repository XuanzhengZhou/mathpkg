---
role: proof
locale: en
of_concept: tensor-hom-adjunction
source_book: gtm013
source_chapter: "5"
source_section: "19"
---

Define the map $\phi: \operatorname{Hom}_S(U \otimes_R M, N) \to \operatorname{Hom}_R(M, \operatorname{Hom}_S(U, N))$ as follows. Given an $S$-homomorphism $\alpha: U \otimes_R M \to N$, define $\phi(\alpha): M \to \operatorname{Hom}_S(U, N)$ by $[\phi(\alpha)(m)](u) = \alpha(u \otimes m)$ for all $m \in M$, $u \in U$.

To see that $\phi(\alpha)(m)$ is an $S$-homomorphism: for $s \in S$, $[\phi(\alpha)(m)](su) = \alpha(su \otimes m) = s \alpha(u \otimes m) = s [\phi(\alpha)(m)](u)$, using the left $S$-module structure on $U \otimes_R M$.

To see that $\phi(\alpha)$ is an $R$-homomorphism: for $r \in R$, $[\phi(\alpha)(rm)](u) = \alpha(u \otimes rm)$. Since $U$ is a right $R$-module, $u \otimes rm = ur \otimes m$, and thus $\phi(\alpha)(rm) = r \cdot \phi(\alpha)(m)$.

Conversely, define $\psi: \operatorname{Hom}_R(M, \operatorname{Hom}_S(U, N)) \to \operatorname{Hom}_S(U \otimes_R M, N)$ by $\psi(\beta)(u \otimes m) = [\beta(m)](u)$, extended linearly. This is well-defined because the map $(u, m) \mapsto [\beta(m)](u)$ is $R$-balanced: $[\beta(m)](ur) = [r \cdot \beta(m)](u) = [\beta(rm)](u)$.

One checks that $\phi$ and $\psi$ are mutually inverse $\mathbb{Z}$-isomorphisms. The naturality (commutative diagram) follows from the definitions: for $f: M'' \to M$, the diagram commutes because both paths compute the same composition.
