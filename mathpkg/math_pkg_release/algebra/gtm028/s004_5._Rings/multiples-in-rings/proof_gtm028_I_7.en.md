---
role: proof
locale: en
of_concept: multiples-in-rings
source_book: gtm028
source_chapter: "I"
source_section: "7"
---

\text{We prove by induction on } n \geq 0. \text{ For } n = 0, \text{ the statement } 0(ab) = (0a)b = a(0b) \text{ reduces to } 0 = 0 = 0, \text{ which holds. For } n = 1, \text{ it is trivial.}

\text{Assuming the statement holds for } n, \text{ we have for } n+1:

$$(n+1)(ab) = n(ab) + ab = (na)b + ab = (na + a)b = ((n+1)a)b,$$

\text{using the inductive hypothesis and the right distributive law. Similarly,}

$$(n+1)(ab) = n(ab) + ab = a(nb) + ab = a(nb + b) = a((n+1)b),$$

\text{using the left distributive law. The case for negative } n \text{ follows from the positive case and the property } (-n)(ab) = -(n(ab)).
