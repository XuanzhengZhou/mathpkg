---
role: proof
locale: en
of_concept: sufficient-alphabet-extension
source_book: gtm053
source_chapter: "I"
source_section: "6"
---

**Step (a):** Let $L'$ be the language obtained from $L$ by adding a set of new constants of cardinality $\operatorname{card}(\text{alphabet of } L) + \aleph_0$. The alphabet of $L'$ then has cardinality $\operatorname{card}(\text{alphabet of } L) + \aleph_0$ as required.

**Step (b):** Consider the set of formulas $\mathcal{E} \cup \operatorname{Ax} L'$ in the language $L'$, where $\operatorname{Ax} L'$ consists of all the logical axioms of $L'$. We claim this set is consistent. If there were a deduction of a contradiction from $\mathcal{E} \cup \operatorname{Ax} L'$ in $L'$, then by the following procedure we could transform it into a deduction of a contradiction from $\mathcal{E}$ in $L$: take the finite set of all new constants that occur in the formulas in the deduction and replace these constants by old variables (in $L$) that do not occur in the formulas in the deduction. One easily verifies that the deduction of a contradiction remains a deduction of a contradiction, and now lies entirely in $L$. This would contradict the consistency of $\mathcal{E}$.

**Step (c):** Consider the set $S$ of formulas $P(x)$ containing one free variable $x$ such that $\neg \forall x P(x) \in \mathcal{E} \cup \operatorname{Ax} L'$. For each $P(x)$ in $S$, choose a new constant $c_P$ subject to the restriction that each $c_P$ can be assigned a natural number (its rank) in such a way that if a constant of rank $n$ occurs in $P(x)$, then $c_P$ has rank $> n$. This is possible since $\operatorname{card}(S) \leqslant \operatorname{card}(\text{alphabet of } L') = \operatorname{card}(\text{alphabet of } L) + \aleph_0$.

For each $P(x) \in S$, define the $R$-formula:

$$R_P: \neg \forall x P(x) \Rightarrow \neg P(c_P).$$

Finally set

$$\mathcal{E}' = \mathcal{E} \cup \operatorname{Ax} L' \cup \{R_P \mid P(x) \in S\}.$$

**Consistency check:** Suppose a contradiction were deducible from $\mathcal{E}'$. Any such deduction uses only finitely many $R$-formulas, say $R_{P_1}, \ldots, R_{P_k}$. Order them so that $c_{P_k}$ has maximal rank. Then one can replace $c_{P_k}$ by a fresh variable and transform the deduction into one from

$$\mathcal{E} \cup \operatorname{Ax} L' \cup \{R_{P_1}, \ldots, R_{P_{k-1}}\}.$$

Iterating this process removes all $R$-formulas, yielding a contradiction deducible from $\mathcal{E} \cup \operatorname{Ax} L'$ alone, which contradicts Step (b).

**Sufficiency:** By construction, whenever $\neg \forall x P(x) \in \mathcal{E}'$, the corresponding $R_P$ is also in $\mathcal{E}'$. Note that no $R_P$ formula has the form $\neg \forall x Q(x)$, so no new existential formulas are introduced. Thus the alphabet of $L'$ is sufficient for $\mathcal{E}'$.
