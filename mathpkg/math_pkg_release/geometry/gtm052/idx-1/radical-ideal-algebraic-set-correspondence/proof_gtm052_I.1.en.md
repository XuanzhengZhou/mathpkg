---
role: proof
locale: en
of_concept: radical-ideal-algebraic-set-correspondence
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

The first part (the one-to-one correspondence) follows directly from Hilbert's Nullstellensatz (Theorem 1.3A) together with properties (d) and (e) of Proposition 1.2. Specifically, for any algebraic set $Y$, we have $Z(I(Y)) = \overline{Y} = Y$, and for any ideal $\mathfrak{a}$, we have $I(Z(\mathfrak{a})) = \sqrt{\mathfrak{a}}$. Thus $Z$ and $I$ restrict to mutually inverse bijections between algebraic sets and radical ideals.

For the second part: If $Y$ is irreducible, we show that $I(Y)$ is prime. Suppose $fg \in I(Y)$. Then $f(P)g(P) = 0$ for all $P \in Y$, so $Y \subseteq Z(fg) = Z(f) \cup Z(g)$. Hence $Y = (Y \cap Z(f)) \cup (Y \cap Z(g))$, both being closed subsets of $Y$. Since $Y$ is irreducible, either $Y = Y \cap Z(f)$, giving $Y \subseteq Z(f)$ and $f \in I(Y)$, or $Y \subseteq Z(g)$ and $g \in I(Y)$. Thus $I(Y)$ is prime.

Conversely, let $\mathfrak{p}$ be a prime ideal and suppose $Z(\mathfrak{p}) = Y_1 \cup Y_2$ for closed subsets $Y_1, Y_2$. Then $\mathfrak{p} = I(Z(\mathfrak{p})) = I(Y_1 \cup Y_2) = I(Y_1) \cap I(Y_2)$ by Proposition 1.2(c). Since $\mathfrak{p}$ is prime, $\mathfrak{p} = I(Y_1)$ or $\mathfrak{p} = I(Y_2)$. Hence $Z(\mathfrak{p}) = Z(I(Y_1)) = Y_1$ or $Z(\mathfrak{p}) = Y_2$, proving $Z(\mathfrak{p})$ is irreducible.
