---
role: proof
locale: en
of_concept: formal-criterion-for-adjoint
source_book: gtm005
source_chapter: "X"
source_section: "1. Adjoints and Limits"
---

**Proof.** A functor $G: A \to X$ has a left adjoint precisely when for each $x \in X$, the comma category $(x \downarrow G)$ has an initial object. By Lemma 1, an initial object in a category is equivalently a limit of the identity functor. The projection $Q: (x \downarrow G) \to A$ sends each object $\langle g: x \to Ga, a \rangle$ to $a$.

If a left adjoint $F$ exists, then the universal arrow $\eta_x: x \to G(Fx)$ is the initial object of $(x \downarrow G)$, so condition (ii) holds via the characterization of initial objects as limits of the identity. Since right adjoints preserve limits, condition (i) follows.

Conversely, if conditions (i) and (ii) hold, then for each $x$, the limit $Fx = \mathrm{Lim}\, Q$ exists in $A$. One verifies that this limit produces an initial object in $(x \downarrow G)$ whose vertex is the universal arrow $x \to G(Fx)$, establishing that $F$ is left adjoint to $G$.
