---
role: proof
locale: en
of_concept: natural-number-induction-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by induction on $n \in \omega$.

**Base case $n = 0$.** We need to show $[\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!] \leq [\![\check{0} \in a]\!]$. This follows immediately since $[\![0 \in a]\!] = [\![\check{0} \in a]\!]$ by Example 1 ($[\![0 = \check{0}]\!] = 1$).

**Inductive step.** Assume the statement holds for $n$, i.e.,
$$[\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!] \leq [\![\check{n} \in a]\!].$$

Then:
$$[\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!]$$
$$\leq [\![0 \in a \land (\forall x \in a)[x + 1 \in a]]\!] \cdot [\![\check{n} \in a]\!]$$
by the induction hypothesis
$$\leq [\![(\forall x \in a)[x + 1 \in a]]\!] \cdot [\![\check{n} \in a]\!]$$
$$\leq [\![\check{n} + 1 \in a]\!]$$
by instantiating the universal quantifier with $x = \check{n}$
$$= [\![(\widehat{n + 1}) \in a]\!]$$
by Example 2.

Thus the statement holds for $n + 1$, completing the induction.
