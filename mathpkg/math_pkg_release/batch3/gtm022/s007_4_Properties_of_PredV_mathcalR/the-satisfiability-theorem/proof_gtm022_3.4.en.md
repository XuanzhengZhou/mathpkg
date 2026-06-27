---
role: proof
locale: en
of_concept: the-satisfiability-theorem
source_book: gtm022
source_chapter: "3"
source_section: "4"
---

Put $V_0 = V$, $A_0 = A$, $P_0 = P(V, \mathcal{R})$. We construct inductively $V_i$, $P_i = P(V_i, \mathcal{R})$, $A_i'$ and $A_i$ for $i > 0$.

Taking a new variable $t_p^{(i)}$ for each $p \in A_i$ of the form $p = (\exists x)q(x)$, we put

$$V_{i+1} = V_i \cup \{t_p^{(i)} \mid p \in A_i,\; p = (\exists x)q(x) \text{ for some } q(x)\},$$

$$A_{i+1}' = A_i \cup \{q(t_p^{(i)}) \mid p \in A_i,\; p = (\exists x)q(x),\; q(x) \in P_i\}.$$

Suppose that $F \notin \text{Ded}(A_i)$. If $F \in \text{Ded}(A_{i+1}')$, then

$$F \in \text{Ded}\big(A_i \cup \{q_1(t_{p_1}^{(i)}), \dots, q_r(t_{p_r}^{(i)})\}\big)$$

for some finite set $\{q_1(t_{p_1}^{(i)}), \dots, q_r(t_{p_r}^{(i)})\}$, which is impossible by Lemma 4.13. Thus $F \notin \text{Ded}(A_{i+1}')$, and by Lemma 2.11 of Chapter II, there exists $A_{i+1} \supseteq A_{i+1}'$ such that $A_{i+1}$ satisfies:

\begin{itemize}
\item[(i)] $F \notin \text{Ded}(A_{i+1})$ (consistency),
\item[(ii)] for every $p \in P_{i+1}$, either $p \in A_{i+1}$ or ${\sim}p \in A_{i+1}$ (maximality).
\end{itemize}

For each $i > 0$, choose such an $A_i$. Put $V^* = \bigcup_i V_i$, $A^* = \bigcup_i A_i$. Since any finite subset of $A^*$ is contained in some $A_i$, it follows that $V^*$ and $A^*$ satisfy (i), (ii) and:

\begin{itemize}
\item[(iii)] if $(\exists x)q(x) \in A^*$, then $q(t) \in A^*$ for some $t \in V^*$.
\end{itemize}

The set $A^*$ then determines a canonical interpretation (the Henkin model) in which every formula in $A^*$ (and hence every formula in $A$) is true.
