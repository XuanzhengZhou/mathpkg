---
role: proof
locale: en
of_concept: matrix-inequalities-preserved-multiplication
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

The proof is left to the reader in the text. The argument follows from the entrywise definition of matrix multiplication.

For $A \geq B$ and non-negative multiplier $M \geq 0$: each entry of $MA$ is $\sum_{m} M_{im} A_{mj} \geq \sum_{m} M_{im} B_{mj}$, which is the corresponding entry of $MB$, since $M_{im} \geq 0$ and $A_{mj} \geq B_{mj}$ for all indices.

For strict inequality $A > B$ and positive multiplier $M > 0$: the same argument holds with strict inequality, provided the sums are finite (ensuring no indeterminate cancellations or infinite values that would break the strictness).
