---
role: proof
locale: en
of_concept: kernel-of-complete-homomorphism
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.**

1. If $f$ is a complete Boolean homomorphism on $\mathbf{B}$ and $A \subseteq \ker(f)$, then $f(\sum_{a \in A} a) = \sum_{a \in A} f(a) = \sum_{a \in A} 0 = 0$. Consequently $\sum_{a \in A} a \in \ker(f)$, so $\ker(f)$ is complete.

2. If $A \subseteq \ker(f)$ and $A \in M$, then $f(\sum_{a \in A} a) = \sum_{a \in A} f(a) = 0$. Hence $\sum_{a \in A} a \in \ker(f)$, so $\ker(f)$ is $M$-complete.
