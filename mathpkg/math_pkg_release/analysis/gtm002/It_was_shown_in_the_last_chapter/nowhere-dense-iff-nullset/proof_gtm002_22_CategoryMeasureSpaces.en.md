---
role: proof
locale: en
of_concept: nowhere-dense-iff-nullset
source_book: gtm002
source_chapter: "22"
source_section: "Category Measure Spaces"
---

If $N \in \mathcal{N}$, then $X - N = \phi(X) - N$ is a member of $\mathcal{T}$, hence $N$ is closed. Moreover, any open set contained in $N$ must be a nullset, hence its closure must also be a nullset, and therefore its interior is empty. Thus $N$ is nowhere dense.

Conversely, suppose $N$ is nowhere dense relative to $\mathcal{T}$. By definition of $\mathcal{T}$, any open set is a member of $\mathcal{T}$, hence of the form $\phi(A) - M$ with $A \in S$ and $M \in \mathcal{N}$. Since $N$ is nowhere dense, its closure $\overline{N}$ has empty interior. But by the property of the topology, any closed set with empty interior is a nullset. Hence $N \in \mathcal{N}$.
