---
role: proof
locale: en
of_concept: euler-analogy-prime-factors-cube
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

For ordinary integers $A, B \in \mathbb{Z}$, the statement follows from the fundamental theorem of arithmetic (unique factorization into primes). If $AB = C^3$ and $\gcd(A, B) = 1$, then the prime factorization of $C^3$ partitions into the prime factors of $A$ and $B$ with no overlap. Since every exponent in $C^3$ is divisible by $3$, the exponents in $A$ and $B$ are each divisible by $3$ as well, so $A = a^3$ and $B = b^3$ for some integers $a, b$.

For surds in $\mathbb{Z}[\sqrt{-3}]$, the proof does not carry over automatically because unique factorization may fail in this ring. Euler's application was therefore a heuristic analogy, not a rigorous deduction. In the specific case $a = 1, c = 3$, the conclusion happens to be true — though with a proof quite different from the integer case — but for other values of $a$ and $c$ the statement can be false, as Euler himself observed.
