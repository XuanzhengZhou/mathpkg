---
role: proof
locale: en
of_concept: baire-property-measurable-equivalence
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

($\Rightarrow$) Suppose $A \subset X$ has the property of Baire with respect to $\mathcal{T}$. Then $A$ can be written as $A = U \triangle M$, where $U$ is $\mathcal{T}$-open and $M$ is of first category in $\mathcal{T}$. Every $\mathcal{T}$-open set is of the form $\phi(B) \setminus N$ for some $B \in S$ and $N \in \mathcal{N}$, hence belongs to $S$ (since $\phi(B) \in S$ and $S$ is a $\sigma$-algebra). By Theorem 22.6, every set of first category in $\mathcal{T}$ belongs to $\mathcal{N}$, so $M \in S$. Therefore $A = U \triangle M \in S$.

($\Leftarrow$) Conversely, suppose $A \in S$ (i.e., $A$ is $\mu$-measurable). By property (1) of the lower density, $A \triangle \phi(A) \in \mathcal{N}$. By Theorem 22.6, $\mathcal{N}$ consists exactly of the $\mathcal{T}$-nowhere dense sets, so $A \triangle \phi(A)$ is $\mathcal{T}$-nowhere dense (hence of first category in $\mathcal{T}$). Since $\phi(A)$ is $\mathcal{T}$-open (being a basic open set $\phi(A) \setminus \emptyset$), we have expressed $A$ as the symmetric difference of an open set and a first category set. Thus $A$ has the property of Baire in $\mathcal{T}$.
