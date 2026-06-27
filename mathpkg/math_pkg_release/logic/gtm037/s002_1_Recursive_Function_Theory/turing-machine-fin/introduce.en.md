---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{\text{fin}}$ ("finish") is a Turing submachine designed to clean up the tape at the end of a computation. It erases intermediate scratchwork (encoded blocks of ones) and leaves only the desired output block on the tape, followed by an appropriate number of zeros. Given a tape with $m$ argument blocks plus an output block, $T_{\text{fin}}$ collapses them all, preserving only the output block $1^{(y+1)}$ in the final configuration. It is an essential utility for composing Turing machine computations.
