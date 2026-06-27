---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{l\text{shift}}$ is a Turing submachine that combines tape seeking, writing, and the $T_{l\text{trans}}$ translation operation. In the canonical case, it transforms the pattern $0\ 1^{(x+1)}\ 0\ 1^{(y+1)}\ 0$ into $0\ 1^{(y+1)}\ 0\ 0^{(x+2)}$, effectively swapping the positions of the two blocks of ones. This machine is used in more complex computations where blocks of encoded numbers need to be reordered on the tape.
