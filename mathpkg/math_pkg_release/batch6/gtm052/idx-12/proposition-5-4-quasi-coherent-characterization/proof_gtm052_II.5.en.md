---
role: proof
locale: en
of_concept: proposition-5-4-quasi-coherent-characterization
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

Let $\mathcal{F}$ be quasi-coherent on $X$, and let $U = \operatorname{Spec} A$ be an open affine. As in the proof of Lemma 5.3, there is a base for the topology consisting of open affines for which the restriction of $\mathcal{F}$ is the sheaf associated to a module. It follows that $\mathcal{F}|_U$ is quasi-coherent, so we can reduce to the case $X$ affine $= \operatorname{Spec} A$. Let $M = \Gamma(X, \mathcal{F})$. Then in any case there is a natural map $\alpha: \tilde{M} \to \mathcal{F}$ (Ex. 5.3). Since $\mathcal{F}$ is quasi-coherent, $X$ can be covered by open sets $D(g_i)$ with $\mathcal{F}|_{D(g_i)} \cong \tilde{M}_i$ for some $A_{g_i}$-module $M_i$. Now Lemma 5.3, applied to the open set $D(g_i)$, tells us exactly that $\mathcal{F}(D(g_i)) \cong M_{g_i}$, so $M_i = M_{g_i}$. It follows that the map $\alpha$, restricted to $D(g_i)$, is an isomorphism. The $D(g_i)$ cover $X$, so $\alpha$ is an isomorphism.

Now suppose that $X$ is noetherian, and $\mathcal{F}$ coherent. Then, using the above notation, we have the additional information that each $M_{g_i}$ is a finitely generated $A_{g_i}$-module, and we want to prove that $M$ is finitely generated. This follows from standard properties of finite generation under localization on a noetherian ring.
