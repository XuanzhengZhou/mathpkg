---
role: proof
locale: en
of_concept: homotopy-invariance-of-tensor-and-hom
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "1. Double Complexes"
---

# Proof of Homotopy Invariance of Tensor Product and Hom Complexes

**Corollary 1.3.** If $C \simeq C'$ and $D \simeq D'$, then $C \otimes_\Lambda D \simeq C' \otimes_\Lambda D'$ and $\operatorname{Hom}_\Lambda(C, D) \simeq \operatorname{Hom}_\Lambda(C', D')$.

**Proof.** Suppose $C \simeq C'$ and $D \simeq D'$. Then there exist chain maps $\varphi: C \to C'$, $\varphi': C' \to C$ and chain homotopies $\varphi' \varphi \simeq 1_C$, $\varphi \varphi' \simeq 1_{C'}$; similarly, there exist $\psi: D \to D'$, $\psi': D' \to D$ with $\psi' \psi \simeq 1_D$, $\psi \psi' \simeq 1_{D'}$.

By Proposition 1.2, these induce chain maps
$$\varphi \otimes \psi: C \otimes_\Lambda D \to C' \otimes_\Lambda D', \quad \varphi' \otimes \psi': C' \otimes_\Lambda D' \to C \otimes_\Lambda D.$$
Moreover, again by Proposition 1.2, the homotopies on $C$ and $D$ induce homotopies:
$$(\varphi' \otimes \psi')(\varphi \otimes \psi) = \varphi' \varphi \otimes \psi' \psi \simeq 1_C \otimes 1_D = 1_{C \otimes D},$$
$$(\varphi \otimes \psi)(\varphi' \otimes \psi') = \varphi \varphi' \otimes \psi \psi' \simeq 1_{C'} \otimes 1_{D'} = 1_{C' \otimes D'}.$$
Thus $\varphi \otimes \psi$ is a homotopy equivalence, showing $C \otimes_\Lambda D \simeq C' \otimes_\Lambda D'$.

The argument for $\operatorname{Hom}_\Lambda(C, D) \simeq \operatorname{Hom}_\Lambda(C', D')$ is symmetric, using the Hom part of Proposition 1.2.
