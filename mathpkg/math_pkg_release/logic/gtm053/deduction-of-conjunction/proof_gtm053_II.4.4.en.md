---
role: proof
locale: en
of_concept: deduction-of-conjunction
source_book: gtm053
source_chapter: "II"
source_section: "4.4"
---

If $P_1, \ldots, P_m$ and $Q_1, \ldots, Q_n$ are deductions of $P$ and $Q$, respectively, from $\mathcal{E}$, then
$$P_1, \ldots, P_m, Q_1, \ldots, Q_n, P \Rightarrow (Q \Rightarrow (P \wedge Q)), Q \Rightarrow (P \wedge Q), P \wedge Q$$
is a deduction of $P \wedge Q$ from $\mathcal{E}$. The formula $P \Rightarrow (Q \Rightarrow (P \wedge Q))$ is a tautology (of type A1). The formula $Q \Rightarrow (P \wedge Q)$ is a direct consequence of this tautology and $P_m = P$ by MP. The last formula $P \wedge Q$ is a direct consequence of $Q \Rightarrow (P \wedge Q)$ and $Q_n = Q$ by MP.
