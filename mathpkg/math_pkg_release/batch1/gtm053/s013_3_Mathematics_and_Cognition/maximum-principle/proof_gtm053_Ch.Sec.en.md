---
role: proof
locale: en
of_concept: maximum-principle
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

First, find an ordinal $\beta$ such that $\bigvee_{U \in V^B} W(U) = \bigvee_{U \in V_\beta^B} W(U)$ using the fact that $B$ is a set. Index $V_\beta^B = \{U_\alpha\}_{\alpha \in I}$ and set
$$a_\alpha = W(U_\alpha) \wedge \left( \bigvee_{\gamma < \alpha} W(U_\gamma) \right)'.$$
Then $a_\alpha \wedge a_\gamma = 0$ for $\alpha \neq \gamma$. Using Lemma 7.2(b), glue together the $U_\alpha$ with probabilities $a_\alpha$ to obtain $X$ satisfying $\|X = U_\alpha\| \geqslant a_\alpha \geqslant W(U_\alpha)$. By extensionality, $W(X) \geqslant \bigvee_\alpha a_\alpha = \bigvee_U W(U)$.
