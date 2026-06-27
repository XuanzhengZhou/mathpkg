---
role: proof
locale: en
of_concept: semisimple-nilpotent-decomposition-via-direct-sum
source_book: gtm023
source_chapter: "12"
source_section: "3"
---

**Proof:** From the direct sum decomposition $\Gamma(\bar{t}) = A \oplus \operatorname{rad} \Gamma(\bar{t})$ (statement 3), every $x \in \Gamma(\bar{t})$ can be written uniquely as
$$
x = x_N + x_R, \quad x_N \in A, \quad x_R \in \operatorname{rad} \Gamma(\bar{t}).
$$
By statement 4, every element of $A$ is semisimple, so $x_N$ is semisimple. Every element of the radical is nilpotent, so $x_R$ is nilpotent. By the uniqueness of the semisimple-nilpotent (Jordan-Chevalley) decomposition, this must be the canonical decomposition of $x$ into its semisimple and nilpotent parts.
