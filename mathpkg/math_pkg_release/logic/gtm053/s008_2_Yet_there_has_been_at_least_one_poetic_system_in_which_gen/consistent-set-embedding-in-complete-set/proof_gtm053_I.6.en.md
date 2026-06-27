---
role: proof
locale: en
of_concept: consistent-set-embedding-in-complete-set
source_book: gtm053
source_chapter: "I"
source_section: "6"
---

The proof is a standard Lindenbaum construction. Enumerate all closed formulas of $L$ as $P_0, P_1, P_2, \ldots$. Define an increasing chain of consistent sets $\mathcal{E}_0 \subset \mathcal{E}_1 \subset \mathcal{E}_2 \subset \cdots$ as follows. Set $\mathcal{E}_0 = \mathcal{E}$. Given $\mathcal{E}_n$, consider $P_n$. If $\mathcal{E}_n \cup \{P_n\}$ is consistent, set $\mathcal{E}_{n+1} = \mathcal{E}_n \cup \{P_n\}$; otherwise, if $\mathcal{E}_n \cup \{\neg P_n\}$ is consistent, set $\mathcal{E}_{n+1} = \mathcal{E}_n \cup \{\neg P_n\}$. At least one of these must be consistent, for if both were inconsistent, we would have $\mathcal{E}_n \vdash \neg P_n$ and $\mathcal{E}_n \vdash \neg\neg P_n$, which would imply $\mathcal{E}_n$ is inconsistent—contradicting the induction hypothesis that $\mathcal{E}_n$ is consistent.

Finally, set $\mathcal{E}' = \bigcup_{n=0}^{\infty} \mathcal{E}_n$. By construction, $\mathcal{E}' \supset \mathcal{E}$. To verify consistency: any deduction of a contradiction from $\mathcal{E}'$ uses only finitely many formulas, hence would already appear in some $\mathcal{E}_n$, contradicting the consistency of $\mathcal{E}_n$. To verify completeness: for any closed formula $P = P_n$, either $P_n \in \mathcal{E}_{n+1}$ or $\neg P_n \in \mathcal{E}_{n+1}$, so either $P \in \mathcal{E}'$ or $\neg P \in \mathcal{E}'$.
