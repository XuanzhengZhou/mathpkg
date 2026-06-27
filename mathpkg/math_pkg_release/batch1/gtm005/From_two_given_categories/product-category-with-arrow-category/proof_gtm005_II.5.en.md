---
role: proof
locale: en
of_concept: product-category-with-arrow-category
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

The product $C \times \mathbf{2}$ embeds into the arrow category $C^{\mathbf{2}}$ but they are not equivalent. An object of $C \times \mathbf{2}$ is $(c, j)$ with $j \in \{0, 1\}$. An object of $C^{\mathbf{2}}$ is an arrow $f: a \to b$ in $C$.

The embedding $E: C \times \mathbf{2} \hookrightarrow C^{\mathbf{2}}$ sends $(c, 0)$ to $1_c: c \to c$ and $(c, 1)$ to $1_c: c \to c$ (identity arrows). An arrow $(f, 1_0): (c, 0) \to (d, 0)$ maps to the commutative square with $f$ on top and bottom; $(f, \alpha): (c, 0) \to (c, 1)$ maps to the square with $1_c$ horizontally and $f, f$ vertically — but this is not square-natural unless we use a different interpretation.

The universal property of $C^{\mathbf{2}}$ is that functors $D \to C^{\mathbf{2}}$ classify natural transformations, while $C \times \mathbf{2}$ classifies pairs of functors with a (very restricted) natural transformation.
