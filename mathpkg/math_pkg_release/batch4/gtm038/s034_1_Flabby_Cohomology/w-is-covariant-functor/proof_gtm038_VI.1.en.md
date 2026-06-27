---
role: proof
locale: en
of_concept: w-is-covariant-functor
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

(1) Let $\psi: \mathcal{S}_1 \to \mathcal{S}$, $\varphi: \mathcal{S} \to \mathcal{S}_2$ be sheaf homomorphisms and $s \in \Gamma(U, \mathcal{S}_1)$. Then
$$W(\varphi \circ \psi) \circ r s = r((\varphi \circ \psi)_* s) = r(\varphi_*(\psi_* s)) = W\varphi \circ (r(\psi_* s)) = W\varphi \circ W\psi \circ r s.$$
Since $r$ is an isomorphism, this yields $W(\varphi \circ \psi) = W\varphi \circ W\psi$.

(2) $W(\text{id}_{\mathcal{S}}) \circ r s = r((\text{id}_{\mathcal{S}})_* s) = r s$ for $s \in \Gamma(U, \mathcal{S})$. Again, since $r$ is an isomorphism, $W(\text{id}_{\mathcal{S}}) = \text{id}_{W(\mathcal{S})}$.
