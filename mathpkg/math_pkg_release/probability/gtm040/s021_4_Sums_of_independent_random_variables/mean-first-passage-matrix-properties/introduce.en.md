---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 6-42 lists the three basic properties satisfied by the mean first passage time matrix $M$ of an ergodic Markov chain. Property (1) is obvious from the definition ($M_{ii} = 0$ since no time is needed to reach the current state). Property (3) follows from Proposition 6-41 and the relation $ar{M} = D + M$. The non-trivial part is property (2): every $M_{ij}$ is finite for an ergodic chain. The proof uses the bound $M_{ij} \leq 1/(lpha_j \cdot {}^jar{H}_{ji})$ and the fact that ${}^jar{H}_{ji} > 0$ for an ergodic chain (all states communicate).
