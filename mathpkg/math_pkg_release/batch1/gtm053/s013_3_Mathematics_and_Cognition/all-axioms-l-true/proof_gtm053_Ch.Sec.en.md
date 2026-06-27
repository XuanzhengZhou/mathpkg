---
role: proof
locale: en
of_concept: all-axioms-l-true
source_book: gtm053
source_chapter: "IV"
source_section: "3"
---

The verification goes axiom by axiom:
- Extensionality: follows from transitivity of $L$.
- Infinity: $\omega_0 \in L$ since $L_n = V_n$ for $n \leqslant \omega_0$ (property 1.3).
- Pairing: $L$ is closed with respect to forming pairs.
- Regularity: follows by direct computation using transitivity.
- Union: for $X \in L$, take $Y = \bigcup_{Z \in X} Z$ and use Proposition 2.3.
- Power set: similar to union, using $\Sigma_0$-absoluteness.
- Replacement: the most involved verification, using $\Sigma_0$-absoluteness and Proposition 2.3.
- Choice: verified separately in Proposition 3.1(ii) using the numbering $N$.
