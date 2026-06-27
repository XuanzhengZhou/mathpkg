---
role: proof
locale: en
of_concept: analytic-continuation-along-line
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

First consider the case where the centers $\alpha_i$ are arranged monotonically along $\ell$. If a disc $D_i$ is wholly contained in some other disc $D_k$ in $\mathcal{K}$, then the function element $(D_i, f_i)$ is redundant (since $f_k$ already extends $f_i$ on $D_i \subset D_k$) and can be removed without loss. Hence assume no disc contains another.

Under this assumption, if $D_i \cap D_k \neq \emptyset$ for some $i < k - 1$, then the geometry of discs with centers on a line forces $D_i \cap D_{k-1} \neq \emptyset$. This ensures that overlapping discs are consecutive in the chain (after removing redundancies). The local agreement of consecutive function elements then extends to a well-defined function on the entire union $D_0 \cup \cdots \cup D_n$ by the uniqueness of analytic continuation.
