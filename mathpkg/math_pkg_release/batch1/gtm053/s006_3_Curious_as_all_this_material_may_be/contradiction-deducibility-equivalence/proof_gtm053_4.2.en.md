---
role: proof
locale: en
of_concept: contradiction-deducibility-equivalence
source_book: gtm053
source_chapter: "I"
source_section: "4.2"
---

Assume $\mathcal{E}$ contains all tautologies of type $\text{B}_2$ (which include $P \Rightarrow (\neg P \Rightarrow Q)$).

\textbf{(b) $\Rightarrow$ (a):} Trivial. If every formula is deducible from $\mathcal{E}$, then in particular there exists a formula $P$ (indeed, any formula) such that both $P$ and $\neg P$ are deducible.

\textbf{(a) $\Rightarrow$ (b):} Suppose $\mathcal{E} \vdash P$ and $\mathcal{E} \vdash \neg P$. Let $Q$ be any formula. Since $\mathcal{E}$ contains all tautologies of type $\text{B}_2$, the formula

$$P \Rightarrow (\neg P \Rightarrow Q)$$

is in $\mathcal{E}$ (or is deducible as a tautology). From $\mathcal{E} \vdash P$ and this tautology, by modus ponens we obtain $\mathcal{E} \vdash \neg P \Rightarrow Q$. Then from $\mathcal{E} \vdash \neg P$ and $\mathcal{E} \vdash \neg P \Rightarrow Q$, by modus ponens we obtain $\mathcal{E} \vdash Q$. Since $Q$ was arbitrary, (b) holds.
