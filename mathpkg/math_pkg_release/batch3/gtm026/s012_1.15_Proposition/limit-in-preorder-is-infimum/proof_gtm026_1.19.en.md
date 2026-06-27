---
role: proof
locale: en
of_concept: limit-in-preorder-is-infimum
source_book: gtm026
source_chapter: "1"
source_section: "1.19"
---

In a preordered category, there is at most one morphism between any two objects, and the composition and identity conditions hold by definition of a preorder. A lower bound $(L, \psi)$ requires morphisms $\psi_i: L \to D_i$ for each $i \in N(\Delta)$, which in a preorder means $L \leqslant D_i$ for all $i$. The commutativity condition $\psi_i \circ D_\alpha = \psi_j$ is automatically satisfied in a preorder since there is at most one morphism from $L$ to $D_j$.

The universal property of a limit states that for any other lower bound $(L', \psi')$ (i.e., $L' \leqslant D_i$ for all $i$), there exists a unique morphism $f: L' \to L$ with $f \circ \psi_i = \psi'_i$. In the preorder, this means $L' \leqslant L$ and the composition condition is automatic. Thus $L$ is a lower bound with $L' \leqslant L$ for every lower bound $L'$, which is precisely the definition of $L = \operatorname{Inf}(D_i)$.
