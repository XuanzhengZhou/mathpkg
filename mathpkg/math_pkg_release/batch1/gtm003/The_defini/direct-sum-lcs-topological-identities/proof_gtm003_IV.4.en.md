---
role: proof
locale: en
of_concept: direct-sum-lcs-topological-identities
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Proof.** Let $\{E_{\alpha}: \alpha \in A\}$ be a family of l.c.s. and let $E$ be their locally convex direct sum. By the duality between products and direct sums (Theorem 4.3), the dual $E'$ is algebraically isomorphic with $\prod_{\alpha} E'_{\alpha}$.

1. The identity $\tau(E, E') = \bigoplus_{\alpha} \tau(E_{\alpha}, E'_{\alpha})$ follows from applying Theorem 4.2 to the families of convex, circled, weakly compact subsets of the duals, using the fact that the dual of a direct sum is the product of the duals.

2. The identity $\tau(E', E) = \prod_{\alpha} \tau(E'_{\alpha}, E_{\alpha})$ follows similarly from Theorem 4.3 (part 2) applied to the product of the strong duals $E'_\alpha$, using the algebraic isomorphism $E' \cong \prod_\alpha E'_\alpha$. $\square$
