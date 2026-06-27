---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Definition 17.4 constructs the formal environment $\mathcal{L}_{\text{el}}$ (elementary language) and the theory $\mathcal{P}$ as a definitional expansion of $(\mathcal{P}, \mathcal{L}_{\text{nos}})$ (the theory $P$ in the language of number theory). The language is enriched with operation symbols for absolute difference $|-|$, integer division $[/]$, and for each operation symbol $\mathbf{O}$ a corresponding relation symbol $R_{\mathbf{O}}$ characterizing when the operation outputs $1$. Crucially, $\mathcal{P}$ includes the induction axiom schema for all formulas of the expanded language. Each nonlogical constant is assigned a number-theoretic interpretation $\#F$ via the recursion clauses, enabling the formalization of Godel numbering and syntax within the theory itself. This definition provides the minimal infrastructure needed to construct a provability predicate $\Pr$ satisfying the Hilbert-Bernays derivability conditions, which in turn makes Lob's Theorem (17.2) applicable and yields Godel's Second Incompleteness Theorem.
