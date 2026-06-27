---
role: proof
locale: en
of_concept: deduction-theorem-prop-calculus
source_book: gtm022
source_chapter: "II"
source_section: "§2 Soundness and Adequacy of Prop(X)"
---

**Proof.** Suppose $A \cup \{p\} \vdash q$. Let $p_1, \ldots, p_n = q$ be a proof of $q$ from $A \cup \{p\}$. We prove by induction on $n$ that $A \vdash p \Rightarrow q$.

If $n = 1$, then $q \in \mathcal{A} \cup A \cup \{p\}$. If $q \in \mathcal{A} \cup A$, then $q, q \Rightarrow (p \Rightarrow q), p \Rightarrow q$ is a proof of $p \Rightarrow q$ from $A$. If $q = p$, then $\vdash p \Rightarrow p$, and so $A \vdash p \Rightarrow q$.

Suppose now $n > 1$. By induction, $A \vdash p \Rightarrow p_i$ for $i = 1, 2, \ldots, n - 1$, and we may suppose $q \notin \mathcal{A} \cup A \cup \{p\}$. For some $i, j < n$, we have $p_i = p_j \Rightarrow q$. Thus $A \vdash p \Rightarrow p_j$, $A \vdash p \Rightarrow (p_j \Rightarrow q)$, and there exists a proof $q_1, \ldots, q_k, q_{k+1}$ from $A$ with

$$q_k = p \Rightarrow p_j,$$
$$q_{k+1} = p \Rightarrow (p_j \Rightarrow q).$$

We put

$$q_{k+2} = (p \Rightarrow (p_j \Rightarrow q)) \Rightarrow ((p \Rightarrow p_j) \Rightarrow (p \Rightarrow q)), \qquad (\mathcal{A}_2)$$
$$q_{k+3} = (p \Rightarrow p_j) \Rightarrow (p \Rightarrow q), \qquad (q_{k+2} = q_{k+1} \Rightarrow q_{k+3})$$
$$q_{k+4} = p \Rightarrow q.$$

Then $q_1, \ldots, q_{k+4}$ is a proof of $p \Rightarrow q$ from $A$.
