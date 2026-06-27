---
role: proof
locale: en
of_concept: collecting-gluing-random-sets
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

The functions $X$ and $Z$ are verified to be extensional. There exists an ordinal $\alpha$ such that $X_i \in V_\alpha^B$ for all $i$. One shows $X \sim X_\alpha$ and $Z \sim Z_\alpha$ using the recursive definition of membership:
$$\|Y \in X_\alpha\| = \bigvee_{U \in V_\alpha^B} \|Y = U\| \wedge \|U \in X_\alpha\|$$
and the fact that $\|U \in X_i\| = \bigvee_{U' \in V_\alpha^B} \|U = U'\| \wedge \|U' \in X_i\|$, which implies $a_i \wedge \|U \in X_i\| \leqslant \|U \in X_\alpha\|$.
