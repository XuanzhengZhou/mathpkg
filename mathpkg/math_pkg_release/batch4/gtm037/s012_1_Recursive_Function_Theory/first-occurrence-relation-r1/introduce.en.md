---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The first occurrence relation $R_1$ is a quaternary relation that encodes the notion of the leftmost position at which a word $b$ occurs in a word $d$. It specifies that $d$ decomposes as the concatenation $a b c$, where $a$ is the prefix before the first occurrence of $b$ and $c$ is the suffix after it, with the additional condition that no proper prefix of $a$ contains $b$. This relation is crucial for formalizing the step-by-step operation of a Markov algorithm, where the first matching row is applied at each step.
