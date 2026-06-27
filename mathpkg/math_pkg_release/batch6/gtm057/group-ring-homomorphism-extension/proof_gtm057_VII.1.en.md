---
role: proof
locale: en
of_concept: group-ring-homomorphism-extension
source_book: gtm057
source_chapter: "VII"
source_section: "1"
---

**Theorem (1.2):** An arbitrary mapping $\phi: G \to A$ into an additive abelian group $A$ extends uniquely to an additive homomorphism $\phi: JG \to A$.

*Proof.* Any element $v \in JG$ has a unique representation $v = \sum_i n_i g_i$ with distinct $g_i \in G$ and nonzero integers $n_i$. Define $\phi(v) = \sum_i n_i \phi(g_i)$ and $\phi(0) = 0$. This is well-defined because the representation is unique. Additivity follows directly. If $A$ is a ring and $\phi$ preserves products on $G$, then $\phi(v_1 v_2) = \phi(v_1)\phi(v_2)$ follows by distributivity and the product formula in $JG$.

**Corollary (1.3):** Every group homomorphism $\phi: G \to G'$ extends uniquely to a ring homomorphism $\phi: JG \to JG'$. This follows from (1.2) applied to the composition $G \xrightarrow{\phi} G' \hookrightarrow JG'$, noting that the extension preserves products on $G$ and hence is a ring homomorphism.
