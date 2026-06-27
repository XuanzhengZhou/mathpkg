---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Machine $T_{\text{seek}1}$ is the first non-trivial composite Turing machine introduced in the text. Built from simpler machines ($T_{\text{right}}$, $T_{\text{left}}$, $T_1$, $T_0$, $T_{l\text{seek}1}$, $T_{r\text{seek}1}$) using the arrow concatenation notation, it searches outward in both directions for a $1$ on the tape. It uses $1$'s as markers to track how far the search has progressed, erasing them afterward so the tape is restored to its original state. If the tape is entirely blank, the search never terminates. This construction demonstrates how flow chart composition yields a machine with non-trivial behavior while maintaining the invariant that the final tape matches the initial tape.
