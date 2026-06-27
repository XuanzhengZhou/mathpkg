---
role: proof
locale: en
of_concept: ba-duality-principle
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

Proof. This is immediate from the form of the axioms in Definition 9.3. Each axiom comes in a dual pair:

(i) Commutativity: $x + y = y + x$ and $x \cdot y = y \cdot x$ are dual to each other.

(ii) Associativity: $x + (y + z) = (x + y) + z$ and $x \cdot (y \cdot z) = (x \cdot y) \cdot z$ are dual.

(iii) Absorption: $x \cdot y + y = y$ and $(x + y) \cdot y = y$ are dual.

(iv) Distributivity: $x \cdot (y + z) = x \cdot y + x \cdot z$ and $x + y \cdot z = (x + y) \cdot (x + z)$ are dual (each distributes over the other).

(v) Complementation: $x \cdot -x = 0$ and $x + -x = 1$ are dual, with $0$ and $1$ interchanged.

Since every axiom is paired with its dual, interchanging $+$ with $\cdot$ and $0$ with $1$ throughout the structure $\langle A, +, \cdot, -, 0, 1 \rangle$ yields another structure $\langle A, \cdot, +, -, 1, 0 \rangle$ that satisfies all the axioms. Therefore it is also a Boolean algebra.
