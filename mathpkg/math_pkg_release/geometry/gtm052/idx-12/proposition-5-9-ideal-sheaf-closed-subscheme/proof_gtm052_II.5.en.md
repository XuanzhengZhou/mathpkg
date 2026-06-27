---
role: proof
locale: en
of_concept: proposition-5-9-ideal-sheaf-closed-subscheme
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

If $Y$ is a closed subscheme of $X$, then the inclusion morphism $i: Y ightarrow X$ is quasi-compact (obvious) and separated (4.6), so by (5.8), $i_*\mathcal{O}_Y$ is quasi-coherent on $X$. Hence $\mathcal{I}_Y$, being the kernel of a morphism of quasi-coherent sheaves, is also quasi-coherent. If $X$ is noetherian, then for any open affine subset $U = \operatorname{Spec} A$ of $X$, the ring $A$ is noetherian, so the ideal $I = \Gamma(U, \mathcal{I}_Y|_U)$ is finitely generated, so $\mathcal{I}_Y$ is coherent.

Conversely, given a scheme $X$ and a quasi-coherent sheaf of ideals $\mathcal{J}$, let $Y$ be the support of the quotient sheaf $\mathcal{O}_X/\mathcal{J}$. Then $Y$ is a subspace of $X$, and $(Y, \mathcal{O}_X/\mathcal{J})$ is the unique closed subscheme of $X$ with ideal sheaf $\mathcal{J}$. The unicity is clear, so we have only to check that $(Y, \mathcal{O}_X/\mathcal{J})$ is a closed subscheme. This is a local question, so we may assume $X = \operatorname{Spec} A$ is affine. Since $\mathcal{J}$ is quasi-coherent, $\mathcal{J} = 	ilde{\mathfrak{a}}$ for some ideal $\mathfrak{a} \subseteq A$. Then $(Y, \mathcal{O}_X/\mathcal{J})$ is just the closed subscheme of $X$ determined by $\mathfrak{a}$.
