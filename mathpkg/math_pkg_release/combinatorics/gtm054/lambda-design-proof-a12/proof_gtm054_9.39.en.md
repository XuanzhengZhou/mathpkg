---
role: proof
locale: en
of_concept: lambda-design-proof-a12
source_book: gtm054
source_chapter: "9"
source_section: "IXA"
---

Consider the set of ordered pairs:

$$S = \{(T, \{E_1, E_2\}) : T \in \mathcal{P}_2(V); \{E_1, E_2\} \in \mathcal{P}_2(\mathcal{E}); T \subseteq E_1 \cap E_2\}.$$

Let $\lambda(2) = m$ and $\lambda^*(2) = n$. For each $T \in \mathcal{P}_2(V)$ there are exactly $m$ blocks containing $T$, and hence $(T, \{E_1, E_2\}) \in S$ for exactly $\binom{m}{2}$ 2-sets $\{E_1, E_2\} \in \mathcal{P}_2(\mathcal{E})$. Thus $|S| = \binom{v}{2}\binom{m}{2}$. By a symmetric argument one verifies that $|S| = \binom{b}{2}\binom{n}{2}$. By Corollary A14, $m = n$.

A $t$-design with $t \geq 2$ which is also a $(; 2)$-design is by Proposition A5 a $(1, 2; 1, 2)$-design. Such a design is called a symmetric block design and will receive attention in §C when we consider BIB-designs. A symmetric $\lambda$-linked design is a nondegenerate, nontrivial $(2; 2)$-design which is not a $t$-design for any $t$.
