---
role: proof
locale: en
of_concept: ext-tensor-product-isomorphism
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

[Note: The proof in the source text is truncated. The standard proof proceeds as follows.]

For the $\operatorname{Ext}$ group isomorphism, fix an injective resolution $\mathcal{G} \to I^\bullet$. The key is the natural isomorphism of complexes:
$$\operatorname{Hom}^\bullet(\mathcal{F} \otimes \mathcal{L}, I^\bullet) \cong \operatorname{Hom}^\bullet(\mathcal{F}, \mathcal{L}^\vee \otimes I^\bullet),$$
which follows from the tensor-hom adjunction (II, Ex. 5.1). Since $\mathcal{L}^\vee$ is locally free of finite rank, each $\mathcal{L}^\vee \otimes I^k$ is injective by Lemma 6.6, so $\mathcal{L}^\vee \otimes I^\bullet$ is an injective resolution of $\mathcal{L}^\vee \otimes \mathcal{G}$. Taking cohomology of both sides yields:
$$\operatorname{Ext}^i(\mathcal{F} \otimes \mathcal{L}, \mathcal{G}) \cong \operatorname{Ext}^i(\mathcal{F}, \mathcal{L}^\vee \otimes \mathcal{G}).$$

For the $\mathcal{E}xt$ sheaf version, the same reasoning applies using the sheaf Hom and the sheaf tensor-hom adjunction:
$$\mathcal{H}om(\mathcal{F} \otimes \mathcal{L}, I^\bullet) \cong \mathcal{H}om(\mathcal{F}, \mathcal{L}^\vee \otimes I^\bullet) \cong \mathcal{H}om(\mathcal{F}, I^\bullet) \otimes \mathcal{L}^\vee,$$
where the last isomorphism holds because $\mathcal{L}^\vee$ is locally free of finite rank. Taking cohomology yields the stated isomorphisms for $\mathcal{E}xt$.
