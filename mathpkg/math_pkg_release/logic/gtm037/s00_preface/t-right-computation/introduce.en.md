---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition characterizes the computation performed by the Turing machine $T_{\text{right}}$. Starting from the initial state $0$ with any tape description $F$ and head position $e$, the machine executes exactly one computation step: it moves the tape one square to the right (action $v_j = 2$) and transitions to state $1$, where it then stops because the matrix row for state $1$ specifies action $4$ (stop). Thus $T_{\text{right}}$ always halts after a single step, producing the same tape description $F$ but with the head one position to the right, corresponding to $e-1$.
