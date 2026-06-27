---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The constructive method for decomposing a prime $p \equiv 1 \pmod{3}$ as $a^2 + 3b^2$ is exactly analogous to the algorithm for the sum of two squares. It begins by finding an integer $c$ such that $p$ divides $c^{3n} - (c-1)^{3n}$, which is guaranteed to exist. From this, one derives a congruence that yields an initial representation of a multiple $kp$ in the form $a^2 + 3b^2$, and then reduces the multiplier $k$ by exploiting the multiplicative structure of the quadratic form $x^2 + 3y^2$.
