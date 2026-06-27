---
role: proof
locale: en
of_concept: radical-ideal-algebraic-set-correspondence
source_book: gtm052
source_chapter: "I"
source_section: "§1"
---
The bijection follows from Hilbert's Nullstellensatz (Theorem 1.3A), which implies $I(Z(\mathfrak{a})) = \sqrt{\mathfrak{a}}$ for any ideal $\mathfrak{a}$.

For the second statement: If $Y$ is irreducible, we show that $I(Y)$ is prime. Indeed, if $fg \in I(Y)$, then $Y \subseteq Z(fg) = Z(f) \cup Z(g)$. Thus $Y = (Y \cap Z(f)) \cup (Y \cap Z(g))$, both being closed subsets of $Y$. Since $Y$ is irreducible, we have either $Y = Y \cap Z(f)$, in which case $Y \subseteq Z(f)$, or $Y \subseteq Z(g)$. Hence either $f \in I(Y)$ or $g \in I(Y)$.

Conversely, let $\mathfrak{p}$ be a prime ideal, and suppose that $Z(\mathfrak{p}) = Y_1 \cup Y_2$. Then $\mathfrak{p} = I(Z(\mathfrak{p})) = I(Y_1 \cup Y_2) = I(Y_1) \cap I(Y_2)$. Since $\mathfrak{p}$ is prime, either $\mathfrak{p} = I(Y_1)$ or $\mathfrak{p} = I(Y_2)$, so applying $Z$ gives $Z(\mathfrak{p}) = Y_1$ or $Z(\mathfrak{p}) = Y_2$. Thus $Z(\mathfrak{p})$ is irreducible.
