---
role: proof
locale: en
of_concept: formal-completion-equivalence-of-categories
source_book: gtm052
source_chapter: "II"
source_section: "9"
---

We have already seen that $M \mapsto M^\triangle$ is exact (9.4). If $M$ is an $A$-module of finite type, then

$$\Gamma(\mathfrak{X}, M^\triangle) = \varprojlim M / I^n M = \hat{M},$$

and $\hat{M} = M$ because $A$ is complete (9.3Ab). Thus one composition of our two functors is the identity.

Conversely, let $\mathfrak{F}$ be a coherent $\mathcal{O}_{\mathfrak{X}}$-module. By (9.6), $\mathfrak{F} \cong \varprojlim \mathfrak{F} / \mathfrak{J}^n \mathfrak{F}$ where $\mathfrak{J}$ is an ideal of definition. Setting $M_n = \Gamma(\mathfrak{X}, \mathfrak{F} / \mathfrak{J}^n \mathfrak{F})$, we obtain an inverse system $(M_n)$ of finitely generated $A$-modules satisfying the Mittag-Leffler condition. Since $A$ is complete, $M = \varprojlim M_n$ is a finitely generated $A$-module, and $\mathfrak{F} \cong M^\triangle$. This shows the two functors are inverse equivalences.
