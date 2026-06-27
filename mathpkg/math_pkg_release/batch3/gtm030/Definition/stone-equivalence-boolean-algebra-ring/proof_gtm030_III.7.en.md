---
role: proof
locale: en
of_concept: stone-equivalence-boolean-algebra-ring
source_book: gtm030
source_chapter: "III"
source_section: "7"
---

**From Boolean algebra to Boolean ring:** Given a Boolean algebra $B$, define
$$a + b = (a \cap b') \cup (a' \cap b)$$
and $ab = a \cap b$. Then $+$ is commutative. Associativity follows from the symmetry of
$$(a + b) + c = (a \cap b' \cap c') \cup (a' \cap b \cap c') \cup (a \cap b \cap c) \cup (a' \cap b' \cap c)$$
in $a, b, c$. We have $a + 0 = (a \cap 1) \cup (a' \cap 0) = a$ and $a + a = (a \cap a') \cup (a' \cap a) = 0$, so $B$ is a commutative group under $+$. The distributive law $(a + b)c = ac + bc$ follows by expansion. The ring is commutative (since $\cap$ is), has identity $1$, and every element is idempotent ($a^2 = a \cap a = a$).

**From Boolean ring to Boolean algebra:** Given a Boolean ring $\mathfrak{B}$ with identity, define $a \cup b = a + b - ab$ and $a \cap b = ab$. From $a^2 = a$ for all $a$, one deduces $2a = 0$ (hence $a = -a$) and $ab = ba$ by expanding $(a + b)^2 = a + b$. The operations $\cup$ and $\cap$ satisfy the lattice axioms; distributivity is verified as
$$(a \cup b) \cap c = (a + b - ab)c = ac + bc - abc = ac + bc - acbc = (a \cap c) \cup (b \cap c).$$
The complement is $a' = 1 - a = 1 + a$.

**Roundtrip consistency:** Starting from a Boolean algebra, converting to a ring and back recovers the original operations: $a \bigcup b = a + b - ab = 1 - (1 - a)(1 - b) = (a' \cap b')' = a \cup b$, and $a \bigcap b = ab = a \cap b$. Starting from a Boolean ring and converting to a Boolean algebra and back yields $a \oplus b = a + b$ and $a \odot b = a \cdot b$, where the verification uses $a' = 1 - a$. Hence the two categories are equivalent.
