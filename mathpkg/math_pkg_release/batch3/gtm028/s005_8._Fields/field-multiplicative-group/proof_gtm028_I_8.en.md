---
role: proof
locale: en
of_concept: field-multiplicative-group
source_book: gtm028
source_chapter: "I"
source_section: "8. Fields"
---

If $F$ satisfies $F_1$, $F_2$, $F_3$, then the set $F^* = F \setminus \{0\}$ is nonempty (by $F_1$), contains the identity 1 (by $F_2$), is closed under multiplication (since the product of two nonzero elements cannot be zero in a ring with identity, otherwise a nonzero element would be a zero divisor, contradicting the existence of inverses), and every element has a multiplicative inverse (by $F_3$). Associativity of multiplication in $F^*$ follows from associativity in $F$. Thus $F^*$ is a group under multiplication.

Conversely, if $F^* = F \setminus \{0\}$ forms a group under multiplication, then $F^*$ is nonempty, so $F$ has at least two elements (the identity of $F^*$ plus 0), giving $F_1$. The identity of the group $F^*$ serves as the identity of $F$, giving $F_2$. Every element of $F^*$ has an inverse by the group property, giving $F_3$.
