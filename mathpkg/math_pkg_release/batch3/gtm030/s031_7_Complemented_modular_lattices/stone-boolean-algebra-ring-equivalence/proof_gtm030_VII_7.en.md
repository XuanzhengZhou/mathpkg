---
role: proof
locale: en
of_concept: stone-boolean-algebra-ring-equivalence
source_book: gtm030
source_chapter: "VII"
source_section: "7. Complemented modular lattices"
---

**Part 1: Boolean algebra $\Rightarrow$ Boolean ring.** Let $B$ be a Boolean algebra. Define $a + b = (a \cap b') \cup (a' \cap b)$ and $a \cdot b = a \cap b$. We verify the ring axioms.

Evidently $+$ is commutative. For associativity, we note that
$$(a + b)' = (a \cap b) \cup (a' \cap b').$$
Then
\begin{align*}
(a + b) + c &= [((a \cap b') \cup (a' \cap b)) \cap c'] \cup [((a \cap b) \cup (a' \cap b')) \cap c] \\
&= (a \cap b' \cap c') \cup (a' \cap b \cap c') \cup (a \cap b \cap c) \cup (a' \cap b' \cap c).
\end{align*}
This expression is symmetric in $a, b, c$, so $(a+b)+c = (c+b)+a$. By commutativity, associativity follows.

The additive identity is $0$, since $a + 0 = (a \cap 1) \cup (a' \cap 0) = a$. Each element is its own inverse: $a + a = (a \cap a') \cup (a' \cap a) = 0$. Hence $(B, +)$ is a commutative group.

Multiplication $\cdot$ (i.e., $\cap$) is associative, commutative, and has identity $1$. The distributive law:
\begin{align*}
(a + b)c &= ((a \cap b') \cup (a' \cap b)) \cap c \\
&= (a \cap b' \cap c) \cup (a' \cap b \cap c) = ac + bc.
\end{align*}
Thus $(B, +, \cdot)$ is a commutative ring with identity. Every element is idempotent since $a \cdot a = a \cap a = a$. Hence it is a Boolean ring with identity.

**Part 2: Boolean ring $\Rightarrow$ Boolean algebra.** Let $\mathfrak{B}$ be a Boolean ring with identity. Define $a \cup b = a + b - ab$, $a \cap b = ab$, and $a' = 1 - a$.

We have seen in Chapter II (circle composition) that $\cup$ is associative. The lattice axioms $\mathrm{L}_1-\mathrm{L}_4$ are immediate from our assumptions and the commutativity of $\mathfrak{B}$ (which follows from idempotence: $a^2 = a$ for all $a$ implies $2a = 0$ and $ab = ba$).

The lattice is distributive since
$$(a \cup b) \cap c = (a + b - ab)c = ac + bc - abc = ac + bc - acbc = (a \cap c) \cup (b \cap c).$$
Also $a \cup a' = a + (1-a) - a(1-a) = a + 1 - a - (a - a^2) = 1$, and $a \cap a' = a(1-a) = a - a^2 = 0$. Thus $\mathfrak{B}$ is a complemented distributive lattice, i.e., a Boolean algebra.

**Part 3: The constructions are inverse.** Starting from a Boolean algebra $B$, forming the ring, then converting back to a Boolean algebra via the second process gives compositions $a \bigcup b = a + b - ab$ and $a \bigcap b = ab = a \cap b$. Since $1 - a = 1 + a = (1 \cap a') \cup (1' \cap a) = a'$,
$$a \bigcup b = a + b - ab = 1 - (1-a)(1-b) = (a' \cap b')' = a \cup b.$$
Thus the compositions $\bigcup$, $\bigcap$ coincide with the original $\cup$, $\cap$.

Conversely, starting with a Boolean ring with $1$ and defining the Boolean algebra operations, then converting back via the first process, $a' = 1 - a$ and
\begin{align*}
a \oplus b &= (a \cap (1-b)) \cup ((1-a) \cap b) = a(1-b) \cup (1-a)b \\
&= (a - ab) \cup (b - ab) \\
&= a - ab + b - ab - (a-ab)(b-ab) \\
&= a - ab + b - ab - ab + ab - ab = a + b.
\end{align*}
Hence $\oplus$ coincides with $+$, and $\odot$ with $\cdot$. This completes the proof that the two types of abstract systems are equivalent.
