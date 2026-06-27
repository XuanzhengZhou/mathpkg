---
role: proof
locale: en
of_concept: maximal-ideal-is-closed
source_book: gtm003
source_chapter: "VI"
source_section: "1"
---

Every proper ideal is contained in a maximal proper ideal by Zorn's lemma (the union of a chain of proper ideals is proper, since a proper ideal cannot contain the unit). A maximal proper ideal $M$ is closed: if $\overline{M} = A$, then $\overline{M} \cap A^{(-1)} \neq \emptyset$ (since $A^{(-1)}$ is open and contains $e$), contradicting properness. Hence $\overline{M} = M$. For the quotient: the norm on $A/J$ is $\|q(x)\| = \inf_{j \in J} \|x + j\|$, and submultiplicativity follows from the ideal property. Completeness follows from closedness of $J$. When $A$ is unital with unit $e$, $q(e)$ is the unit of $A/J$ and $\|q(e)\| \leq 1$; if $\|q(e)\| < 1$, scaling arguments show $\|q(e)\| = 1$ must hold.
