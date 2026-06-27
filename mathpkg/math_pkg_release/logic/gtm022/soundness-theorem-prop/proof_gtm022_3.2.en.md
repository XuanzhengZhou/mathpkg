---
role: proof
locale: en
of_concept: soundness-theorem-prop
source_book: gtm022
source_chapter: "III"
source_section: "2"
---

Suppose there exists a proof $p_1, \ldots, p_n$ of $p$ from $A$. Let $v: P(X) \to \mathbb{Z}_2$ be a valuation with $v(A) \subseteq \{1\}$. By induction on $n$:
$n=1$: $p \in \mathcal{A} \cup A$. If $p \in A$, then $v(p)=1$. If $p \in \mathcal{A}$, then $p$ is a tautology (Exercise 3.8 of Ch.II), so $v(p)=1$.
$n>1$: Assume $v(p_i)=1$ for $i<n$. If $p_n \in \mathcal{A} \cup A$, then $v(p_n)=1$. Otherwise, $p_i = p_j \Rightarrow p_n$ for some $i,j<n$. Then $v(p_j)=1$ and $v(p_j \Rightarrow p_n)=1$, so $v(p_n)=1$ by the homomorphism property.
