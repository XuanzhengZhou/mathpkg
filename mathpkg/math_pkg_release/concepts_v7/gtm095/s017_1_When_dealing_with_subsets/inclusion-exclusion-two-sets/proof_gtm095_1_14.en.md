---
role: proof
locale: en
of_concept: inclusion-exclusion-two-sets
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of Inclusion–Exclusion Principle for Two Sets

Let $\Omega$ be a finite set and $A, B \subseteq \Omega$. Denote by $N(D)$ the number of elements (cardinality) of a finite set $D$.

Consider the union $A \cup B$. By definition, every element $\omega \in A \cup B$ belongs to $A$ or to $B$ (or to both). If we simply sum $N(A) + N(B)$, then each element that lies in the intersection $AB = A \cap B$ is counted twice—once as a member of $A$ and once as a member of $B$. Therefore, to obtain the correct count of $A \cup B$, we must subtract the doubly counted elements:

$$N(A \cup B) = N(A) + N(B) - N(AB).$$

This is the **inclusion–exclusion formula for two sets**. The term $N(A) + N(B)$ corresponds to "inclusion" of the two sets, and the term $-N(AB)$ corresponds to "exclusion" of their intersection.

The same reasoning can be visualized using a **Venn diagram**: $N(A)$ counts the left circle, $N(B)$ counts the right circle, and $N(AB)$ is the overlapping region, which is counted twice in $N(A) + N(B)$ and must be subtracted once.

Using De Morgan's laws $\overline{A \cup B} = \overline{A} \cap \overline{B}$ and $\overline{A \cap B} = \overline{A} \cup \overline{B}$, one also obtains the complementary formula:

$$N(\overline{A} \, \overline{B}) = N(\Omega) - [N(A) + N(B)] + N(AB),$$

where $\overline{A} \, \overline{B} = \overline{A} \cap \overline{B}$ is the set of elements belonging to neither $A$ nor $B$.
