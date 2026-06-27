---
role: proof
locale: en
of_concept: semicolon-design-inequality-b6
source_book: gtm054
source_chapter: "IX"
source_section: "B"
---
The proof is by induction on $a$. Theorem A12 serves as the first step, with $a = 2$. For the induction hypothesis, we assume that the theorem is valid for all $(; a)$-designs where $a$ is some fixed integer at least 2 and no vertex is incident with every block.

For the inductive step, consider a $(; a+1)$-design $\Lambda$ with incidence matrix $M$. By considering the matrix $M$ and counting arguments, one establishes that $v \geq b$.

For part (b), assuming $b = v$ and $a \geq 3$, the incidence matrix $M$ must have exactly one $0$ in each row and each column. Then $M$ is an incidence matrix of the set system $(V, \mathcal{P}_{v-1}(V))$, which is a trivial design. We have already noted (A3) that $b = v$ for trivial designs.
