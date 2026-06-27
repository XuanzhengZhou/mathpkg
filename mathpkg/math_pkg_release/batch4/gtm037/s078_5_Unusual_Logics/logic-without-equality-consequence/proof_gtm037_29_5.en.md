---
role: proof
locale: en
of_concept: logic-without-equality-consequence
source_book: gtm037
source_chapter: "29"
source_section: "Unusual Logics"
---

First assume that $\Gamma \models_{L} \varphi$. Let $(A, E)$ be any model in the $L^{e}$-sense of $\Gamma \cup \text{E}\{\varphi\}$, where $A$ is the underlying $L$-structure. Then $E$ is an equivalence relation on $A$. We form an $L$-structure $A/E$ with universe $A/E$ by setting

$$R^{A/E} = \{([a_0], \ldots, [a_{m-1}]) : (a_0, \ldots, a_{m-1}) \in R^{A}\}$$

for each $m$-ary relation symbol $R$ of $L$. For each $a \in A$ let $fa = [a]$. It is easily verified that $f$ is a two-way homomorphism of $A$ onto $A/E$. From 29.8 we see, then, that $(A/E, =)$ is a model of $\Gamma$ in the $L^{e}$-sense, so obviously $A/E$ is a model of $\Gamma$ in the $L$-sense. Hence by assumption $A/E \models_{L} \varphi$. Thus 29.9 yields $(A/E, =) \models_{L} \varphi$, and so by 29.8 we get $(A, E) \models_{L} \varphi$, as desired.

The converse direction follows similarly.
