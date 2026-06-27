---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{rend}$ is the companion submachine to $T_{lend}$ for locating the right end of a tape block. It scans leftward until encountering two consecutive zeros ($00$) and halts on the leftmost zero. Together with $T_{lend}$, these two machines provide the basic navigation capabilities needed for Turing machine constructions that manipulate blocks of encoded numbers.
