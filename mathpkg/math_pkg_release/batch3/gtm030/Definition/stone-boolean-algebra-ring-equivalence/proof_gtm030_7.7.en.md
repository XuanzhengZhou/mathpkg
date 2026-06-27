---
role: proof
locale: en
of_concept: stone-boolean-algebra-ring-equivalence
source_book: gtm030
source_chapter: "7"
source_section: "7"
---

**From Boolean algebra to Boolean ring:** Given a Boolean algebra $B$, define addition as symmetric difference $a + b = (a \cap b') \cup (a' \cap b)$ and multiplication as $ab = a \cap b$. One verifies that $(B, +, \cdot)$ is a commutative ring with identity $1$, and $a^2 = a \cap a = a$ for all $a$, so it is a Boolean ring.

**From Boolean ring to Boolean algebra:** Given a Boolean ring $\mathfrak{B}$ with identity, define $a \cup b = a + b - ab$ and $a \cap b = ab$. Since $a^2 = a$ for all $a$, we have $2a = 0$ (set $a = b$ in $a + b + ab + ba = a + b$, which follows from $(a+b)^2 = a+b$) and commutativity $ab = ba$. Then $\cup$ is associative (the circle composition), and the lattice axioms hold. Distributivity follows since $(a \cup b) \cap c = (a+b-ab)c = ac+bc-abc = (a \cap c) \cup (b \cap c)$. The complement is $a' = 1 - a = 1 + a$.

**Inverse constructions:** If one starts with a Boolean algebra, forms the Boolean ring, and then constructs the lattice operations from the ring, one recovers $\bigcup = \cup$ and $\bigcap = \cap$. Conversely, starting with a Boolean ring, forming the algebra, and then reconstructing the ring operations via symmetric difference, one recovers $\oplus = +$ and $\odot = \cdot$. Thus the two systems are equivalent.
