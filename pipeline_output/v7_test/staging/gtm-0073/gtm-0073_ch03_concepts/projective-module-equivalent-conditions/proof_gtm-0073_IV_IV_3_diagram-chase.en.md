---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.3"
proof_technique: diagram-chase
locale: en
content_hash: ""
written_against: ""
---
(i) $\Rightarrow$ (ii) Consider the diagram with $1_P: P \to P$ and epi $g: B \to P$. Projectivity gives $h: P \to B$ with $gh = 1_P$, so the sequence splits by Theorem 1.18.

(ii) $\Rightarrow$ (iii) By Corollary 2.2, there is a free module $F$ and an epimorphism $F \to P$. The short exact sequence $0 \to K \to F \to P \to 0$ splits by (ii), giving $F \cong K \oplus P$.

(iii) $\Rightarrow$ (i) $F \cong K \oplus P$ free implies $P$ is a direct summand of a projective module. Compose any map $f: P \to B$ with the projection $F \to P$, lift via projectivity of $F$, then restrict via the injection $P \to F$.
