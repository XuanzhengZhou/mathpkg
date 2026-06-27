---
role: proof
locale: en
of_concept: tensor-locally-free-injective-is-injective
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

To show that $\mathcal{L} \otimes \mathcal{I}$ is injective, we must prove that the functor $\operatorname{Hom}(-, \mathcal{L} \otimes \mathcal{I})$ is exact. Using the adjunction between tensor product and sheaf Hom (II, Ex. 5.1), we have a natural isomorphism of functors:
$$\operatorname{Hom}(-, \mathcal{L} \otimes \mathcal{I}) \cong \operatorname{Hom}(- \otimes \mathcal{L}^\vee, \mathcal{I}),$$
where $\mathcal{L}^\vee = \mathcal{H}om(\mathcal{L}, \mathcal{O}_X)$ is the dual of $\mathcal{L}$.

Now consider the composite functor: first tensor with $\mathcal{L}^\vee$, then apply $\operatorname{Hom}(-, \mathcal{I})$. The functor $- \otimes \mathcal{L}^\vee$ is exact because $\mathcal{L}^\vee$ is locally free of finite rank, hence flat. The functor $\operatorname{Hom}(-, \mathcal{I})$ is exact because $\mathcal{I}$ is injective. Therefore the composite $\operatorname{Hom}(- \otimes \mathcal{L}^\vee, \mathcal{I})$ is exact, and by the isomorphism above, $\operatorname{Hom}(-, \mathcal{L} \otimes \mathcal{I})$ is exact. Hence $\mathcal{L} \otimes \mathcal{I}$ is injective.
