---
role: proof
locale: en
of_concept: soundness-theorem-predicate-calculus
source_book: gtm022
source_chapter: "IV"
source_section: "§4 Properties of Pred(V,R)"
---

**Proof.** Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$. Let $(U, \varphi, \psi, v)$ be an interpretation such that $v(A) \subseteq \{1\}$. We use induction on $n$. If $n=1$, $p \in \mathcal{A} \cup A$, so $v(p)=1$. For $n>1$, if $p_i = p_j \Rightarrow p_n$ then $v(p_n)=1$ by the homomorphism property. If $p_n = (\forall x)q(x)$ obtained by Generalisation, the condition $(c_r)$ in the definition of interpretation ensures $v(p_n)=1$.
