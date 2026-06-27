---
role: proof
locale: en
of_concept: biendomorphism-bimodule-is-faithfully-balanced
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

Let $T = \operatorname{End}(_R M)$ and $B = \operatorname{BiEnd}(_R M) = \operatorname{End}(M_T)$. Then $_B M$ and $M_T$ are automatically faithful: $B$ is defined as a subring of $\operatorname{End}_{\mathbb{Z}}(M)$, so the action is faithful; similarly $T \leq \operatorname{End}_{\mathbb{Z}}(M)$ acts faithfully on $M$.

By definition, every $T$-endomorphism of $M$ is an element of $B$, so the natural map $B \to \operatorname{End}(M_T)$ is surjective (in fact, it is the identity).

For the other side: the ring homomorphism $\lambda: R \to B$ with $\lambda(r)x = rx$ gives an $R$-module structure on $M$ that factors through $B$, so $_B M$ is a module. By (4.8), $\operatorname{End}(_B M) \leq \operatorname{End}(_R M) = T$. That is, every $B$-endomorphism of $M$ is an $R$-endomorphism, i.e., an element of $T$. This means the natural map $T \to \operatorname{End}(_B M)$ is surjective. Since $T$ acts faithfully, it is also injective, hence an isomorphism.

Therefore both natural maps are isomorphisms, and $_B M_T$ is faithfully balanced.
