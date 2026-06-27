---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{n\text{copy}}$ generalizes $T_{\text{copy}}$ to sequences of $n$ blocks. Given a tape configuration with $n$ blocks of encoded numbers, it copies the $n$th block (the rightmost) to the left end, after the first block. The machine is defined recursively as $T_{\text{copy}} \cdot T_{2 \text{copy}}^{n-1}$, leveraging repeated application of the copy operation. This provides a systematic way to access and duplicate arbitrarily indexed arguments in multi-argument Turing machine computations.
