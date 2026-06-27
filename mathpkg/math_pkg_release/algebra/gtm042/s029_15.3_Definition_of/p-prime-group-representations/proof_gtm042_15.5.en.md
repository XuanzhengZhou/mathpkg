---
role: proof
locale: en
of_concept: p-prime-group-representations
source_book: gtm042
source_chapter: "15"
source_section: "15.5"
---

Let $E$ be an $A[G]$-module which is free over $A$. We can write $E$ as a quotient $L/R$ of a free $A[G]$-module $L$. Since $E$ is $A$-free, the exact sequence $0 \to R \to L \to E \to 0$ splits over $A$. 

Because the order of $G$ is prime to $p$, the group algebra $A[G]$ is semisimple modulo $p$, and Maschke's theorem implies that every $k[G]$-module is projective. By standard lifting techniques (cf. 14.4), the same holds for $A$-free $A[G]$-modules, establishing (i).

For (ii), the reduction mod $\mathfrak{m}$ sends simple $K[G]$-modules to simple $k[G]$-modules. Since $|G|$ is prime to $p$, the Brauer-Nesbitt theorem implies this map is a bijection.

For (iii), once $S_K$ and $S_k$ are identified, the Cartan matrix $C$ is the identity because every simple $k[G]$-module is its own projective cover (it is already projective). The decomposition matrix $D$ is the identity because reduction mod $\mathfrak{m}$ is a bijection on simples. Finally, $C = D \cdot E$ with $C = D = I$ forces $E = I$.
