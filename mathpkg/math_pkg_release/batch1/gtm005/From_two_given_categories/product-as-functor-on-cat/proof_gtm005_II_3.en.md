---
role: proof
locale: en
of_concept: product-as-functor-on-cat
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

The product $\times$ is a pair of functions: on objects, $\langle B, C \rangle \mapsto B \times C$; on arrows, $\langle U, V \rangle \mapsto U \times V$. When composites $U' \circ U$ and $V' \circ V$ are defined, one has
$$(U' \times V') \circ (U \times V) = U'U \times V'V,$$
which follows directly from the componentwise definition. This verifies that $\times$ preserves composition. It also preserves identities: $I_B \times I_C = I_{B \times C}$. Hence, on restricting to small categories, $\times$ is a functor $\mathbf{Cat} \times \mathbf{Cat} \to \mathbf{Cat}$.
