---
role: proof
locale: en
of_concept: baire-property-in-density-topology
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

**($\Rightarrow$)** Suppose $A$ has the property of Baire relative to $\mathcal{T}$. Then $A = U \triangle M$ where $U$ is open in $\mathcal{T}$ and $M$ is of first category in $\mathcal{T}$. Every open set in $\mathcal{T}$ is of the form $\phi(B) - N$ for some $B \in S$, $N \in \mathcal{N}$, or a union of such sets. By the proof of Theorem 22.5, any union of basic open sets equals $\phi(C) - N'$ for some $C \in S$, $N' \in \mathcal{N}$. Hence $U = \phi(C) - N' \in S$. By Theorem 22.6, $M$ (being of first category) belongs to $\mathcal{N} \subset S$. Therefore $A = (\phi(C) - N') \triangle M \in S$.

**($\Leftarrow$)** Conversely, if $A \in S$, then by definition $A$ is measurable. Write $A = \phi(A) \triangle (A \triangle \phi(A))$. Now $\phi(A)$ is a basic open set in $\mathcal{T}$ (take $N = \emptyset$), and $A \triangle \phi(A)$ is a nullset by property (1) of the lower density. By Theorem 22.6, every nullset is nowhere dense, hence of first category. Therefore $A$ is the symmetric difference of an open set and a first category set, so $A$ has the property of Baire.
