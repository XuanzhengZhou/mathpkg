---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition characterizes the possible computations of machine $T_1$ on an arbitrary tape description $F$. There are exactly two cases: if the currently scanned cell contains $0$, then $T_1$ writes a $1$ and halts (producing configuration $(F_1^e, 0, e)$); if it already contains $1$, then $T_1$ halts immediately without altering the tape. The machine thus ensures that the scanned cell contains $1$ upon termination, without ever moving the tape head.
