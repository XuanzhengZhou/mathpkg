---
role: proof
locale: en
of_concept: iteration-theorem
source_book: gtm037
source_chapter: "5. Recursive Functions"
source_section: "5.1 Recursive Function Theory"
---

If $M$ is any Turing machine and $y_1, \ldots, y_m$ are given, we construct a Turing machine $M'$ that, on input $x_1, \ldots, x_n$, first writes $y_1, \ldots, y_m$ on the tape following the input, then simulates $M$ on the combined input $(x_1, \ldots, x_n, y_1, \ldots, y_m)$. The function $s_n^m(e, y_1, \ldots, y_m)$ is then defined as the Gödel number of $M'$, where $e$ is the Gödel number of $M$. This construction is effective (recursive) because the transformation from $M$ to $M'$ is a simple syntactic operation on Turing machine descriptions.
