---
role: proof
locale: en
of_concept: pairing-axiom-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

For fixed $U, W \in V^B$, choose any $\alpha$ such that $U, W \in V_\alpha^B$. Then $X_\alpha \in V_{\alpha+1}^B$ defined as the function on $V_\alpha^B$ taking value 1 on $U$ and $W$ (and 0 elsewhere) satisfies: $\|U \in X_\alpha\| = 1$ and $\|W \in X_\alpha\| = 1$. The required inequality $\|Z \in X_\alpha\| \leqslant \|Z = U\| \vee \|Z = W\|$ follows since $\|Z \in X_\alpha\| = \bigvee_{Y \in V_\alpha^B} \|Z = Y\| \wedge X_\alpha(Y)$, and the only nonzero terms are for $Y=U$ and $Y=W$.
