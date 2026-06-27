---
role: proof
locale: en
of_concept: tensor-with-ring
source_book: gtm013
source_chapter: "5"
source_section: "19"
---

Since $(m, r) \mapsto mr$ defines an $R$-balanced map $M \times R \to M$, the universal property of the tensor product gives a $\mathbb{Z}$-homomorphism $\eta: M \otimes_R R \to M$ with $\eta(m \otimes r) = mr$. The map $\eta$ is clearly an $R$-homomorphism. Define $\eta: M \to M \otimes_R R$ by $\eta(m) = m \otimes 1$, which is an $R$-homomorphism by (19.4). Clearly $\eta \circ \eta = 1_M$. Since $M \otimes_R R = \{m \otimes 1 \mid m \in M\}$ (because $m \otimes r = mr \otimes 1$), it follows that $\eta \circ \eta = 1_{M \otimes_R R}$. The proof for the left module case is symmetric.
