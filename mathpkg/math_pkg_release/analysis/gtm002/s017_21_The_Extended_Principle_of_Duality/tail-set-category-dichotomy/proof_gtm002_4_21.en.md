---
role: proof
locale: en
of_concept: tail-set-category-dichotomy
source_book: gtm002
source_chapter: "4"
source_section: "21. The Extended Principle of Duality"
---

Suppose that $E$ is not residual. Then $X - E$ is of the form $G \triangle P$, where $G$ is open and non-empty and $P$ is of first category. (This is the characterization of sets with the Baire property: every such set can be written as the symmetric difference of an open set and a first category set.)

$G$ is a countable union of basic open sets of the form $U = A_n \times Y^n$ (corresponding to the closed intervals used to define the Cantor set). Hence $G$ contains a set $U$ of the form $U = A_n \times Y^n$, where $A_n$ is a non-empty subset of the finite discrete space $X^n = \prod_{i=1}^n X_i$.

By hypothesis, $E$ is a tail set, so it can be written in the form $E = X^n \times B_n$ for some $B_n \subset Y^n = \prod_{i=n+1}^\infty X_i$. Hence

$$U \cap E = A_n \times B_n.$$

But also,

$$A_n \times B_n \subset U \subset G \subset (X - E) \cup P.$$

Therefore

$$A_n \times B_n = (A_n \times B_n) \cap ((X - E) \cup P) = [(A_n \times B_n) \cap (X - E)] \cup [(A_n \times B_n) \cap P].$$

Since $E \cap (X - E) = \emptyset$ (as $E$ is a tail set), the first term is contained in the complement of a tail set intersected with the tail set, which is empty. More precisely, since $E = X^n \times B_n$ and $U \subset X - E$ (up to a first category set), we have

$$A_n \times B_n \subset E \cap ((X - E) \cup P) \subset P.$$

Therefore $A_n \times B_n$ is of first category. Since $A_n$ is a non-empty subset of the finite discrete space $X^n$, it is of second category. It follows from Theorem 15.3 (the Kuratowski-Ulam theorem for category) that $B_n$ is of first category in $Y^n$. Hence $E = X^n \times B_n$ is of first category in $X$.

Thus, if $E$ is not residual, it must be of first category. The theorem holds for the product of any family of Baire spaces each of which has a countable base.
