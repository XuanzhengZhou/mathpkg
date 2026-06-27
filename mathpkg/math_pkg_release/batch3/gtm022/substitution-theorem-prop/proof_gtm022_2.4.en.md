---
role: proof
locale: en
of_concept: substitution-theorem-prop
source_book: gtm022
source_chapter: "II"
source_section: "4"
---

Let $p_1, \ldots, p_n$ be a proof of $w$ from $A$. We use induction on $n$. For $n = 1$, $w \in \mathcal{A} \cup A$. If $w \in A$, then $\varphi(w) \in \varphi(A)$. If $w$ is an axiom, then $\varphi(w)$ is also an axiom since the axiom schemas are closed under substitution. For $n > 1$, if $p_i = p_j \Rightarrow p_n$, then $\varphi(p_i) = \varphi(p_j) \Rightarrow \varphi(p_n)$, and the result follows by induction.
