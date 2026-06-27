---
role: proof
locale: en
of_concept: sophie-germain-theorem-2n-plus-one-prime
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

Exactly the same argument as the proof for the case $n = 5$ proves this more general theorem. The proof proceeds by reformulating $x^n + y^n = z^n$ as $x^n + y^n + z^n = 0$ (moving all terms to one side, using the symmetry that $n$ is odd). One factors

$$-x^n = (y + z)(y^{n-1} - y^{n-2}z + y^{n-3}z^2 - \cdots + z^{n-1}).$$

Assuming $x, y, z$ are pairwise relatively prime (as a common factor can be divided out), the two factors on the right are relatively prime except possibly for the prime $n$. If they share a prime factor $p \neq n$, then from $y \equiv -z \pmod{p}$ one obtains that the second factor is congruent to $n y^{n-1} \pmod{p}$, forcing $p \mid y$, contradicting relative primality. Therefore either $n$ divides $x$ (which is the desired conclusion) or the two factors are relatively prime $n$-th powers.

The remainder of the argument uses the auxiliary prime $2n + 1$ (which is given to be prime) and the fact that the $n$-th powers modulo $2n + 1$ are severely restricted (only $0, \pm 1$ modulo $2n + 1$), leading to a contradiction unless one of $x, y, z$ is divisible by $n$. This completes the proof.
