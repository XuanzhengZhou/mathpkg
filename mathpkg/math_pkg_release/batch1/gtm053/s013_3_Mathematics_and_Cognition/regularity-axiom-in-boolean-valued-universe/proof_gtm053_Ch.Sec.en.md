---
role: proof
locale: en
of_concept: regularity-axiom-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "6"
---

Fix $X \in V^B$. The axiom has the form $R \Rightarrow S$. Suppose $\|R\| \wedge \|S\|' = a \neq 0$ and derive a contradiction. There exists $Y$ of least rank with $\|Y \in X\| \wedge a \neq 0$. Using the definitions:
$$\|R\| = \bigvee_{Y} \|Y \in X\|,$$
$$\|S\|' = \bigwedge_{Y} \|Y \in X\|' \vee \left( \bigvee_{Z} \|Z \in Y\| \wedge \|Z \in X\| \right),$$
the minimality of rank forces $\|Y \in X\| \wedge a \leqslant \bigvee_{Z} \|Z \in Y\| \wedge \|Z \in X\| \wedge a$, which contradicts the definition of $a$.
