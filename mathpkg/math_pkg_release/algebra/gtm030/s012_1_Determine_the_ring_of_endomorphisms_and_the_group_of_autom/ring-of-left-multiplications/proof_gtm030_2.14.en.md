---
role: proof
locale: en
of_concept: ring-of-left-multiplications
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

From the anti-homomorphism $a \mapsto a_l$, the image set $\mathfrak{A}_l = \{a_l : a \in \mathfrak{A}\}$ is the homomorphic image of $\mathfrak{A}$ in $\mathfrak{E}$ (albeit via an anti-homomorphism). Since the relations $(a + b)_l = a_l + b_l$ and $(ab)_l = b_l a_l$ hold, the set $\mathfrak{A}_l$ is closed under the addition and multiplication in $\mathfrak{E}$, hence is a subring of $\mathfrak{E}$.

The kernel of the anti-homomorphism $a \mapsto a_l$ consists of those $a \in \mathfrak{A}$ such that $a_l = 0$, i.e., $x a_l = ax = 0$ for all $x \in \mathfrak{A}$. This is precisely the set $\mathfrak{Z}_l$ of left annihilators of $\mathfrak{A}$. If $\mathfrak{A}$ has an identity element $1$, then $a_l = 0$ implies $1 \cdot a = a = 0$, so $\mathfrak{Z}_l = 0$. In this case the anti-homomorphism is injective, hence an anti-isomorphism onto $\mathfrak{A}_l$.
