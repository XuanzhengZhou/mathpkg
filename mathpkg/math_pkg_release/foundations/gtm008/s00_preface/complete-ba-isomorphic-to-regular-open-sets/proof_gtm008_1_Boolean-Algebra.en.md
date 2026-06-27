---
role: proof
locale: en
of_concept: complete-ba-isomorphic-to-regular-open-sets
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** Define $F(b) = [b]$ for each $b \in B$. Then $F$ maps into the regular open subsets of $B_0$.

First, $F$ preserves addition: $F(a + b) = [a + b] = [a] + [b] = F(a) + F(b)$, since $x \leq a + b$ iff $[x] \subseteq ([a] \cup [b])^{-0}$.

Second, $F$ preserves multiplication: $[a][b] = \{x \in B_0 \mid x \leq a \land x \leq b\} = \{x \in B_0 \mid x \leq ab\} = [ab]$, so $F(ab) = F(a)F(b)$.

Third, $F$ preserves complementation: $- [b] = (B_0 - [b])^0 = B_0 - [b]^-$. Then $a \in -[b] \leftrightarrow a \neq 0 \land [a] \cap [b] = 0 \leftrightarrow a \neq 0 \land ab = 0 \leftrightarrow a \neq 0 \land a \leq -b \leftrightarrow a \in [-b]$. Thus $-F(b) = F(-b)$.

To prove $F$ is onto, note that if $A$ is a regular open subset, then $A = \bigcup_{b \in A} [b]$. Therefore $A = A^{-0} = (\bigcup_{b \in A} [b])^{-0} = \sum_{b \in A} [b]$. Since $B$ is complete, there exists $a = \sum_{b \in A} b \in B$. Then $F(a) = [a] = A$, establishing surjectivity. Thus $F$ is an isomorphism.
