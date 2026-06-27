---
role: proof
locale: en
of_concept: "deduction-theorem-propositional"
source_book: gtm022
source_chapter: "III"
source_section: "2"
---
Proof. If $A \vdash p \Rightarrow q$, then by appending $p$ and applying Modus Ponens we obtain a proof of $q$ from $A \cup \{p\}$, so $A \cup \{p\} \vdash q$.

Conversely, suppose $A \cup \{p\} \vdash q$ and let $p_1, \ldots, p_n$ be a proof of $q$ from $A \cup \{p\}$. We prove by induction on $n$ that $A \vdash p \Rightarrow p_n$. For $n = 1$: if $p_n \in \mathcal{A} \cup A$, then $p_n, p_n \Rightarrow (p \Rightarrow p_n), p \Rightarrow p_n$ is a proof of $p \Rightarrow p_n$ from $A$. If $p_n = p$, then $\vdash p \Rightarrow p$ (Example 4.5 of Chapter II), so $A \vdash p \Rightarrow p_n$.

For $n > 1$, by induction $A \vdash p \Rightarrow p_i$ for $i < n$. If $p_n \in \mathcal{A} \cup A \cup \{p\}$, the result follows as above. Otherwise, for some $i, j < n$, $p_i = p_j \Rightarrow p_n$. Thus $A \vdash p \Rightarrow p_j$ and $A \vdash p \Rightarrow (p_j \Rightarrow p_n)$. Using axiom $\mathcal{A}_2$, we have:
$$(p \Rightarrow (p_j \Rightarrow p_n)) \Rightarrow ((p \Rightarrow p_j) \Rightarrow (p \Rightarrow p_n))$$
and two applications of Modus Ponens yield $A \vdash p \Rightarrow p_n$. $\square$
