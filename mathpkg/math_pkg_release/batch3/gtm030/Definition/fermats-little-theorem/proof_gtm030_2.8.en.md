---
role: proof
locale: en
of_concept: fermats-little-theorem
source_book: gtm030
source_chapter: "2"
source_section: "8"
---

The proof follows from the Euler-Fermat theorem. The set of residue classes modulo $p$ that are not divisible by $p$ forms the multiplicative group of the finite field $\mathbb{Z}/p\mathbb{Z}$, which has order $p-1$. By Lagrange's theorem, the order of any element $a$ in this group divides $p-1$, hence $a^{p-1} \equiv 1 \pmod{p}$. Alternatively, multiplying each nonzero residue $1, 2, \ldots, p-1$ by $a$ permutes them modulo $p$, so their products satisfy $a^{p-1}(p-1)! \equiv (p-1)! \pmod{p}$. Since $(p-1)!$ is coprime to $p$, we conclude $a^{p-1} \equiv 1 \pmod{p}$.
