---
role: proof
locale: en
of_concept: deduction-of-conjunction
source_book: gtm053
source_chapter: "I"
source_section: "4.4"
---

If $P_1, \ldots, P_m$ and $Q_1, \ldots, Q_n$ are deductions of $P$ and $Q$, respectively, then

$$P_1, \ldots, P_m, Q_1, \ldots, Q_n, P \Rightarrow (Q \Rightarrow (P \wedge Q)), Q \Rightarrow (P \wedge Q), P \wedge Q$$

is a deduction of $P \wedge Q$. The third formula from the end is a tautology; the second formula from the end is a direct consequence of this tautology and $P_m = P$ using MP; and the last formula is a direct consequence of the second to last and $Q_n = Q$ using MP.
