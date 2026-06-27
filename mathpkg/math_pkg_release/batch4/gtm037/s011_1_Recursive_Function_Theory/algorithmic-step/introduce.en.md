---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

An algorithmic step formalizes one computation step of a Markov algorithm. Given an input word $d$, the algorithm scans its rules from top to bottom (smallest index $i$) to find the first rule whose left-hand side $a_i$ occurs in $d$. It then replaces the leftmost occurrence of $a_i$ in $d$ with the corresponding right-hand side $b_i$, producing the output word $e$. This deterministic leftmost-outermost matching strategy ensures that at each step the computation is uniquely determined. The resulting pair $(d, e)$ is called an algorithmic step under $A$.
