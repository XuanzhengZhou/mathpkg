---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{\text{copy}}$ is a Turing submachine that duplicates a block of encoded number on the tape. Starting from a configuration $0\ 1^{(x+1)}\ 0\ 0^{(x+2)}$ (where the trailing zeros provide workspace), it produces $0\ 1^{(x+1)}\ 0\ 1^{(x+1)}\ 0$, creating an identical copy of the original block. This copy operation is central to many Turing machine computations where the same argument must be used multiple times.
