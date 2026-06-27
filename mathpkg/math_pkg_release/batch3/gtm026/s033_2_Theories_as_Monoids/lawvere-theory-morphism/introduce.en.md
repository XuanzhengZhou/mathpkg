---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A morphism of Lawvere theories $\psi: (\mathcal{T}, R) \to (\mathcal{T}', R')$ is a functor between the underlying categories that is compatible with the structure functors: $R \circ \psi = R'$. Since $R$ and $R'$ are identity-on-objects, the commutativity condition forces $\psi$ to be identity-on-objects as well, so the morphism only changes the morphisms — it maps the $n$-ary operations of one theory to $n$-ary operations of the other while preserving the "projection" mappings. This definition generalizes the notion of a theory map in clone form: a clone morphism $\lambda: T \to S$ induces a Lawvere theory morphism via the functor that sends $\alpha: BT \to A$ to $\alpha \cdot B\lambda: BS \to A$.
