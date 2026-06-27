---
role: proof
locale: en
of_concept: replacement-axiom-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

First reduce to the special case where $\|R\| = 1$ for $R$ being the premise $\forall x \in U \exists!y P(x,y)$. Under this assumption, construct $W$ as a random class by
$$\|Y \in W\| = \bigvee_{X \in V^B} \|X \in U\| \wedge \|P(X,Y)\|.$$
By the Maximum Principle (Lemma 7.4), for each $X \in D(U)$ find $Y_X \in V^B$ with $\|\exists y P(X,y)\| = \|P(X,Y_X)\|$. The premise $\|R\|=1$ implies $\|X \in U\| \leqslant \|\exists!y P(X,y)\|$, and then one shows $W \sim W_\alpha$ where $\alpha$ is chosen so that all $Y_X \in V_\alpha^B$.
