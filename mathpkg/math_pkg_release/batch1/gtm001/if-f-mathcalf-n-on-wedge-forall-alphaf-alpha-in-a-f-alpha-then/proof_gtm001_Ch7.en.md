---
role: proof
locale: en
of_concept: if-f-mathcalf-n-on-wedge-forall-alphaf-alpha-in-a-f-alpha-then
source_book: gtm001
source_chapter: "7"
source_section: ""
---

(1) Since $(\forall \alpha)[F' \alpha \in (A - F' \alpha)]$ it follows that $(\forall \alpha)[F' \alpha \in A]$ and hence $\mathcal{W}(F) \subseteq A$.

(2) If $\alpha < \beta$, then $F' \alpha \in F'' \beta$. Since by hypothesis $F' \beta \in (A - F'' \beta)$, it follows that $F' \beta \notin F'' \beta$. Therefore $F' \alpha \neq F' \beta$. We have just proven that if $\alpha \neq \beta$, then $F' \alpha \neq F' \beta$. Consequently, if $F' \alpha = F' \beta$, then $\alpha = \beta$. Therefore $F$ is one-to-one.

(3) Since $\mathcal{W}(F) \subseteq A$, it follows that if $A$ is a set,

Remark. In the proof of Proposition 7.48 we see that the requirement that $(\forall \alpha)[F' \alpha \in A - F'' \alpha]$ assures us that the function $F$ defined by transfinite induction will be one-to-one. Conversely if $F$ is one-to-one then $W(F)$ will be a proper class and $(\forall \alpha)[F' \alpha \in A - F'' \alpha]$. Furthermore if $W(F)$ is a set then $F$ cannot be one-to-one. In this case Proposition 7.49 assures us that if $F$ fulfills the requirements for one-to-oneness "as long as it can," i.e., until $W(F)$ is exhausted then the restriction of $F$ to some ordinal $\alpha$ will map $\alpha$ one-to-one onto $W(F)$. From this we can prove that every well-ordered set is order isomorphic to an ordinal number.
