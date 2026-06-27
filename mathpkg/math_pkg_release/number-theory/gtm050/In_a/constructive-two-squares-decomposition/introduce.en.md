---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition describes the constructive algorithm for writing a prime $p \equiv 1 \pmod{4}$ as a sum of two squares. Unlike Euler's original indirect proof by infinite descent (which merely shows existence by contradiction), this constructive version actively produces the integers $a$ and $b$ satisfying $p = a^{2} + b^{2}$. The method starts by finding a multiple $kp = c^{2} + d^{2}$ using the fact that $-1$ is a quadratic residue modulo $p$, then iteratively reduces the multiplier $k$ using the Brahmagupta--Fibonacci identity $(x^{2}+y^{2})(u^{2}+v^{2}) = (xu \pm yv)^{2} + (xv \mp yu)^{2}$ until $k = 1$.
