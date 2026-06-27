---
role: proof
locale: en
of_concept: "infinite-model-from-arbitrarily-large-finite"
source_book: gtm022
source_chapter: "V"
source_section: "3"
---
Proof. Let $\mathcal{T} = (\mathcal{R}, A, C)$. Form $\mathcal{T}'$ by adding $\{\operatorname{al}(n) \mid n \in \mathbb{N}^+\}$ to the axioms, where $\operatorname{al}(n)$ asserts the existence of at least $n$ distinct elements. If $\mathcal{T}' \vdash F$, then a finite subset of the new axioms suffices, say up to $\operatorname{al}(m)$. But $\mathcal{T}$ has a model with at least $m$ elements, which would also satisfy this finite set and make $F$ true---contradiction. Thus $\mathcal{T}'$ is consistent and has a model, which must be infinite. $\square$
