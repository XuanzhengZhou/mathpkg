---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Machine $T_{l\text{seek}1}$ is a two-state Turing machine that searches leftward on the tape for the first occurrence of the symbol $1$. It moves left across any $0$'s it encounters and halts when it reaches a $1$ cell. Unlike the seek-0 machines, $T_{l\text{seek}1}$ may fail to terminate if no $1$ exists to the left of the starting position; in that case the computation continues forever. This non-termination behavior is essential for expressing partial recursive functions in Turing machine terms.
