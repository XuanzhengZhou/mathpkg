---
role: proof
locale: en
of_concept: deduction-lemma
source_book: gtm053
source_chapter: "I"
source_section: "4.5"
---

Suppose $\mathcal{E} \supset \text{Ax } L$, $P$ is closed, and $Q_1, \ldots, Q_n = Q$ is a deduction of $Q$ from $\mathcal{E} \cup \{P\}$. We prove by induction on $j$ that $\mathcal{E} \vdash P \Rightarrow Q_j$ for each $j = 1, \ldots, n$. The base case and induction step consider the possible justifications for $Q_j$:

\textbf{Case (a):} $Q_j \in \mathcal{E}$ or $Q_j \in \text{Ax } L$. Then $Q_j, Q_j \Rightarrow (P \Rightarrow Q_j), P \Rightarrow Q_j$ is a deduction of $P \Rightarrow Q_j$ from $\mathcal{E}$, where the second formula is a tautology of type A1 and the third follows by MP.

\textbf{Case (b):} $Q_j = P$. Then $P \Rightarrow P$ is a tautology, hence deducible from $\mathcal{E}$.

\textbf{Case (c):} $Q_j$ follows from earlier $Q_r$ and $Q_s = Q_r \Rightarrow Q_j$ by MP. By induction hypothesis, $\mathcal{E} \vdash P \Rightarrow Q_r$ and $\mathcal{E} \vdash P \Rightarrow (Q_r \Rightarrow Q_j)$. Using the tautology
$$(P \Rightarrow Q_r) \Rightarrow ((P \Rightarrow (Q_r \Rightarrow Q_j)) \Rightarrow (P \Rightarrow Q_j))$$
and two applications of MP, we obtain $\mathcal{E} \vdash P \Rightarrow Q_j$.

\textbf{Case (d):} $Q_j = \forall x Q_r$ follows from $Q_r$ by Gen, where $x$ does not occur freely in $P$ (since $P$ is closed) nor in any formula of $\mathcal{E}$ used in deriving $Q_r$. By induction hypothesis, $\mathcal{E} \vdash P \Rightarrow Q_r$. We append:
$$\forall x(P \Rightarrow Q_r) \quad (\text{Gen})$$
$$\forall x(P \Rightarrow Q_r) \Rightarrow (P \Rightarrow \forall x Q_r) \quad (\text{logical quantifier axiom, since } P \text{ is closed})$$
$$P \Rightarrow \forall x Q_j \quad (\text{MP})$$

This completes the induction. Setting $j = n$ yields $\mathcal{E} \vdash P \Rightarrow Q$.

In the parts of deductions constructed here and in Lemma 4.4, only tautologies of types A0, A1, and A2 were used.
