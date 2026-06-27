---
role: proof
locale: en
of_concept: "soundness-theorem-propositional"
source_book: gtm022
source_chapter: "III"
source_section: "2"
---
Proof. Suppose there exists a proof $p_1, \ldots, p_n$ of $p$ from $A$. We show $p$ is a consequence of $A$.

Let $v: P(X) \to \mathbb{Z}_2$ be a valuation for which $v(A) \subseteq \{1\}$. We use induction over the length $n$ of the proof. Suppose $n = 1$. Then $p \in A \cup \mathcal{A}$, and since every axiom is a tautology (Exercise 3.8 of Chapter II), we have $v(p) = 1$.

Suppose $n > 1$, and that $v(q) = 1$ for every $q$ provable from $A$ by a proof of length $< n$. Then $v(p_1) = v(p_2) = \cdots = v(p_{n-1}) = 1$. Either $p_n \in A \cup \mathcal{A}$ and $v(p_n) = 1$, or for some $i, j < n$ we have $p_i = p_j \Rightarrow p_n$. In the latter case, $v(p_j) = 1$ and $v(p_j \Rightarrow p_n) = 1$, and the homomorphism property of $v$ forces $v(p_n) = 1$. $\square$
