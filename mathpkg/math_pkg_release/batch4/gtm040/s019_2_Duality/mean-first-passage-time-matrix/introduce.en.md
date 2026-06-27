---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The mean first passage time matrix $M$ records the expected time for a recurrent Markov chain to reach each state for the first time: $M_{ij} = M_i[t_j]$ is the mean time starting from $i$ until first hitting $j$. The variant $\bar{M}_{ij}$ counts the mean time to return to $j$ (counting from the first step). These quantities generalize to sets: $M_{iE}$ is the mean time from $i$ until $E$ is reached, and $\bar{M}_{iE}$ is the mean time to return to $E$. These definitions are essential for computations involving the regular measure $\alpha$ in the subsequent propositions.
