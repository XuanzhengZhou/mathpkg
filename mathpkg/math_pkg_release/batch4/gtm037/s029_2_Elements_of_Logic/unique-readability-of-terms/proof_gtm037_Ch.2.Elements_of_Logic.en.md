---
role: proof
locale: en
of_concept: unique-readability-of-terms
source_book: gtm037
source_chapter: "2"
source_section: "Elements of Logic"
---

(i) Since every term is formed as a nonempty finite sequence (either a singleton variable $\langle v_m \rangle$ or a compound expression beginning with an operation symbol followed by subterms), every term is nonempty.

(ii) Let $\sigma$ be a term. By Definition 10.8(ii), $\text{Trm}$ is the intersection of all classes closed under variable and operation-symbol formation rules. Consider the first symbol of $\sigma$. 

If the first symbol is $v_m$ for some $m \in \omega$, then $\sigma$ must be exactly $\langle v_m \rangle$, for if $\sigma$ began with $v_m$ and contained further symbols, it would have to be formed via rule (2) of 10.8(ii), which requires the first symbol to be an operation symbol $\mathbf{O} \in \text{Dmn } \mathcal{O}$. Since $v_m \notin \text{Dmn } \mathcal{O}$, this is impossible. The index $m$ is uniquely determined because $v$ is a one-one function.

If the first symbol is some $\mathbf{O} \in \text{Dmn } \mathcal{O}$, then necessarily $\sigma = \langle \mathbf{O} \rangle \sigma_0 \cdots \sigma_{m-1}$ where $m = \mathcal{O}\mathbf{O}$ and each $\sigma_i \in \text{Trm}$. The uniqueness of $\mathbf{O}$ follows from $v \cap \mathcal{O} = \emptyset$ (variables and operation symbols are disjoint). The subterms $\sigma_0, \ldots, \sigma_{m-1}$ are uniquely determined because the length of each is determined by its own unique decomposition, proceeding by induction on the length of $\sigma$.
