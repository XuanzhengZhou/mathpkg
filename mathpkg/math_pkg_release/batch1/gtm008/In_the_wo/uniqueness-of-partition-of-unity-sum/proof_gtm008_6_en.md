---
role: proof
locale: en
of_concept: uniqueness-of-partition-of-unity-sum
source_book: gtm008
source_chapter: "6"
source_section: "Boolean-Valued Structures"
---

**Proof.** For each $i \in I$,
$$b_i \leq [\![a = a_i]\!] \cdot [\![a' = a_i]\!] \leq [\![a = a']\!].$$
Since $\langle b_i \mid i \in I \rangle$ is a partition of unity,
$$1 = \sum_{i \in I} b_i \leq [\![a = a']\!] \leq 1.$$
Hence $[\![a = a']\!] = 1$. The mixed sum element $a$ is therefore unique up to equality with truth value $1$, and is sometimes denoted by $\sum_{i \in I} b_i a_i$. $\square$
