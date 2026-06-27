---
role: proof
locale: en
of_concept: conditional-probability-of-disjoint-disjunctions
source_book: gtm040
source_chapter: "4"
source_section: "4"
---

For each $k$, when $\Pr[p_k] > 0$ we have

$$c \cdot \Pr[p_k] = \Pr[p \mid p_k] \cdot \Pr[p_k] = \Pr[p \land p_k].$$

When $\Pr[p_k] = 0$, then $\Pr[p \land p_k] = 0 = c \cdot \Pr[p_k]$ holds as well. Summing over $k$:

$$c \cdot \Pr[\textstyle\bigvee p_k] = c \cdot \sum_{k} \Pr[p_k] = \sum_{k} \Pr[p \land p_k] = \Pr[p \land \textstyle\bigvee p_k].$$

Since $\Pr[\bigvee p_k] > 0$ by hypothesis, we obtain

$$\Pr[p \mid \textstyle\bigvee p_k] = \frac{\Pr[p \land \bigvee p_k]}{\Pr[\bigvee p_k]} = c.$$
