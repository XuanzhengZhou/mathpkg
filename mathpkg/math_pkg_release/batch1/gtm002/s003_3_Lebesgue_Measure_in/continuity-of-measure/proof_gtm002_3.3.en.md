---
role: proof
locale: en
of_concept: continuity-of-measure
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

Write $A = \bigcup_{i=1}^{\infty} A_i$ where $A_i = A \cap (-i, i)^r$. The sets $A_i$ are increasing: $A_1 \subset A_2 \subset \cdots$. We can write $A$ as the disjoint union

$$
A = A_1 \cup \bigcup_{i=2}^{\infty} (A_i \setminus A_{i-1}).
$$

By countable additivity of Lebesgue measure on measurable sets (Lemma 3.13),

$$
m(A) = m(A_1) + \sum_{i=2}^{\infty} m(A_i \setminus A_{i-1})
     = m(A_1) + \sum_{i=2}^{\infty} \bigl(m(A_i) - m(A_{i-1})\bigr)
     = \lim_{n \to \infty} m(A_n).
$$

The general statement for any increasing sequence $B_i \uparrow B$ follows by the same decomposition argument using countable additivity.
