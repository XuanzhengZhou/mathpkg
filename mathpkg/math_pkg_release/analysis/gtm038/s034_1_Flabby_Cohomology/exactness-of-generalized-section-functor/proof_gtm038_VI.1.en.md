---
role: proof
locale: en
of_concept: exactness-of-generalized-section-functor
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

The functoriality follows directly from the definition of $\varphi_*$ as post-composition: for sheaf homomorphisms $\psi: \mathcal{S}_1 \to \mathcal{S}$ and $\varphi: \mathcal{S} \to \mathcal{S}_2$, we have $(\varphi \circ \psi)_* = \varphi_* \circ \psi_*$ and $(\text{id}_{\mathcal{S}})_* = \text{id}_{\hat{\Gamma}(U,\mathcal{S})}$.

For exactness, let $0 \to \mathcal{S}_1 \xrightarrow{\alpha} \mathcal{S} \xrightarrow{\beta} \mathcal{S}_2 \to 0$ be an exact sequence of $R$-module sheaves. Since generalized sections are defined pointwise without continuity constraints, the exactness at the level of stalks lifts directly to exactness of the sequence
$$0 \to \hat{\Gamma}(U, \mathcal{S}_1) \xrightarrow{\alpha_*} \hat{\Gamma}(U, \mathcal{S}) \xrightarrow{\beta_*} \hat{\Gamma}(U, \mathcal{S}_2) \to 0.$$
At each point $x \in U$, the stalk sequence $0 \to (\mathcal{S}_1)_x \to \mathcal{S}_x \to (\mathcal{S}_2)_x \to 0$ is exact, so for any generalized section $s$ one can construct preimages pointwise. The surjectivity of $\beta_*$ holds because at each $x$ there exists a preimage in $\mathcal{S}_x$, and a generalized section can be chosen arbitrarily without continuity constraints to realize that preimage globally.
