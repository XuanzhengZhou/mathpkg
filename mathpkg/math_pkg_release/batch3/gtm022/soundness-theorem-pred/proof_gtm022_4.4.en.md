---
role: proof
locale: en
of_concept: soundness-theorem-pred
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---

Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$, and let $(U, \varphi, \psi, v)$ be an interpretation with $v(A) \subseteq \{1\}$. By induction on $n$:
$n=1$: $p \in \mathcal{A} \cup A$. All axioms are valid, so $v(p)=1$.
$n>1$: If by Modus Ponens, $v(p_j)=v(p_j \Rightarrow p_n)=1$, then $v(p_n)=1$. If by Generalisation, $p_n = (\forall x)q$, with a proof $q_1, \ldots, q_k$ of $q$ from $A_0$ where $x \notin \operatorname{var}(A_0)$. By the Substitution Theorem, for any extension with a new variable $t$, $q_1(t), \ldots, q_k(t)$ is a proof of $q(t)$ from $A_0$. By the induction hypothesis and condition $(c_r)$ in the definition of interpretation, $v((\forall x)q) = 1$.
