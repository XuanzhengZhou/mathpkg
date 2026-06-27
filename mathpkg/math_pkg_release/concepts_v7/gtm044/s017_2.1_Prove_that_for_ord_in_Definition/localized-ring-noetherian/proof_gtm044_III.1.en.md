---
role: proof
locale: en
of_concept: localized-ring-noetherian
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of The Localized Ring $R_{\mathfrak{p}}$ is Noetherian

**Lemma 3.9.** The ring $R_{\mathfrak{p}}$ is Noetherian.

*Proof.* The extension map $(\cdot)^e : \mathcal{I}(R) \to \mathcal{I}(R_{\mathfrak{p}})$ is onto (by (8): every ideal $a^* \subset R_{\mathfrak{p}}$ satisfies $a^* = (a^{*c})^e$), and its restriction to the set of contracted ideals of $R$ (i.e., ideals of the form $a^{ec}$) is a bijection onto $\mathcal{I}(R_{\mathfrak{p}})$. Moreover, $(\cdot)^e$ preserves inclusion on this set: if $a^{ec} \subset b^{ec}$, then $a^e = a^{ece} \subset b^{ece} = b^e$.

Suppose there exists an infinite strictly ascending chain of ideals in $R_{\mathfrak{p}}$:

$$a_1^* \subsetneq a_2^* \subsetneq a_3^* \subsetneq \cdots$$

Under the contraction map $(\cdot)^c$, each $a_i^*$ corresponds to the contracted ideal $a_i^{*c}$ in $R$. Since contraction preserves strict inclusion (by the injectivity of extension on contracted ideals), we obtain a strictly ascending chain

$$a_1^{*c} \subsetneq a_2^{*c} \subsetneq a_3^{*c} \subsetneq \cdots$$

in $R$. But $R = \mathbb{C}[x_1, \ldots, x_n]/I(V)$ is the coordinate ring of an affine variety, hence is Noetherian by the Hilbert Basis Theorem. Therefore any ascending chain of ideals in $R$ must stabilize, a contradiction. Thus $R_{\mathfrak{p}}$ is Noetherian. $\square$
