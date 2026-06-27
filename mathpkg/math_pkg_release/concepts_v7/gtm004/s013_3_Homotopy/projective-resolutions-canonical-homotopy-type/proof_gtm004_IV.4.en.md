---
role: proof
locale: en
of_concept: projective-resolutions-canonical-homotopy-type
source_book: gtm004
source_chapter: "IV"
source_section: "4. Projective and Injective Resolutions"
---

# Proof of Projective Resolutions Have the Same Homotopy Type

**Proposition 4.3.** Two projective resolutions of $A$ are canonically of the same homotopy type.

*Proof.* Let $C$ and $D$ be two projective resolutions of $A$. By Theorem 4.1, there exist chain maps $\varphi : C \rightarrow D$ and $\psi : D \rightarrow C$ inducing the identity in

$$H_0(C) = A = H_0(D).$$

The composition $\psi \varphi : C \rightarrow C$, as well as the identity $1 : C \rightarrow C$, both induce the identity in $A$. By Theorem 4.1 (the uniqueness-up-to-homotopy clause), we have

$$\psi \varphi \simeq 1_C.$$

Analogously,

$$\varphi \psi \simeq 1_D.$$

Hence $C$ and $D$ are of the same homotopy type; i.e., they are isomorphic in the homotopy category. Moreover, since the homotopy class of the homotopy equivalence $\varphi : C \rightarrow D$ is uniquely determined (by Theorem 4.1), the resolutions $C$ and $D$ are *canonically* of the same homotopy type. $\square$

**Remark.** This proposition is fundamental for the definition of left derived functors: it guarantees that $L_n F(A)$, defined via any projective resolution of $A$, is independent of the choice of resolution up to canonical isomorphism.
