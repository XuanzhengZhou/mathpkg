---
role: proof
locale: en
of_concept: hash-open-continuous-map
source_book: gtm008
source_chapter: "22"
source_section: "22. The Completion of a Boolean Algebra"
---

1. $b_1 \in (\#^{-1})``[b_0] \leftrightarrow \#(b_1) \leq b_0 \leftrightarrow b_1 \leq i(b_0) \leftrightarrow b_1 \in [i(b_0)]$.

2. $\#$ is continuous because of 1. We show that $\#``[b_1]$ is open for every $b_1 \in B_1$. Let $b_0 \in \#``[b_1]$. If $b'_0 \leq b_0$, then since $\#$ is order preserving, $b'_0 \leq \#(b_1)$ and hence
   $$b'_0 = b'_0 \cdot \#(b_1) = \#(i(b'_0) \cdot b_1) \quad \text{by 5 of Theorem 22.10}$$
   $$\in \#``[b_1],$$
   hence $[b_0] \subseteq \#``[b_1]$. $\#$ is onto by Theorem 22.10.3.

3. Obvious from 1.
