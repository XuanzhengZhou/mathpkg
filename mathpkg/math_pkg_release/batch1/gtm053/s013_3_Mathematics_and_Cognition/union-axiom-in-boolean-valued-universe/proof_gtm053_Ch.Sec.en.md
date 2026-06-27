---
role: proof
locale: en
of_concept: union-axiom-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

Fix $X \in V^B$ and construct $Y$ as a random class by
$$\|U \in Y\| = \bigvee_{Z \in V^B} \|U \in Z\| \wedge \|Z \in X\|.$$
By Proposition 6.4, this defines a random class. To show $Y$ is equivalent to a random set, let $D(X) = V_\alpha^B$. One shows $Y \sim Y_\alpha$ by noting that for any $Z_1$,
$$\|Z_1 \in X\| = \bigvee_{Z_2 \in D(X)} \|Z_1 = Z_2\| \wedge \|Z_2 \in X\|,$$
which allows restricting the sum over $Z$ to $D(X)$.
