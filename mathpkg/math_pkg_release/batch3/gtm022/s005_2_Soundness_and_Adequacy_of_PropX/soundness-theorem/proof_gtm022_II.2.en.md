---
role: proof
locale: en
of_concept: soundness-theorem
source_book: gtm022
source_chapter: "II"
source_section: "2"
---

Suppose there exists a proof $p_1, \ldots, p_n$ of $p$ from $A$. We have to show $p$ is a consequence of $A$.

Let $v: P(X) \to \mathbb{Z}_2$ be a valuation for which $v(A) \subseteq \{1\}$. We shall use induction over the length $n$ of the proof of $p$ from $A$ to show that $v(p) = 1$. Suppose that $n = 1$. Then $p \in A \cup \mathcal{A}$, and since every axiom is a tautology (Exercise 3.8 of Chapter II), we have $v(p) = 1$.

Suppose now $n > 1$, and that $v(q) = 1$ for every $q$ provable from $A$ by a proof of length $< n$. Then $v(p_1) = v(p_2) = \cdots = v(p_{n-1}) = 1$. Either $p_n \in A \cup \mathcal{A}$ and $v(p_n) = 1$, as required, or for some $i, j < n$, we have $p_i = p_j \Rightarrow p_n$. In the latter case, $v(p_j) = v(p_j \Rightarrow p_n) = 1$, and the homomorphism property of $v$ requires $v(p_n) = 1$.
