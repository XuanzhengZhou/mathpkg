---
role: proof
locale: en
of_concept: parity-in-cubic-fermat
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Assume $x, y, z$ are pairwise coprime positive integers satisfying $x^3 + y^3 = z^3$.

First, at most one of $x, y, z$ is even, because if two were even they would share the factor 2, contradicting pairwise coprimality.

Second, at least one of $x, y, z$ is even. Suppose $x$ and $y$ are both odd. Then $x^3 \equiv x \pmod{2}$ and $y^3 \equiv y \pmod{2}$, so $x^3 + y^3$ is even. Hence $z^3$ is even, which implies $z$ is even. The case where $x$ and $z$ are both odd (forcing $y$ even) and the case where $y$ and $z$ are both odd (forcing $x$ even) are symmetric.

Therefore exactly one of $x, y, z$ is even.
