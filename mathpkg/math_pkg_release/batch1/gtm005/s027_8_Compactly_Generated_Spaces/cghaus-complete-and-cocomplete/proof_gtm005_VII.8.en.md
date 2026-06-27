---
role: proof
locale: en
of_concept: cghaus-complete-and-cocomplete
source_book: gtm005
source_chapter: "VII"
source_section: "8"
---

$\mathbf{CGHaus}$ is both complete and cocomplete.

**Limits**: For a diagram $D: J \to \mathbf{CGHaus}$, compute the limit $L$ in $\mathbf{Top}$. Since $k$ is right adjoint to the inclusion $\mathbf{CGHaus} \hookrightarrow \mathbf{Top}$, it preserves limits. The limit in $\mathbf{CGHaus}$ is $\varprojlim D = k(L)$. Since all objects in the diagram are in $\mathbf{CGHaus}$, and the limit of compactly generated spaces computed in $\mathbf{Top}$ may not be compactly generated, applying $k$ corrects this.

**Colimits**: Similarly, compute the colimit $C$ in $\mathbf{Top}$, then $\varinjlim D = k(C)$. The Kelley functor, as a left adjoint (when $\mathbf{CGHaus}$ is viewed appropriately), preserves colimits.

Since $\mathbf{Top}$ has all small limits and colimits, and $k$ provides the necessary correction, $\mathbf{CGHaus}$ inherits completeness and cocompleteness.
