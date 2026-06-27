---
role: proof
locale: en
of_concept: ext-of-structure-sheaf
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

The functor $\operatorname{Hom}(\mathcal{O}_X,\cdot)$ is naturally isomorphic to the identity functor on $\operatorname{Mod}(X)$, since $\operatorname{Hom}(\mathcal{O}_X,\mathcal{G}) \cong \mathcal{G}$ via evaluation at the unit section $1 \in \mathcal{O}_X$. Consequently, its derived functors vanish for $i > 0$: $\mathcal{E}xt^i(\mathcal{O}_X,\mathcal{G}) = 0$ for $i > 0$, and $\mathcal{E}xt^0(\mathcal{O}_X,\mathcal{G}) = \mathcal{G}$. This proves (a) and (b).

For (c), observe that the functors $\operatorname{Hom}(\mathcal{O}_X,\cdot)$ and $\Gamma(X,\cdot)$ are equal as functors from $\operatorname{Mod}(X)$ to $\mathbf{Ab}$. Indeed, $\operatorname{Hom}(\mathcal{O}_X,\mathcal{G}) = \Gamma(X,\mathcal{G})$ for any $\mathcal{O}_X$-module $\mathcal{G}$. Therefore their derived functors coincide:
$$\operatorname{Ext}^i(\mathcal{O}_X,\mathcal{G}) = R^i\operatorname{Hom}(\mathcal{O}_X,\cdot)(\mathcal{G}) = R^i\Gamma(X,\cdot)(\mathcal{G}) = H^i(X,\mathcal{G}).$$
The identification with cohomology uses (2.6), which defines $H^i(X,\mathcal{G})$ as the right derived functors of $\Gamma(X,\cdot)$.
