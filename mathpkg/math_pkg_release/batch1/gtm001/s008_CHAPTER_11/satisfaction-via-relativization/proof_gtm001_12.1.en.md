---
role: proof
locale: en
of_concept: satisfaction-via-relativization
source_book: gtm001
source_chapter: "12"
source_section: "12.1"
---

Proved by induction on the number of logical symbols in $\varphi$. Base case: $[A \models a \in b] \leftrightarrow a \in A \wedge b \in A \wedge a \in b = [a \in b]^A$. Inductive steps for $\neg$, $\wedge$, and $\forall$ use the induction hypothesis and properties of the definitions. Transitivity of $A$ ensures that elements of elements remain in $A$.