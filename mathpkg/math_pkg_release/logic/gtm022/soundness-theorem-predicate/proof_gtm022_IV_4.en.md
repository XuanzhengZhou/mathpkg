---
role: proof
locale: en
of_concept: "soundness-theorem-predicate"
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---
Proof. Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$. Let $(U, \varphi, \psi, v)$ be an interpretation with $v(A) \subseteq \{1\}$. By induction on $n$: if $n=1$, $p \in \mathcal{A} \cup A$ and $v(p)=1$ (all axioms are valid). For $n>1$, if Modus Ponens: $v(p_j)=v(p_j \Rightarrow p_n)=1$ implies $v(p_n)=1$.

If Generalisation: $p_n = (\forall x)q(x)$ from a proof of $q(x)$ from $A_0 \subseteq A$ with $x \notin \operatorname{var}(A_0)$. By condition $(c_r)$ in the interpretation definition, take a new variable $t$, form $V' = V \cup \{t\}$, and extend $\varphi$, $v'$. By the Substitution Theorem, $q_1(t), \ldots, q_k(t)$ is a proof of $q(t)$ from $A_0$. By induction, $v'(q(t)) = 1$. By condition $(c_r)$, $v(p_n) = 1$. $\square$
