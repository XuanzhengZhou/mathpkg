---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

An occurrence of a word $a$ in a word $b$ is formalized as a triple $(c, a, d)$ where $b = cad$, representing the decomposition of $b$ into a prefix $c$, the matched substring $a$, and a suffix $d$. Since $a$ may occur multiple times in $b$, the first occurrence is defined as the one with the shortest possible prefix $c$, i.e. the leftmost occurrence. This leftmost-first matching strategy is the standard rule application convention in Markov algorithms.
