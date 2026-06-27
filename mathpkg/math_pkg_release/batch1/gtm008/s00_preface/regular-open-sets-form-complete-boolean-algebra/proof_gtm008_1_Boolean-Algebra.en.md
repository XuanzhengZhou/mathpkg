---
role: proof
locale: en
of_concept: regular-open-sets-form-complete-boolean-algebra
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** The operations are well-defined: if $A$ is regular open, then $(-A)^{-0} = (X - A^-)^{-0} = (X - A^{-0})^0 = (-A)$, so complementation maps regular open sets to regular open sets. By Theorem 1.29, multiplication (intersection) of regular open sets is regular open. Both $\emptyset$ and $X$ are regular open.

The Boolean algebra axioms are verified: commutativity of addition follows from commutativity of union; associativity of addition uses $(A + B) + C = [(A \cup B) \cup C]^{-0} = [(B \cup C) \cup A]^{-0} = (B + C) + A = A + (B + C)$. Multiplication (intersection) is associative. The distributive laws are verified using Theorems 1.27 and 1.28. Identity and complementation laws are checked directly.

For completeness, if $H \subseteq F$ (a collection of regular open sets), then $\sum_{A \in H} A = [\bigcup(H)]^{-0}$ and $\prod_{A \in H} A = [\bigcap(H)]^{-0}$ provide the required supremum and infimum.
