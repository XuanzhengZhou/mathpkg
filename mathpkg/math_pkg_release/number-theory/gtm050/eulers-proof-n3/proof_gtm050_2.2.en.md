---
role: proof
locale: en
of_concept: eulers-proof-n3
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Assume $x^3 + y^3 = z^3$ with $x,y,z$ pairwise relatively prime positive integers. Exactly one is even; consider two cases.

**Case 1:** $z$ even, $x,y$ odd. Set $x = p+q$, $y = p-q$ where $p,q$ are positive integers, one even one odd, relatively prime. Then $x^3 + y^3 = (p+q)^3 + (p-q)^3 = 2p(p^2 + 3q^2)$. Since $x^3 + y^3 = z^3$ and $z$ is even, $2p(p^2 + 3q^2)$ is a cube.

Now $2p$ and $p^2 + 3q^2$ are relatively prime (any common divisor would divide both $p$ and $q$). Hence each must be a cube. Using the arithmetic of numbers $a + b\sqrt{-3}$, one shows that if $p^2 + 3q^2$ is a cube, then $p + q\sqrt{-3} = (a + b\sqrt{-3})^3$ for some integers $a,b$. Expanding gives $p = a^3 - 9ab^2$, $q = 3a^2b - 3b^3 = 3b(a^2 - b^2)$.

Since $2p$ is also a cube and $p$ is given by the above, one obtains a new, smaller triple $(x',y',z')$ satisfying $x'^3 + y'^3 = z'^3$. Infinite descent completes the proof.

**Case 2:** $x$ or $y$ even. By symmetry, the same argument applies after relabeling.
