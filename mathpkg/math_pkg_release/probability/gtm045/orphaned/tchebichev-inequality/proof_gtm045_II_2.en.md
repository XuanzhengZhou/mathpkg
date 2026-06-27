---
role: proof
locale: en
of_concept: tchebichev-inequality
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "2. Simple random variables"
---
The inequality follows from

$$EX^2 = E(X^2 I_{[|X| \geq \epsilon]}) + E(X^2 I_{[|X| < \epsilon]}) \geq E(X^2 I_{[|X| \geq \epsilon]}) \geq \epsilon^2 EI_{[|X| \geq \epsilon]} = \epsilon^2 P[|X| \geq \epsilon].$$

The first inequality holds because the second term is nonnegative. The second inequality holds because on the set $[|X| \geq \epsilon]$, we have $X^2 \geq \epsilon^2$.
