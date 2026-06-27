---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$T_0$ is a minimal one-state Turing machine that writes a $0$ on the current square and then halts. If the scanned square already contains $0$, the machine simply stops. Otherwise, it writes $0$ (erasing whatever was there) and then, remaining in state $0$, checks again -- at which point it finds $0$ and stops. Thus $T_0$ serves as a basic "erase" operation, ensuring the current square contains $0$ before halting.
