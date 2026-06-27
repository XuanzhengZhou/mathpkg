---
role: proof
locale: en
of_concept: spectral-sequence-composition-functors
source_book: gtm004
source_chapter: "IX"
source_section: "6. Applications: Homology of Small Categories, Spectral Sequences"
---

# Proof of Spectral Sequence for Composition of Functors (J-Homology)

**Theorem 6.1.** Let $\mathfrak{U} \xrightarrow{J} \mathfrak{V} \xrightarrow{I} \mathfrak{W}$ be functors between small categories, and let $\mathfrak{A}$ be an abelian category with enough projectives. Then there is a spectral sequence

$$E_1^{p,q} = H_p(I, H_{q-p}(J, -)) \Rightarrow H_q(IJ, -).$$

**Proof.** We only have to show that projectives in $[\mathfrak{U}, \mathfrak{A}]$ are transformed by $\widetilde{J}$ into $\widetilde{I}$-acyclic objects in $[\mathfrak{V}, \mathfrak{A}]$. Since $\widetilde{J}$ is additive, it is enough to check this claim on functors

$$R = \widetilde{K}_U P_U: \mathfrak{U} \rightarrow \mathfrak{A},$$

where $P_U$ is projective in $\mathfrak{A}$. Such functors generate the $\mathcal{E}_1'$-projectives under coproducts and direct summands, by Theorem 4.1 and Corollary 5.4.

Now compute

$$\widetilde{J}(\widetilde{K}_U P_U) = \widetilde{K}_{JU} P_U$$

by the formula (5.14) of the text, which identifies the Kan extension of a "single-object" functor. The functor $\widetilde{K}_{JU} P_U$ is projective in $[\mathfrak{V}, \mathfrak{A}]$ (it is a coproduct of copies of $P_U$, indexed by morphisms out of $JU$). In particular, it is $\widetilde{I}$-acyclic for any functor $I$, since projectives are always acyclic for any left derived functor.

Thus $\widetilde{J}$ sends $\mathcal{E}_1'$-projectives to $\widetilde{I}$-acyclics. By the standard Grothendieck spectral sequence for the composition of functors $\widetilde{I} \circ \widetilde{J} = \widetilde{IJ}$, we obtain the spectral sequence

$$E_1^{p,q} = (L_p^{\mathcal{E}_1''} \widetilde{I})(L_q^{\mathcal{E}_1'} \widetilde{J}) \Rightarrow L_{p+q}^{\mathcal{E}_1'} (\widetilde{I} \circ \widetilde{J}),$$

where $\mathcal{E}_1''$ is the projective class in $[\mathfrak{V}, \mathfrak{A}]$. Translating via the definition of the $J$-homology functors $H_n(J, -) = L_n^{\mathcal{E}_1'} \widetilde{J}$, this becomes

$$E_1^{p,q} = H_p(I, H_{q-p}(J, -)) \Rightarrow H_q(IJ, -).$$

(Note the index shift $q-p$ reflects the standard convention for the $E_1$-page of such a spectral sequence.) $\square$
