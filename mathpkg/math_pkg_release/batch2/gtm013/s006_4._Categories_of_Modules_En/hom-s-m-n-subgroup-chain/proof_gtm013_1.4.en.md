---
role: proof
locale: en
of_concept: hom-s-m-n-subgroup-chain
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

Let $\phi: R \to S$ be a ring homomorphism and let $M, N$ be left $S$-modules. Define an $R$-module structure on $M$ by $r \cdot x = \phi(r)x$ for $r \in R, x \in M$, and similarly for $N$. Let $f \in \operatorname{Hom}_S(M, N)$. For $r \in R$ and $x \in M$,

$$f(rx) = f(\phi(r)x) = \phi(r)f(x) = rf(x).$$

Thus $f$ is an $R$-homomorphism, so $\operatorname{Hom}_S(M, N) \subseteq \operatorname{Hom}_R(M, N)$. Clearly the $R$-action factors through $\phi(R)$, so $\operatorname{Hom}_R(M, N) = \operatorname{Hom}_{\phi(R)}(M, N)$. Finally, every $R$-module homomorphism is in particular a homomorphism of the underlying abelian groups, i.e., a $\mathbb{Z}$-module homomorphism, giving $\operatorname{Hom}_R(M, N) \leq \operatorname{Hom}_{\mathbb{Z}}(M, N)$. All are subgroups by (4.1).
