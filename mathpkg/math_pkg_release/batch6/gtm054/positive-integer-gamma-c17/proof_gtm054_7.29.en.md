---
role: proof
locale: en
of_concept: positive-integer-gamma-c17
source_book: gtm054
source_chapter: "7"
source_section: "Section 29"
---

Observe that if $n \geq m + 1$, then all the 2$m$ statements are true for $K_n$. We assume, therefore, that $\Gamma$ is not complete. The entanglement of the implications that we prove is indicated by the directed graph in Figure C18.

B₁ ⇒ A. The condition B₁ is precisely C8. The implication follows from Whitney's theorem (C7).

Bₖ ⇒ Cₖ-1 (k = 2, ..., m). Let S ∈ 𝒐ₖ-1(V) and {a, z} ∈ 𝒐₂(V + S) be given. Assume Bₖ with z = z₁ and S = {z₁, ..., zₖ}. This provides an openly-disjoint [m - (k - 1)]-family of az-paths which avoid S.

Cₖ ⇒ A (k = 1, ..., m - 1). Let U ⊆ V, and suppose that a is an interior vertex of Γ_U and that z is an exterior vertex of Γ_U. Let S be the set of attachment vertices of Γ_U. By the definitions, every az-path contains a vertex in S.

Suppose |S| ≤ k. By Cₖ, there exists an openly-disjoint (m - k)-family of az-paths in Γ_(S), and since m - k > 0, this family is not empty; i.e., some az-path contains no vertex of S. Hence |S| > k. Let T ∈ 𝒐ₖ(S). Similarly, there exists an openly-disjoint (m - k)-family of az-paths in Γ_(T). Since no two of these paths contain the same vertex in S + T, we have m - k ≤ |S + T| = |S| - k. Hence Γ_U has |S| ≥ m attachment vertices, and Γ is m-connected by Exercise C16.
