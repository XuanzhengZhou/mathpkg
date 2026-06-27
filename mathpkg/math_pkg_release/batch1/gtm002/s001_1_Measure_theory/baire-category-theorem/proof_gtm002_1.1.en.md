---
role: proof
locale: en
of_concept: baire-category-theorem
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
The proof of the Baire category theorem on the line is not given explicitly in this section; it is deferred to Chapter 9 where the general theorem for complete metric spaces is proved. For the line, one can argue as follows: let $A = \bigcup_n A_n$ be of first category, with each $A_n$ nowhere dense. Given any open interval $I$, since $A_1$ is nowhere dense, there exists a closed interval $I_1 \subset I \setminus A_1$. Since $A_2$ is nowhere dense, there exists a closed interval $I_2 \subset I_1 \setminus A_2$, and so on. The nested intervals $I_n$ have a nonempty intersection, and any point in $\bigcap I_n$ belongs to $I$ but not to $A$. Hence the complement of $A$ is dense. Consequently, no interval can be covered by a countable union of nowhere dense sets, i.e., no interval is of first category.
