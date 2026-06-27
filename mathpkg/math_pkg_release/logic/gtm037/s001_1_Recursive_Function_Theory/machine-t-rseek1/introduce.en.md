---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Machine $T_{r\text{seek}1}$ is a two-state Turing machine that searches rightward on the tape for the first occurrence of the symbol $1$. It moves right across any $0$'s it encounters and halts when it reaches a $1$ cell. Like $T_{l\text{seek}1}$, it may fail to terminate if no $1$ exists to the right; in that case the computation continues forever. Together with $T_{l\text{seek}1}$, it provides a bidirectional search mechanism for the symbol $1$.
