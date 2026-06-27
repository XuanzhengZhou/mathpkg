---
role: proof
locale: en
of_concept: power-set-axiom-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

Fix $X \in V^B$. Define $Y$ as a random class by
$$\|Z \in Y\| = \|Z \subset X\| = \bigwedge_{U \in V^B} \|U \in Z\|' \vee \|U \in X\|.$$
By Proposition 6.4, this is a random class. Let $D(X) = V_\alpha^B$. One first shows $\|U \in Z_\alpha\|' \geqslant \|U \in Z\|$, which yields $\|Z \in Y\| \leqslant \|Z_\alpha \in Y_{\alpha+1}\|$. Then one proves $\|Z \in Y\| \leqslant \|Z_\alpha = Z\|$, which gives $Y \sim Y_{\alpha+1}$.
