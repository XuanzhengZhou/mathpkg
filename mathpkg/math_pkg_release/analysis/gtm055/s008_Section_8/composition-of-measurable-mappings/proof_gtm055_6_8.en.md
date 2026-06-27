---
role: proof
locale: en
of_concept: composition-of-measurable-mappings
source_book: gtm055
source_chapter: "6"
source_section: "8"
---

The proof is elementary. For any $U \in \mathbf{U}$, we have

$$(\Psi \circ \Phi)^{-1}(U) = \Phi^{-1}(\Psi^{-1}(U)).$$

Since $\Psi$ is measurable, $\Psi^{-1}(U) \in \mathbf{T}$. Since $\Phi$ is measurable, $\Phi^{-1}(\Psi^{-1}(U)) \in \mathbf{S}$. Hence $(\Psi \circ \Phi)^{-1}(U) \in \mathbf{S}$ for every $U \in \mathbf{U}$, proving that $\Psi \circ \Phi$ is measurable. The Borel measurable case follows by taking $\mathbf{S} = \mathbf{B}_X$, $\mathbf{T} = \mathbf{B}_Y$, $\mathbf{U} = \mathbf{B}_Z$.
