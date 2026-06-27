---
role: proof
locale: en
of_concept: j-homology-existence
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Existence of J-Homology via Derived Kan Extension

**Theorem 5.6.** If $\mathfrak{A}$ has enough projectives then the $J$-homology

$$H_*(J, -): [\mathfrak{U}, \mathfrak{A}] \rightarrow [\mathfrak{V}, \mathfrak{A}]$$

exists. It may be computed as the left $\mathcal{E}_1'$-derived functor of the Kan extension,

$$H_n(J, T) = (L_n^{\mathcal{E}_1'} \widetilde{J})T, \quad n = 0, 1, \dots.$$

**Proof.** Since $\mathfrak{A}$ has enough projectives, the category $[\mathfrak{U}_d, \mathfrak{A}]$ (where $\mathfrak{U}_d$ is the discrete category on the objects of $\mathfrak{U}$) has enough projectives: the projectives are simply families $\{P_U\}_{U \in \mathfrak{U}}$ where each $P_U$ is projective in $\mathfrak{A}$. Let $\mathcal{E}_1$ be the class of all epimorphisms in $[\mathfrak{U}_d, \mathfrak{A}]$; this is a projective class. The inclusion $I: \mathfrak{U}_d \hookrightarrow \mathfrak{U}$ induces, by Theorem 4.1 applied to the adjunction $\widetilde{I} \dashv I^*$, a projective class $\mathcal{E}_1' = (I^*)^{-1}\mathcal{E}_1$ in $[\mathfrak{U}, \mathfrak{A}]$.

Now $J^*: [\mathfrak{V}, \mathfrak{A}] \rightarrow [\mathfrak{U}, \mathfrak{A}]$ is the precomposition functor. By Theorem 5.1, $\widetilde{J}$ is left adjoint to $J^*$. Since $[\mathfrak{U}, \mathfrak{A}]$ has the projective class $\mathcal{E}_1'$ with enough projectives, we may form the left $\mathcal{E}_1'$-derived functors of the right-exact functor $\widetilde{J}$. Define

$$H_n(J, T) = (L_n^{\mathcal{E}_1'} \widetilde{J})T, \quad n = 0, 1, \dots$$

for $T \in [\mathfrak{U}, \mathfrak{A}]$. These constitute the $J$-homology functors.

The projectives in $[\mathfrak{U}, \mathfrak{A}]$ relative to $\mathcal{E}_1'$ are precisely, by Theorem 4.1 and Corollary 5.4, the direct summands of functors of the form

$$\bar{S}(U') = \coprod_{U \in \mathfrak{U}} \coprod_{v \in \mathfrak{U}(U, U')} (P_U)_v,$$

where each $P_U$ is projective in $\mathfrak{A}$ and $(P_U)_v = P_U$. Thus a functor $S: \mathfrak{U} \rightarrow \mathfrak{A}$ is $\mathcal{E}_1'$-projective if and only if it is a direct summand of such a coproduct functor. With this description of the projectives, the left derived functors are well-defined and yield the $J$-homology as claimed. $\square$
