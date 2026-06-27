---
role: proof
locale: en
of_concept: fermats-little-theorem
source_book: gtm030
source_chapter: "II"
source_section: "9"
---

This is a corollary of the Euler-Fermat theorem. Since the proof appears in context of Chapter II Section 9 (Homomorphism of rings), the result can be proved using group theory: the multiplicative group of nonzero residue classes modulo a prime $p$ has order $p-1$, so by Lagrange's theorem every element has order dividing $p-1$, hence $a^{p-1} \equiv 1 \pmod{p}$ for $a \not\equiv 0 \pmod{p}$. The two formulations are equivalent: if $a^p \equiv a \pmod{p}$ and $a \not\equiv 0 \pmod{p}$, then dividing by $a$ gives $a^{p-1} \equiv 1 \pmod{p}$. Conversely, if $a^{p-1} \equiv 1 \pmod{p}$ for $a \not\equiv 0 \pmod{p}$, then $a^p \equiv a \pmod{p}$ (trivially true for $a$ divisible by $p$).
