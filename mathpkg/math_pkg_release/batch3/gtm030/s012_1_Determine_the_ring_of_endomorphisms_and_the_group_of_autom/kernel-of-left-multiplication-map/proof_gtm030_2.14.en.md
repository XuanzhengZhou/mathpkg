---
role: proof
locale: en
of_concept: kernel-of-left-multiplication-map
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

The kernel of the anti-homomorphism $a \mapsto a_l$ is

$$\ker(a \mapsto a_l) = \{ a \in \mathfrak{A} \mid a_l = 0 \} = \{ a \in \mathfrak{A} \mid x a_l = 0 \text{ for all } x \in \mathfrak{A} \}.$$

Since $x a_l = ax$, this equals $\{ a \in \mathfrak{A} \mid ax = 0 \text{ for all } x \in \mathfrak{A} \}$, which is precisely the set $\mathfrak{Z}_l$ of left annihilators of the ring $\mathfrak{A}$.

If $\mathfrak{A}$ has an identity element $1$, then for any $a \in \mathfrak{Z}_l$ we have $a \cdot 1 = a = 0$, so $\mathfrak{Z}_l = 0$. Thus the kernel is trivial and the anti-homomorphism $a \mapsto a_l$ is injective, hence an anti-isomorphism of $\mathfrak{A}$ onto $\mathfrak{A}_l$.
