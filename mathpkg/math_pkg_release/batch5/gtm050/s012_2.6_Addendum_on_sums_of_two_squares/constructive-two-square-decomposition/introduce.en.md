---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Euler's classical proof that every prime $p \equiv 1 \pmod{4}$ is a sum of two squares uses infinite descent and is non-constructive. However, a careful examination of the proof reveals that it can be modified to yield a fully constructive algorithm. The key insight is that Step (5) of Euler's proof, which shows that one of the numbers $1^{2n} + 2^{2n}, 2^{2n} + 3^{2n}, \ldots$ is divisible by $p$, can be used to find an explicit representation of $kp$ as $a^2 + b^2$ and then successively reduce the multiplier $k$.
