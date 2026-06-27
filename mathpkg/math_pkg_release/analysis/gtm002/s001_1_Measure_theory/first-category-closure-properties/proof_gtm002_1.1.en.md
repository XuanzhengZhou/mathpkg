---
role: proof
locale: en
of_concept: first-category-closure-properties
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
\textbf{(1)} If $B \subset A$ and $A = \bigcup_{n} A_n$ with each $A_n$ nowhere dense, then $B = \bigcup_n (B \cap A_n)$. Since each $B \cap A_n$ is a subset of a nowhere dense set, it is nowhere dense (by Theorem 1.2). Hence $B$ is a countable union of nowhere dense sets, i.e., of first category.

\textbf{(2)} If $A_i = \bigcup_n A_{i,n}$ is of first category for each $i = 1, 2, \dots$, then $\bigcup_i A_i = \bigcup_{i,n} A_{i,n}$ is a countable union of nowhere dense sets, hence of first category.

\textbf{Remark on closure:} The closure of a first category set may not be first category. If $\overline{A}$ is of first category, write $\overline{A} = \bigcup_n A_n$ with $A_n$ nowhere dense. Then $A \subset \overline{A}$ and each $A_n$ is nowhere dense. For $A$ not to be nowhere dense, some interval would have to be contained in $\overline{A}$ without being covered by any $A_n$, which is possible. Conversely, if $A$ is nowhere dense, then $\overline{A}$ is nowhere dense (Theorem 1.2) and hence of first category.
