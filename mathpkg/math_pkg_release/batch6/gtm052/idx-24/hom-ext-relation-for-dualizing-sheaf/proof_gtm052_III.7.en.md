---
role: proof
locale: en
of_concept: hom-ext-relation-for-dualizing-sheaf
source_book: gtm052
source_chapter: "III"
source_section: "7"
---

Let $0 \to \omega_P \to \mathcal{I}^\bullet$ be an injective resolution of $\omega_P$ in $\operatorname{Mod}(P)$. Then we calculate $\operatorname{Ext}^i_P(\mathcal{F}, \omega_P)$ as the cohomology groups $h^i$ of the complex $\operatorname{Hom}_P(\mathcal{F}, \mathcal{I}^\bullet)$. But since $\mathcal{F}$ is an $\mathcal{O}_X$-module, any morphism $\mathcal{F} \to \mathcal{I}^i$ factors through $\mathcal{J}^i = \mathcal{H}om_P(\mathcal{O}_X, \mathcal{I}^i)$. Thus we have

$$\operatorname{Ext}^i_P(\mathcal{F}, \omega_P) = h^i(\operatorname{Hom}_X(\mathcal{F}, \mathcal{J}^\bullet)).$$

Now each $\mathcal{J}^i$ is an injective $\mathcal{O}_X$-module. Indeed, for $\mathcal{F} \in \operatorname{Mod}(X)$, $\operatorname{Hom}_X(\mathcal{F}, \mathcal{J}^i) = \operatorname{Hom}_P(\mathcal{F}, \mathcal{I}^i)$, so $\operatorname{Hom}_X(\cdot, \mathcal{J}^i)$ is an exact functor because $\mathcal{I}^i$ is injective. Furthermore, by (7.3) we have $h^i(\mathcal{J}^\bullet) = 0$ for $i \neq r$, and $h^r(\mathcal{J}^\bullet) = \omega_X$. Hence $\mathcal{J}^\bullet$ gives an injective resolution of $\omega_X$ up to a shift. Therefore the cohomology of $\operatorname{Hom}_X(\mathcal{F}, \mathcal{J}^\bullet)$ computes $\operatorname{Ext}^i_X(\mathcal{F}, \omega_X)$ after an appropriate shift. Comparing the two expressions yields the isomorphism $\operatorname{Hom}_X(\mathcal{F}, \omega_X) \cong \operatorname{Ext}^r_P(\mathcal{F}, \omega_P)$.
