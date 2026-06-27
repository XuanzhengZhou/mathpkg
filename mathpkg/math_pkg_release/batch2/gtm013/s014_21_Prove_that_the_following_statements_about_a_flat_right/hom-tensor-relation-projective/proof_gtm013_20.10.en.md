---
role: proof
locale: en
of_concept: hom-tensor-relation-projective
source_book: gtm013
source_chapter: "20"
source_section: "20.10"
---

It is tedious but not difficult to check that $\eta$ is a $\mathbb{Z}$-homomorphism natural in all three variables.

Now for each ${}_S U_T$ and ${}_T N$, consider the case $P = S$. By Proposition 20.1 and (20.5.3):

$$\operatorname{Hom}_S(S, U) \otimes_T N \cong U \otimes_T N \cong \operatorname{Hom}_S(S, U \otimes_T N)$$

via $\gamma \otimes_T n \mapsto \gamma(1) \otimes_T n \mapsto \rho(\gamma(1) \otimes_T n)$ where $\rho$ is the isomorphism from (20.1). But for all $s \in S$:

$$\eta(\gamma \otimes_T n)(s) = \gamma(s) \otimes_T n = s(\gamma(1) \otimes_T n) = [\rho(\gamma(1) \otimes_T n)](s).$$

Thus $\eta: \operatorname{Hom}_S(S, U) \otimes_T N \to \operatorname{Hom}_S(S, U \otimes_T N)$ is precisely the composite of these isomorphisms, hence is itself an isomorphism.

Now by Lemma 20.9, the class of modules $P$ for which $\eta$ is an isomorphism is closed under direct summands and finite direct sums. Since $S$ belongs to this class, so does any finitely generated free module $S^{(n)}$. By (17.3), any finitely generated projective $P$ is a direct summand of a finitely generated free module, hence $\eta$ is an isomorphism for all finitely generated projective $P$.
