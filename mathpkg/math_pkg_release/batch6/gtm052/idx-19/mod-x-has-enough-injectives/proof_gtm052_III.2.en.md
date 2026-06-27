---
role: proof
locale: en
of_concept: mod-x-has-enough-injectives
source_book: gtm052
source_chapter: "III"
source_section: "2"
---

Let $\mathcal{F}$ be a sheaf of $\mathcal{O}_X$-modules. For each point $x \in X$, the stalk $\mathcal{F}_x$ is an $\mathcal{O}_{x,X}$-module. Since the category of modules over a ring has enough injectives (every module embeds into an injective module), there exists an injection $\mathcal{F}_x \hookrightarrow I_x$ where $I_x$ is an injective $\mathcal{O}_{x,X}$-module.

For each point $x$, let $j: \{x\} \hookrightarrow X$ denote the inclusion of the one-point space. View $I_x$ as a sheaf on the one-point space, and consider the direct image sheaf $j_*(I_x)$ on $X$. Define
$$\mathcal{I} = \prod_{x \in X} j_*(I_x).$$

For any sheaf $\mathcal{G}$ of $\mathcal{O}_X$-modules,
$$\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{G}, \mathcal{I}) = \prod_{x \in X} \operatorname{Hom}_{\mathcal{O}_X}(\mathcal{G}, j_*(I_x)) \cong \prod_{x \in X} \operatorname{Hom}_{\mathcal{O}_{x,X}}(\mathcal{G}_x, I_x).$$
The isomorphism follows from the adjunction between direct image and stalk.

Since $I_x$ is an injective $\mathcal{O}_{x,X}$-module, the functor $\operatorname{Hom}_{\mathcal{O}_{x,X}}(\cdot, I_x)$ is exact. A product of exact functors is exact, so $\operatorname{Hom}_{\mathcal{O}_X}(\cdot, \mathcal{I})$ is exact, which means $\mathcal{I}$ is injective.

The stalkwise injections $\mathcal{F}_x \hookrightarrow I_x$ induce a natural morphism $\mathcal{F} \to \mathcal{I}$ via the universal property of the product. This morphism is injective because it is injective on each stalk. Thus every sheaf $\mathcal{F}$ embeds into an injective sheaf, proving that $\operatorname{Mod}(X)$ has enough injectives.
