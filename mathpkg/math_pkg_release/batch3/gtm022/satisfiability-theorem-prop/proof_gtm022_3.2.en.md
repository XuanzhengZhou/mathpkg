---
role: proof
locale: en
of_concept: satisfiability-theorem-prop
source_book: gtm022
source_chapter: "III"
source_section: "2"
---

Let $M$ be a maximal consistent subset containing $A$ (exists by extending $A$ via Zorn's Lemma). For $p \in P(X)$, put $v(p) = 1$ if $p \in M$ and $v(p) = 0$ if $p \notin M$.
$v(F) = 0$ since $F \notin M$. To show $v(p \Rightarrow q) = v(p) \Rightarrow v(q)$:
- If $q \in M$, then $\{q\} \vdash p \Rightarrow q$, so $p \Rightarrow q \in M$, and $v(p \Rightarrow q) = 1 = v(p) \Rightarrow v(q)$.
- If $p \notin M$, then $\{\sim p\} \vdash p \Rightarrow q$, so $p \Rightarrow q \in M$, and $v(p \Rightarrow q) = 1 = v(p) \Rightarrow v(q)$.
- If $p \in M$ and $q \notin M$, then $p \Rightarrow q \notin M$ (otherwise Modus Ponens would give $q \in M$), so $v(p \Rightarrow q) = 0 = v(p) \Rightarrow v(q)$.
