---
role: proof
locale: en
of_concept: maximal-consistent-characterization
source_book: gtm022
source_chapter: "III"
source_section: "2"
---

(a) Let $A$ be maximal consistent. Since $A$ is consistent, $F \notin \operatorname{Ded}(A)$, so $F \notin A$. By definition, $A \subseteq \operatorname{Ded}(A)$. If $\operatorname{Ded}(A) \neq A$, then $\operatorname{Ded}(A)$ properly contains $A$ and is consistent (since $F \notin \operatorname{Ded}(A)$), contradicting maximality. Thus $A = \operatorname{Ded}(A)$. For (iii), if $p \notin A$ and $\sim p \notin A$, then both $A \cup \{p\}$ and $A \cup \{\sim p\}$ are inconsistent, which would imply $A$ is inconsistent.
(b) Conversely, if $A$ satisfies (i)-(iii) and $B \supsetneq A$, pick $p \in B \setminus A$. By (iii), $\sim p \in A \subseteq B$, so $\{p, \sim p\} \subseteq B$. From $\{p, \sim p\} \vdash F$, we get $F \in \operatorname{Ded}(B)$, so $B$ is inconsistent.
