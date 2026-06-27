---
role: proof
locale: en
of_concept: quotient-category
source_book: gtm005
source_chapter: "I"
source_section: "8"
---
Call $R$ a \textbf{congruence} on $C$ if: (i) each $R_{a,b}$ is an equivalence relation; (ii) if $f R_{a,b} f'$, then for all $g: a' \rightarrow a$ and $h: b \rightarrow b'$, one has $(h f g) R_{a',b'} (h f' g)$. Given any $R$, take the least congruence $R'$ containing $R$. Define the objects of $C/R$ to be those of $C$, and $\hom_{C/R}(a,b) = \hom_C(a,b)/R'_{a,b}$. Because $R'$ is a congruence, composition descends to the quotient, and the projection $Q: C \rightarrow C/R$ satisfies the universal property.