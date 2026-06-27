---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition asserts that every prime $p \equiv 1 \pmod{3}$ can be expressed as $a^{2} + 3b^{2}$ for some integers $a, b$. It is the natural analogue of Fermat's theorem on sums of two squares for the quadratic form $x^{2} + 3y^{2}$. The proof follows the same constructive descent strategy: one first finds an integer $c$ such that $c^{3} \equiv 1 \pmod{p}$ (using the fact that the multiplicative group modulo $p$ is cyclic of order $3n$), and then $p$ divides $c^{2n} + c^{n}(c-1)^{n} + (c-1)^{2n}$. From this a multiple $kp = A^{2} + 3B^{2}$ is obtained, and the multiplier $k$ is reduced iteratively using the composition identity for the form $x^{2} + 3y^{2}$.
