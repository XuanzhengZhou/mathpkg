---
role: proof
locale: en
of_concept: fundamental-lemma-tautologies
source_book: gtm053
source_chapter: "5"
source_section: "5.2"
---

The proof of the Fundamental Lemma proceeds by induction on the construction of the logical polynomial $P$.

**Base case.** If $P$ is one of the variables in $\mathcal{E}$, say $P = Q \in \mathcal{E}$, then $P^v = Q^v$. Since $Q^v \in \mathcal{E}^v$, we trivially have $\mathcal{F} \cup \mathcal{E}^v \vdash Q^v$ (it is one of the hypotheses).

**Inductive step.** Assume the statement holds for subformulas $Q_1$ and $Q_2$, i.e., $\mathcal{F} \cup \mathcal{E}^v \vdash Q_1^v$ and $\mathcal{F} \cup \mathcal{E}^v \vdash Q_2^v$. We must show that $\mathcal{F} \cup \mathcal{E}^v \vdash (Q_1 * Q_2)^v$ for each logical connective $* \in \{\Rightarrow, \land, \lor, \Leftrightarrow\}$.

The deduction is carried out by a case analysis on the four possible truth values $v(Q_1), v(Q_2) \in \{0,1\}$. For each combination, the formula $(Q_1 * Q_2)^v$ is listed as one of formulas 1--16, and it is shown to be deducible from $\mathcal{F}$ together with $Q_1^v$ and $Q_2^v$ using MP and the basis tautologies in $\mathcal{F}$ (in particular, tautologies C1, C2, and C5).

The sixteen formulas are organized by connective:

- For $\Rightarrow$: formulas 1--4 give $(Q_1 \Rightarrow Q_2)^v$ for each valuation.
- For $\land$: formulas 5--8 give $(Q_1 \land Q_2)^v$ (using C1).
- For $\lor$: formulas 9--12 give $(Q_1 \lor Q_2)^v$ (using C2 and C5).
- For $\Leftrightarrow$: formulas 13--16 give $(Q_1 \Leftrightarrow Q_2)^v$.

By the induction hypothesis, we have deductions of $Q_1^v$ and $Q_2^v$ from $\mathcal{F} \cup \mathcal{E}^v$. Appending the appropriate deduction from the table yields a deduction of $(Q_1 * Q_2)^v$ from $\mathcal{F} \cup \mathcal{E}^v$, completing the induction.
