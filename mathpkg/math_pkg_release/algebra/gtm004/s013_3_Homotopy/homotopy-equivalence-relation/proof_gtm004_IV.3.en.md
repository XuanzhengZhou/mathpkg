---
role: proof
locale: en
of_concept: homotopy-equivalence-relation
source_book: gtm004
source_chapter: "IV"
source_section: "3. Homotopy"
---

# Proof of Homotopy is an Equivalence Relation

**Lemma 3.2.** The homotopy relation "$\simeq$" is an equivalence relation.

*Proof.* Plainly "$\simeq$" is reflexive and symmetric. Indeed, $\varphi - \varphi = 0 = \partial 0 + 0\partial$ shows reflexivity, and if $\psi - \varphi = \partial\Sigma + \Sigma\partial$, then $\varphi - \psi = \partial(-\Sigma) + (-\Sigma)\partial$ shows symmetry.

To check transitivity, let $\psi - \varphi = \partial\Sigma + \Sigma\partial$ and $\chi - \psi = \partial T + T\partial$ (suppressing the subscripts). An easy calculation shows

$$\chi - \varphi = (\chi - \psi) + (\psi - \varphi) = (\partial T + T\partial) + (\partial\Sigma + \Sigma\partial) = \partial(T + \Sigma) + (T + \Sigma)\partial.$$

Hence $\varphi \simeq \chi$, and the homotopy relation is transitive. $\square$
