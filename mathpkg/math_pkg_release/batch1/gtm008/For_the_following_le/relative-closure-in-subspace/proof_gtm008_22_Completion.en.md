---
role: proof
locale: en
of_concept: relative-closure-in-subspace
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

**1.** Let $A \subseteq S$. Then obviously
$$A^{-S} \subseteq A^{-} \cap S.$$

Conversely, let $p \in A^{-} \cap S$. Then
$$p \in S \land (\forall N(p))[N(p) \cap A \neq 0],$$
where $N(p)$ ranges over open neighborhoods of $p$ in $X$. Since $A \subseteq S$, we have
$$(\forall N(p))[N(p) \cap S \cap A \neq 0].$$

Thus for every relative neighborhood $N^S(p)$ (which is of the form $N(p) \cap S$),
$$(\forall N^S(p))[N^S(p) \cap A \neq 0],$$
i.e., $p \in A^{-S}$.

**2.** Follows from 1.
