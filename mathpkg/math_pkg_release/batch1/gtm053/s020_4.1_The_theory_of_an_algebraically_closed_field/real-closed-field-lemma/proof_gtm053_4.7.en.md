---
role: proof
locale: en
of_concept: real-closed-field-lemma
source_book: gtm053
source_chapter: "4"
source_section: "4.7"
---

(i) The relative algebraic closure $\tilde{A}_0$ of $A_0$ in $A$ consists of all elements of $A$ that are algebraic over $A_0$. Since $A$ is real closed, each such element is characterized by its minimal polynomial over $A_0$ and its position in the ordering of the roots. The isomorphism $\varphi$ sends the minimal polynomial to a polynomial over $B_0$, whose roots in $B$ correspond bijectively and order-preservingly to the roots in $A$. Thus $\varphi$ extends uniquely to the algebraic closures.

(ii) The field $A_0(a_0)$ consists of rational functions in $a_0$ with coefficients in $A_0$. Since $a_0 \notin A_0$ and $A_0$ is algebraically closed in $A$, $a_0$ is transcendental over $A_0$. The ordering condition $a_0 \leq a \iff b_0 \leq \varphi(a)$ for all $a \in A_0$ determines the cut that $a_0$ fills in $A_0$, and $\varphi$ maps this cut to the corresponding cut in $B_0$ filled by $b_0$. Hence $\varphi$ extends by sending $a_0 \mapsto b_0$ and extending to the field of rational functions, preserving order by the condition on cuts.

(iii) This follows from the fact that $A_0$ is algebraically closed in $A$, so any quantifier-free condition with parameters from $A_0$ that is satisfiable in $A$ must also be satisfiable in $A_0$, by the model-completeness of the theory of real closed fields (or directly via Sturm's theorem on real roots).
