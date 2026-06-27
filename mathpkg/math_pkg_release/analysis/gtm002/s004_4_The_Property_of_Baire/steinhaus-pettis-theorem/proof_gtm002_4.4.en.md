---
role: proof
locale: en
of_concept: steinhaus-pettis-theorem
source_book: gtm002
source_chapter: "4"
source_section: "4. The Property of Baire"
---

(The proof in the source text was truncated during OCR extraction. The following outlines the standard argument.)

For the measure case: if $m(A) > 0$, then by Lebesgue density theorem or by regularity of Lebesgue measure, there exists an interval $I$ such that $m(A \cap I) > \frac{3}{4}m(I)$. For $|x| < m(I)/2$, one can show that $(x + A) \cap A \neq \emptyset$ by noting that $A \cap I$ and $x + (A \cap I)$ cannot be disjoint within $I \cup (x + I)$.

For the category case: if $A$ has the property of Baire and is of second category, write $A = G \triangle P$ with $G$ regular open and non-empty. Since $G$ is non-empty open, for sufficiently small $x$, $(x + G) \cap G$ contains a non-empty open set, and the first-category perturbation $P$ does not affect the conclusion that $(x + A) \cap A$ contains an interval.
