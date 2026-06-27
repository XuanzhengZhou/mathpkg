---
role: proof
locale: en
of_concept: sharp-operator-properties
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

Properties 1--4 follow directly from the definition of $\#$. (Note that $B_0$ and $B_1$ are complete, so all required infima and suprema exist, and $i$ is a complete monomorphism.)

**5.** By property 1, $i(b_0) \cdot b_1 \leq i(b_0 \cdot \#(b_1))$. Applying $\#$ and using properties 3 and 4,
$$\#(i(b_0) \cdot b_1) \leq \#(i(b_0 \cdot \#(b_1))) = b_0 \cdot \#(b_1).$$

Conversely, $b_0 \cdot \#(b_1) \leq \#(b_1)$, so $i(b_0 \cdot \#(b_1)) \leq i(\#(b_1))$. Combined with property 1, we have the reverse inequality, establishing the equality.

**6.** This follows directly from property 5: if $i(b_0) \cdot b_1 = 0$, then $\#(i(b_0) \cdot b_1) = \#(0) = 0$ (by property 2), so $b_0 \cdot \#(b_1) = 0$.
