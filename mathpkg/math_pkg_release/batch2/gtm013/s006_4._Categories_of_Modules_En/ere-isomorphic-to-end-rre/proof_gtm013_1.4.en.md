---
role: proof
locale: en
of_concept: ere-isomorphic-to-end-rre
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

Apply Proposition 4.6 with $M = Re$, viewed as an $R$-$eRe$-bimodule (since $Re \cdot eRe = Re$). The map $\rho: eM = eRe \to \operatorname{Hom}_R(Re, Re) = \operatorname{End}(_R Re)$ from (4.6) sends $ere$ to the map $ae \mapsto aere$. This is an isomorphism of $eRe$-bimodules.

To verify it is a ring isomorphism: for $er_1e, er_2e \in eRe$,
$\rho(er_1e \cdot er_2e)(ae) = \rho(er_1er_2e)(ae) = aer_1er_2e = \rho(er_1e)(aer_2e) = \rho(er_1e)(\rho(er_2e)(ae)) = (\rho(er_1e) \circ \rho(er_2e))(ae)$.
Thus $\rho$ preserves multiplication, and clearly $\rho(e) = \operatorname{id}_{Re}$.

The right-sided version is symmetric: apply (4.6) with $M = eR$ as an $eRe$-$R$-bimodule. Then $\lambda: eRe \to \operatorname{Hom}_R(eR_R, eR_R) = \operatorname{End}(eR_R)$ sends $ere$ to $ea \mapsto erea$, which is a ring anti-isomorphism (or an isomorphism when endomorphisms are written as right operators).

For the biendomorphism statement: by (4.12), $\operatorname{BiEnd}(_R Re) = \operatorname{End}(Re_{\operatorname{End}(_R Re)})$. Since $\operatorname{End}(_R Re) \cong eRe$ via $\rho$, we have $\operatorname{BiEnd}(_R Re) \cong \operatorname{End}(Re_{eRe})$.
