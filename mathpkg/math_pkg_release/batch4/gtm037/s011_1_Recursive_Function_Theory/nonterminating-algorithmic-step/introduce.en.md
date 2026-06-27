---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Each rule $(a_i, b_i, c_i)$ in a Markov algorithm carries a termination flag $c_i \in \{0, 1\}$. When an algorithmic step applies the $i$-th rule, the step is classified as nonterminating if $c_i = 0$ (computation continues) or terminating if $c_i = 1$ (computation halts after this step). The algorithm's computation proceeds by repeatedly applying algorithmic steps to the current word until either no rule is applicable or a terminating step is executed, at which point the current word is the output of the algorithm.
