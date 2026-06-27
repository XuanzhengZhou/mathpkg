---
role: proof
locale: en
of_concept: discrete-topology-left-adjoint
source_book: gtm005
source_chapter: "IV. Adjoints"
source_section: "9. Adjoints in Topology"
---

The adjunction $D \dashv G$ is established by the natural bijection

$$\mathbf{Top}(DS, X) \cong \mathbf{Set}(S, GX).$$

Given a topological space $X$, any set function $f: S \to GX$ lifts uniquely to a continuous map $\tilde{f}: DS \to X$ because every function from a discrete space is continuous — all subsets of $DS$ are open, so the preimage of any open set in $X$ is automatically open. Thus $D$ is left adjoint to $G$. As a right adjoint, $G$ preserves all limits (Theorem 1, Section 3).
