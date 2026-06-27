---
role: proof
locale: en
of_concept: cde-triangle-commutativity
source_book: gtm042
source_chapter: "15"
source_section: "15.4"
---

The commutativity $c = d \circ e$ follows directly from the definitions of the three homomorphisms. Recall that $c: P_k(G) \to R_k(G)$ is the Cartan homomorphism, $d: R_K(G) \to R_k(G)$ is the decomposition homomorphism (reduction mod $\mathfrak{m}$), and $e: P_k(G) \to R_K(G)$ is defined by composing the tensor-product-with-$K$ functor $P_A(G) \to R_K(G)$ with the inverse of the canonical isomorphism $P_A(G) \to P_k(G)$.

For a projective $A[G]$-module $X$, its class in $P_A(G)$ maps under $c$ (identified with $P_k(G)$) to $[k \otimes_A X] \in R_k(G)$. Under $e$, it maps to $[K \otimes_A X] \in R_K(G)$, and then $d$ sends this to $[k \otimes_K (K \otimes_A X)] = [k \otimes_A X] \in R_k(G)$. Thus $d(e([X])) = c([X])$, so $d \circ e = c$. In matrix terms, $D \cdot E = C$.
