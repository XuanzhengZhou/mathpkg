---
role: proof
locale: en
of_concept: logical-consequence-equality-free
source_book: gtm037
source_chapter: "Part 5"
source_section: "Unusual Logics"
---

**Proof.** First assume that $\Gamma \models_{L} \varphi$. Let $(A, E)$ be any model in the $L^{e}$-sense of $\Gamma \cup E\{\varphi\}$, where $A$ is the underlying $L$-structure. Then $E$ is an equivalence relation on $A$. We form an $L$-structure $A/E$ with universe $A/E$ by setting
$$R^{A/E} = \{([a_0], \ldots, [a_{m-1}]) : (a_0, \ldots, a_{m-1}) \in R^{A}\}$$
for each $m$-ary relation symbol $R$ of $L$. For each $a \in A$ let $f a = [a]$. It is easily verified that $f$ is a two-way homomorphism of $A$ onto $A/E$. From 29.8 we see, then, that $(A/E, =)$ is a model of $\Gamma$ in the $L^{e}$-sense, so obviously $A/E$ is a model of $\Gamma$ in the $L$-sense. Hence by assumption $A/E \models_{L} \varphi$. Thus 29.9 yields $(A/E, =) \models_{L} \varphi$, and so by 29.8 we get $(A, E) \models_{L} \varphi$, as desired.

Conversely, suppose $\Gamma \models_{L} \bigwedge E\{\varphi\} \to \varphi$. Let $A$ be any $L$-structure such that $A \models_{L} \Gamma$. Consider the $L^{e}$-structure $(A, =)$ where equality is interpreted as the identity relation. Since equality does not appear in $\Gamma$, we have $(A, =) \models_{L^{e}} \Gamma$. Moreover, $=$ is an equivalence relation on $A$, so $(A, =) \models_{L^{e}} E\{\varphi\}$ (since $E\{\varphi\}$ replaces $=$ by $E$, and in $(A, =)$ the interpretation of $E$ coincides with identity). Hence $(A, =) \models_{L^{e}} \bigwedge E\{\varphi\}$. By the hypothesis, $(A, =) \models_{L} \varphi$. By 29.9, $A \models_{L} \varphi$, as desired.
