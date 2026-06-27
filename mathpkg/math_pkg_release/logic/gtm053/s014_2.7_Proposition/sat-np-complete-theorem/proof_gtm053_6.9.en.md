---
role: proof
locale: en
of_concept: sat-np-complete-theorem
source_book: gtm053
source_chapter: "6"
source_section: "6.9"
---
Let $D \in \text{NP}$, $D \subset A$, where $A$ is some constructive world. Represent $D$ as a polynomially truncated projection of some set $D' \subset A \times B$, $D' \in \text{P}$. Choose a normal (Turing) model of computation and consider the Turing protocols of computation of $\chi_{D'}(a,b)$ with fixed $a$ and variable polynomially bounded $b$.

For a given $a$, any such protocol can be imagined as a table of a fixed polynomially bounded size whose rows are the consecutive states of the computation. In the microscopic description, positions in this table can be filled only by 0 or 1. Each row is supplied with the specification of the position and inner state of the head/processor.

Some arrangements are valid protocols, others are not, but the condition of being a valid protocol accepting the input is expressible as a Boolean formula in the bits of the table entries. This gives a polynomial-time reduction from any NP problem to SAT. Combined with Proposition 6.8 (SAT $\in$ NP), this proves SAT is NP-complete.
