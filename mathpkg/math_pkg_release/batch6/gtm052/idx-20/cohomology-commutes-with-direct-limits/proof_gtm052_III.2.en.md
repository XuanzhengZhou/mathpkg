---
role: proof
locale: en
of_concept: cohomology-commutes-with-direct-limits
source_book: gtm052
source_chapter: "III"
source_section: "§2 Cohomology of Sheaves"
---

For each $\alpha$ we have a natural map $\mathcal{F}_\alpha \to \varinjlim \mathcal{F}_\alpha$. This induces a map on cohomology, and then we take the direct limit of these maps to obtain

$$\varinjlim H^i(X, \mathcal{F}_\alpha) \to H^i(X, \varinjlim \mathcal{F}_\alpha).$$

For $i = 0$, the result is already known (II, Ex. 1.11). For the general case, we consider the category $\operatorname{Ind}_A(\mathfrak{Ab}(X))$ consisting of all directed systems of objects of $\mathfrak{Ab}(X)$, indexed by $A$. This is an abelian category. Furthermore, since $\varinjlim$ is an exact functor, we have a natural transformation of $\delta$-functors

$$\varinjlim H^i(X, \cdot) \to H^i(X, \varinjlim \cdot)$$

from $\operatorname{Ind}_A(\mathfrak{Ab}(X))$ to $\mathfrak{Ab}$. For $i = 0$ this is an isomorphism. To show it is an isomorphism for all $i \geq 0$, it suffices to show that the left-hand side is universal (1.3A). For this, we need to show it is effaceable. Given a direct system $(\mathcal{F}_\alpha)$, we embed each $\mathcal{F}_\alpha$ in a flasque sheaf $\mathcal{G}_\alpha$ (e.g., the sheaf of discontinuous sections), and then take the direct system $(\mathcal{G}_\alpha)$. By Lemma 2.8, $\varinjlim \mathcal{G}_\alpha$ is flasque, hence acyclic for $H^i(X, \cdot)$ by Proposition 2.5. This shows effaceability and completes the proof.
