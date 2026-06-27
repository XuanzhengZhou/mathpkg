---
role: proof
locale: en
of_concept: consistency-contradiction-equivalence
source_book: gtm053
source_chapter: "II"
source_section: "4.2"
---

The implication (b) $\Rightarrow$ (a) is trivial: if all formulas are deducible, then in particular both $P$ and $\neg P$ are deducible for some $P$.

For (a) $\Rightarrow$ (b), suppose $\mathcal{E} \vdash P$ and $\mathcal{E} \vdash \neg P$. Let $Q$ be any formula. The tautology B2 gives $\neg P \Rightarrow (P \Rightarrow Q)$. Since $\mathcal{E} \vdash \neg P$, by MP we obtain $\mathcal{E} \vdash P \Rightarrow Q$. Since also $\mathcal{E} \vdash P$, by MP again we obtain $\mathcal{E} \vdash Q$. Thus every formula is deducible from $\mathcal{E}$.
