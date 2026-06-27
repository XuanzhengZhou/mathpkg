---
role: proof
locale: en
of_concept: "characterization-of-maximal-consistent"
source_book: gtm022
source_chapter: "III"
source_section: "2"
---
Proof. (a) Let $A$ be maximal consistent. Then $F \notin A$, for otherwise $A \vdash F$ and $A$ inconsistent. If $A \vdash q$, then $A \cup \{q\} = A$ is consistent, so maximality gives $q \in A$; thus $A = \operatorname{Ded}(A)$. For any $p \in P(X)$, if $p \notin A$, then $A \cup \{p\}$ is inconsistent, so $A \cup \{p\} \vdash F$. By the Deduction Theorem, $A \vdash p \Rightarrow F = \sim p$, hence $\sim p \in A$.

(b) Conversely, suppose $A$ satisfies (i)-(iii). If $A$ is inconsistent, then $A \vdash F$ and so $F \in A = \operatorname{Ded}(A)$, contradicting (i). If $A \subset T$, pick $p \in T \setminus A$. By (iii), $\sim p \in A \subseteq T$, so $T$ contains both $p$ and $\sim p = p \Rightarrow F$, hence $T \vdash F$ by Modus Ponens. Thus $T$ is inconsistent. $\square$
