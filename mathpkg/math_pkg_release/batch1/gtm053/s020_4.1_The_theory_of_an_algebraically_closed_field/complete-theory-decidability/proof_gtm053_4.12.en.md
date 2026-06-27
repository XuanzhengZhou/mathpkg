---
role: proof
locale: en
of_concept: complete-theory-decidability
source_book: gtm053
source_chapter: "4"
source_section: "4.12"
---

If there is an algorithm listing the axioms of $T$, then it is easy to compile an algorithm that lists all consequences of the axioms, that is, enumerates $T$. Given a recursively enumerable set of axioms, one can systematically generate all finite sequences of formulas, check whether each constitutes a valid proof from the axioms, and output the conclusion whenever a valid proof is found. This procedure enumerates all theorems of $T$.

Now, given a sentence $P$, one can decide whether $P \in T$ by the following algorithm: run the enumeration of theorems and check at each step whether the current formula $Q_i$ equals $P$ or equals $\neg P$. By completeness, at some step one or the other must happen (exactly one, since the theory is consistent). This obviously decides whether $P$ is in $T$.
