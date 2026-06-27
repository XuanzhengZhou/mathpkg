---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.5"
proof_technique: universal-property
locale: en
content_hash: ""
written_against: ""
---
Let $F$ be the free abelian group on $A \times B$ and $K$ as in Definition 5.1. The assignment $(a,b) \mapsto g(a,b)$ determines a unique homomorphism $g_1: F \to C$. Since $g$ is middle linear, $g_1$ maps every generator of $K$ to 0, so $K \subset \operatorname{Ker} g_1$. By Theorem 1.7, $g_1$ induces $\bar{g}: F/K \to C$ with $\bar{g}[(a,b) + K] = g(a,b)$. But $F/K = A \otimes_R B$ and $(a,b) + K = a \otimes b$. Uniqueness follows because elementary tensors generate $A \otimes_R B$.
