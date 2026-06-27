---
role: proof
locale: en
of_concept: deduction-theorem-prop
source_book: gtm022
source_chapter: "III"
source_section: "2"
---

($\Leftarrow$) If $A \vdash p \Rightarrow q$, then from a proof of $p \Rightarrow q$ from $A$, append $p$ (assumption) and $q$ (Modus Ponens) to get $A \cup \{p\} \vdash q$.
($\Rightarrow$) Suppose $p_1, \ldots, p_n = q$ is a proof of $q$ from $A \cup \{p\}$. We prove by induction on $n$ that $A \vdash p \Rightarrow p_i$ for each $i$.
$n=1$: If $q \in \mathcal{A} \cup A$, then $q, q \Rightarrow (p \Rightarrow q), p \Rightarrow q$ is a proof. If $q = p$, then $\vdash p \Rightarrow p$ (Example 4.5 of Ch.II).
$n>1$: If $p_i = p_j \Rightarrow q$ for $j,k < i$, the induction hypothesis gives $A \vdash p \Rightarrow p_j$ and $A \vdash p \Rightarrow (p_j \Rightarrow q)$. Using axiom $\mathcal{A}_2$ and Modus Ponens twice yields $A \vdash p \Rightarrow q$.
