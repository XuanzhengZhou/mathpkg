---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Conditional probability $\mu_F(E)$ answers the question: "What is the probability of $E$ when $F$ is known to have occurred?" It is defined as $\mu_F(E) = \mu(E \cap F) / \mu(F)$, provided $\mu(F) > 0$. Intuitively, this measures the extent to which $F$ is contained in $E$ by comparing the likelihood of their simultaneous occurrence to the likelihood of $F$ alone. In the die-rolling example, if $E = \{2,4,6\}$ (even) and $F = \{1,2\}$ (less than 3), then $\mu_F(E) = \mu(\{2\}) / \mu(\{1,2\}) = (1/6)/(2/6) = 1/2$.
