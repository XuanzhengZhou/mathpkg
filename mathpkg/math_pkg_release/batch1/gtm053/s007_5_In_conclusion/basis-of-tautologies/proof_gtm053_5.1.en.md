---
role: proof
locale: en
of_concept: basis-of-tautologies
source_book: gtm053
source_chapter: "5"
source_section: "5.1"
---

Let $\mathcal{E}$ be a finite set of formulas in $L$, and let $P$ be a logical polynomial (with a fixed representation) over $\mathcal{E}$. For any map $v : \mathcal{E} \to \{0,1\}$, we extend $v$ to $P$ using the same rules that defined the truth function $|\cdot|$ in Section 2.5. We set

$$P^v = \begin{cases} P, & \text{if } v(P) = 1, \\ \neg P, & \text{if } v(P) = 0. \end{cases}$$

**Fundamental Lemma (5.2).** Let $\mathcal{E}^v = \{Q^v \mid Q \in \mathcal{E}\}$. Then for any $v$ we have $\mathcal{F} \cup \mathcal{E}^v \vdash P^v$ (using MP).

This lemma expresses the following idea. It is natural to prove Proposition 5.1 by induction on the length of the tautology. However, the component parts of a tautology themselves might not be tautologies. The operation of taking $P$ to $P^v$ forces any formula to be ``$v$-true'' and makes it possible for us to use induction.

**Proof of 5.1 assuming the Fundamental Lemma.** Let $P$ be a tautology, so that $P^v = P$ for all $v$. Set $\mathcal{E} = \{P_1, \ldots, P_r\}$. By the fundamental lemma, $\mathcal{F} \cup \{P_1^v, \ldots, P_r^v\} \vdash P$ using MP for any $v$. We show that then $\mathcal{F} \cup \{P_1^v, \ldots, P_{r-1}^v\} \vdash P$ using MP. Descending induction on $r$ then gives the required assertion.

The induction step proceeds by considering the two cases $v(P_r) = 0$ and $v(P_r) = 1$. In each case we apply the deduction theorem and use the basis tautologies to eliminate the assumption $P_r^v$, reducing the number of hypotheses by one. The required deductions of formulas 1--16 from $\mathcal{F}$ and the pair $(Q_1^v, Q_2^v)$ using MP are given by the table:

$$\begin{array}{cccc}
v(Q_1) & v(Q_2) & Q_1^v, Q_2^v & (Q_1 \Rightarrow Q_2)^v \\ \hline
0 & 0 & \neg Q_1, \neg Q_2 & 1.\; Q_1 \Rightarrow Q_2 \\
0 & 1 & \neg Q_1, Q_2 & 2.\; Q_1 \Rightarrow Q_2 \\
1 & 0 & Q_1, \neg Q_2 & 3.\; \neg(Q_1 \Rightarrow Q_2) \\
1 & 1 & Q_1, Q_2 & 4.\; Q_1 \Rightarrow Q_2
\end{array}$$

$$\begin{array}{cccc}
v(Q_1) & v(Q_2) & (Q_1 \land Q_2)^v & (Q_1 \lor Q_2)^v \\ \hline
0 & 0 & 5.\; \neg\neg(Q_1 \Rightarrow \neg Q_2) & 9.\; \neg(\neg Q_1 \Rightarrow Q_2) \\
0 & 1 & 6.\; \neg\neg(Q_1 \Rightarrow \neg Q_2) & 10.\; \neg Q_1 \Rightarrow Q_2 \\
1 & 0 & 7.\; \neg\neg(Q_1 \Rightarrow \neg Q_2) & 11.\; \neg Q_1 \Rightarrow Q_2 \\
1 & 1 & 8.\; \neg(Q_1 \Rightarrow \neg Q_2) & 12.\; \neg(\neg Q_1 \Rightarrow Q_2)
\end{array}$$

In the columns under $\land$ and $\lor$ we give formulas from which $(Q_1 \land Q_2)^v$ and $(Q_1 \lor Q_2)^v$, respectively, are deducible using MP and the tautologies in $\mathcal{F}$ (tautologies C1, C2, and C5). Hence it suffices to find deductions of each of formulas 1--16 from $\mathcal{F}$ and the pair of formulas in the appropriate row using MP.
