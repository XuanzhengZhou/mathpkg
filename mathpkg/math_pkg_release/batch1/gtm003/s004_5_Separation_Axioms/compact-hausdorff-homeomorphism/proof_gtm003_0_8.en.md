---
role: proof
locale: en
of_concept: compact-hausdorff-homeomorphism
source_book: gtm003
source_chapter: "0"
source_section: "8"
---

Let $f : X \to Y$ be a continuous bijection with $X$ compact and $Y$ Hausdorff. To show $f^{-1}$ is continuous, it suffices to show $f$ is closed. Let $C \subset X$ be closed. Since $X$ is compact and $C$ is a closed subspace, $C$ is also compact. By continuity of $f$, $f(C)$ is a compact subset of the Hausdorff space $Y$, hence $f(C)$ is closed in $Y$. Thus $f$ sends closed sets to closed sets, i.e., $f$ is a closed map, so $f^{-1}$ is continuous. Therefore $f$ is a homeomorphism.

For the equivalent formulation: If $\mathfrak{T}_1$ is compact on $X$ and $\mathfrak{T}_2$ is Hausdorff on $X$ with $\mathfrak{T}_2 \subset \mathfrak{T}_1$, then the identity map $(X, \mathfrak{T}_1) \to (X, \mathfrak{T}_2)$ is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism, so $\mathfrak{T}_1 = \mathfrak{T}_2$.
