---
role: proof
locale: en
of_concept: elementary-ideals-homomorphism-image
source_book: gtm057
source_chapter: "VII"
source_section: "4"
---

Let $\phi: R \to R'$ be an onto ring homomorphism between commutative rings, $A$ an $m \times n$ matrix over $R$, and $\phi A = \|\phi(a_{ij})\|$.

If $0 < n-k \leq m$, each $(n-k) \times (n-k)$ subdeterminant of $\phi A$ equals $\phi$ applied to the corresponding subdeterminant of $A$, so $E_k(\phi A) \subset \phi E_k(A)$. Conversely, since $\phi$ is onto, any generator of $E_k(\phi A)$ is $\phi(d)$ for some $d \in E_k(A)$, giving $\phi E_k(A) \subset E_k(\phi A)$.

If $n-k > m$: $E_k(A) = 0$, $E_k(\phi A) = 0$, and $\phi(0) = 0$.

If $n-k \leq 0$: $E_k(A) = R$, $E_k(\phi A) = R'$, and $\phi(R) = R'$ since $\phi$ is onto.
