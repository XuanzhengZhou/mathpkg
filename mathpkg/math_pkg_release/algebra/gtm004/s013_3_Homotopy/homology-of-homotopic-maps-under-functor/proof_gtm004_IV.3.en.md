---
role: proof
locale: en
of_concept: homology-of-homotopic-maps-under-functor
source_book: gtm004
source_chapter: "IV"
source_section: "3. Homotopy"
---

# Proof of Homology of Homotopic Maps under a Functor

**Corollary 3.5.** Let $\varphi, \psi : C \rightarrow D$ be chain maps. If $\varphi \simeq \psi$, then for any additive functor $F : \mathcal{A} \rightarrow \mathcal{B}$, the induced homomorphisms

$$H(F(\varphi)), H(F(\psi)) : H(F(C)) \rightarrow H(F(D))$$

coincide; i.e., $H(F(\varphi)) = H(F(\psi))$.

*Proof.* By Lemma 3.4, the additivity of $F$ implies that $F(\varphi) \simeq F(\psi)$ in $\mathbf{Ch}(\mathcal{B})$. By Proposition 3.1, homotopic chain maps induce the same homomorphism in homology. Hence

$$H(F(\varphi)) = H(F(\psi)).$$

In particular, the homology functor $H$ factors through the homotopy category, and this factorization is compatible with any additive functor $F$. $\square$

**Remark.** The contrapositive of this corollary provides a useful criterion to detect that two chain maps are *not* homotopic: if there exists an additive functor $F$ such that $H(F(\varphi)) \neq H(F(\psi))$, then $\varphi$ and $\psi$ cannot be homotopic. The example given in the text takes $F = -\otimes \mathbb{Z}_2$, where two specific maps $\varphi, 0 : C \rightarrow D$ are shown to be non-homotopic because $H_1(\varphi \otimes \mathbb{Z}_2) \neq H_1(0 \otimes \mathbb{Z}_2)$.
