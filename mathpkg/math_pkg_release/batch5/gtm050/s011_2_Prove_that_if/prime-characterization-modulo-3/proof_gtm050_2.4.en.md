---
role: proof
locale: en
of_concept: prime-characterization-modulo-3
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

Any integer is congruent to 0, 1, or 2 modulo 3. Hence every prime $p \neq 3$ is either $3n+1$ or $3n+2$.

Suppose $p = 3n+2$ could be written as $a^2+3b^2$. If $3 \mid a$, then $a = 3a'$, so $a^2+3b^2 = 9a'^2+3b^2 = 3(3a'^2+b^2)$, which is divisible by 3. Since $p$ is prime, $p=3$, contradicting $p=3n+2 \neq 3$. Therefore $3 \nmid a$.

Now $a^2 \equiv 1 \pmod{3}$ (since the only nonzero square mod 3 is 1), and $3b^2 \equiv 0 \pmod{3}$, so $a^2+3b^2 \equiv 1 \pmod{3}$. But if $p = a^2+3b^2 = 3n+2$, then $a^2+3b^2 \equiv 2 \pmod{3}$, a contradiction. Hence no prime of the form $3n+2$ can be represented as $a^2+3b^2$.
