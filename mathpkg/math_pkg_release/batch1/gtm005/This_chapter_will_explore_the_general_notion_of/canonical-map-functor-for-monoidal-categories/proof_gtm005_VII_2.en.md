---
role: proof
locale: en
of_concept: canonical-map-functor-for-monoidal-categories
source_book: gtm005
source_chapter: "VII"
source_section: "2. Coherence"
---

By Theorem 1 (Coherence), for each object $b \in B$ there is a unique strict morphism $W \rightarrow B$ with $(-) \mapsto b$. For words $v, w$ of length $n$, the functors $v_B$ and $w_B$ are defined recursively. When we substitute an $n$-tuple $(b_1, \ldots, b_n)$ of objects of $B$ for the $n$ blanks in $v$ and $w$, we obtain two objects $v(b_1, \ldots, b_n)$ and $w(b_1, \ldots, b_n)$ in $B$.

By the coherence theorem applied to the monoidal category $B^{B^n}$ (or equivalently by considering the word $v$ and $w$ as operations on $n$ variables), the unique morphism property of $W$ guarantees that there is a unique natural transformation from $v_B$ to $w_B$ built from the coherence isomorphisms $\alpha, \lambda, \varrho$ and their inverses, closed under $\square$ and composition. This defines $\mathrm{can}_B(v, w)$.

The verification of the properties follows from the construction:
- For words of length $0$, the only functors are the constant functor $e$, and the identity $e \rightarrow e$ is canonical.
- For length $1$, the only functor without $e_0$ is the identity $I_B$, and $\mathrm{id}_{I_B}$ is canonical.
- The fundamental isomorphisms $\alpha, \lambda, \varrho$ are instances of canonical maps (e.g., $\alpha$ corresponds to the word pair $((- \square -) \square -, - \square (- \square -))$ of length $3$), and their inverses are canonical as well.
- If $\mathrm{can}(v,w)$ and $\mathrm{can}(w,u)$ are canonical, their composite is canonical (composition of the corresponding natural transformations).
- If $\mathrm{can}(v,w)$ and $\mathrm{can}(v',w')$ are canonical, then $\mathrm{can}(v,w) \square \mathrm{can}(v',w')$ is canonical for the word pair $(v \square v', w \square w')$.

The uniqueness follows from the coherence theorem: any two natural transformations built from $\alpha, \lambda, \varrho$ between the same pair of functors $v_B$ and $w_B$ must be equal, as otherwise substituting a particular object $b$ would yield two distinct arrows $v_b \rightarrow w_b$ in $B$, contradicting Theorem 1.
