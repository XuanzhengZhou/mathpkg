---
role: proof
locale: en
of_concept: haus-complete-cocomplete
source_book: gtm005
source_chapter: "IV. Adjoints"
source_section: "9. Adjoints in Topology"
---

The left adjoint $H$ is obtained by the adjoint functor theorem. First, any product of Hausdorff spaces or subspace of a Hausdorff space is also Hausdorff, hence $\mathbf{Haus}$ is complete and the inclusion functor is continuous (i.e., preserves small limits).

It remains only to verify the solution set condition for every topological space $X$. Any continuous map of $X$ to a Hausdorff space $Y$ factors through its image, a subspace of $Y$, hence Hausdorff. This image is a quotient set of $X$ with some topology, so there is at most a small set of (non-isomorphic) surjections $X \to Y$ to a Hausdorff $Y$. This establishes the solution set condition.

The resulting left adjoint $H$ assigns to each space $X$ a Hausdorff space $HX$ and a continuous map $\eta: X \to HX$, universal from $X$ to a Hausdorff space. The universal property implies that $\eta$ is a surjection, so $HX$ may be described as the "largest Hausdorff quotient" of $X$. If $X$ is already Hausdorff, we may take $HX = X$ and $\eta = 1$, so $H$ is a left-adjoint-left-inverse to the inclusion.

The forgetful functor $\mathbf{Haus} \to \mathbf{Set}$ also has a left adjoint: equip a set $S$ with the discrete topology, which is Hausdorff.
