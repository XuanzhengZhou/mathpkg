---
role: proof
locale: en
of_concept: autotopism-additive-maps-form-group
source_book: gtm006
source_chapter: "VIII"
source_section: "4"
---
Since $P_1, P_2, Q_1, Q_2, R_1, R_2$ are all clearly non-singular additive mappings, we have to show that $(xP_1P_2)(yQ_1Q_2) = (xy)R_1R_2$ for all $x, y \in D$. But, since $(P_1, Q_1, R_1)$ and $(P_2, Q_2, R_2)$ are autotopisms,
$$(xP_1P_2)(yQ_1Q_2) = [(xP_1)(yQ_1)]R_2 = (xy)R_1R_2.$$

The given rule is obviously associative so that, in order to prove the lemma, we need only show that each element of $A$ has an inverse in $A$. If $(P, Q, R) \in A$ then we must find $(P', Q', R') \in A$ such that $(P, Q, R)(P', Q', R') = (P', Q', R')(P, Q, R) = (1, 1, 1)$. By the rule of composition, if such an element exists it must be $(P^{-1}, Q^{-1}, R^{-1})$; thus we must show that $(P^{-1}, Q^{-1}, R^{-1}) \in A$. But
$$[(xP^{-1})(yQ^{-1})]R = (xP^{-1})P \cdot (yQ^{-1})Q \quad 	ext{(since } (ab)R = aP \cdot bQ 	ext{ for all } a, b \in D	ext{)}$$
and thus $(xP^{-1})(yQ^{-1}) = (xy)R^{-1}$ as required. $\square$
