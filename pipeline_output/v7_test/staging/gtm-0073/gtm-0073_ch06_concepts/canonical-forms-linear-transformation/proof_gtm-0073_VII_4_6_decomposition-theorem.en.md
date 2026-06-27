---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: decomposition-theorem
locale: en
content_hash: ""
written_against: ""
---
(i) By Theorem 4.2, $E = E_1 \oplus \cdots \oplus E_t$ where each $E_i$ is $\phi$-cyclic with minimal polynomial $q_i$ (the invariant factor). By Theorem 4.3, each $E_i$ has a basis in which $\phi|_{E_i}$ is the companion matrix of $q_i$. By Lemma 4.5, the direct sum of these companion matrices is the matrix of $\phi$ on the concatenated basis. This is the rational canonical form.

(ii) Further decomposing each $E_i$ into primary cyclic summands (Theorem 4.2(ii)) and applying the same argument gives the primary rational canonical form.

(iii) When the irreducible factors are all linear, each elementary divisor is $(x - b)^r$. By Corollary 4.4, the restriction of $\phi$ to each primary cyclic subspace has an elementary Jordan matrix (Jordan block) relative to some basis. The direct sum of these Jordan blocks gives the Jordan canonical form.
