---
role: proof
locale: en
of_concept: cghaus-cartesian-closed
source_book: gtm005
source_chapter: "VII"
source_section: "8"
---

$\mathbf{CGHaus}$ is cartesian closed. For $X, Y \in \mathbf{CGHaus}$, define the internal hom $Y^X = k(C(X, Y))$, where $C(X, Y)$ has the compact-open topology and $k$ is the Kelley functor (retopologizing so that a set is closed iff its intersection with every compact subset is closed).

Adjointness: $\mathbf{CGHaus}(X \times Y, Z) \cong \mathbf{CGHaus}(X, Z^Y)$. Given $f: X \times Y \to Z$, define $\hat{f}: X \to Z^Y$ by $\hat{f}(x)(y) = f(x, y)$. Continuity of $\hat{f}$ follows from: for compact $K \subseteq X$, the restricted map $K \to Z^Y$ is continuous in the compact-open topology (since $K \times Y$ is compactly generated, $f|_{K \times Y}$ is continuous, and the evaluation $\operatorname{ev}: Z^Y \times Y \to Z$ is continuous after applying $k$).

The bijection is established by the exponential law for compactly generated spaces: $k(X \times Y) = X \times_k Y$ (the Kelley product), and the natural homeomorphism $Z^{X \times_k Y} \cong (Z^Y)^X$ in $\mathbf{CGHaus}$.
