---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_{lend}$ is a Turing submachine designed to locate the left end of a block on the tape. It scans rightward until it encounters two consecutive zeros ($00$), which serve as an end marker, and halts on the rightmost of those two zeros. This machine is used as a building block in more complex Turing machine constructions for computability theory, specifically to help machines find the boundaries of encoded number blocks on the tape.
