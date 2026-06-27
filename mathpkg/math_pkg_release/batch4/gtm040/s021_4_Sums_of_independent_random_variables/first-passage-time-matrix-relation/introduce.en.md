---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 6-41 gives a simple relationship between the mean first passage time matrix $M$ (with $M_{ij} = M_i[ar{t}_j]$) and the transition matrix $P$. The identity follows by conditioning on the first step: from state $i 
eq j$, the chain moves in one step to some state $k$ with probability $P_{ik}$, after which the expected additional time to reach $j$ is $M_{kj}$. Including the one step already taken yields $M_{ij} = \sum_k P_{ik}(M_{kj} + 1) = (PM)_{ij} + 1$. This identity is used in Propositions 6-42 and Theorem 6-43 to characterize $M$.
