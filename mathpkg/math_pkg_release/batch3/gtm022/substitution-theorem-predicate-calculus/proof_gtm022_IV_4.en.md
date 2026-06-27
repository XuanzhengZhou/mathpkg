---
role: proof
locale: en
of_concept: "substitution-theorem-predicate-calculus"
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---
Proof. (a) Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$. By induction on $n$, $\alpha(p_1), \ldots, \alpha(p_n)$ is a proof of $\alpha(p)$ from $\alpha(A)$. If $a$ is an axiom of type $\mathcal{A}_4$, Lemma 4.2 ensures $x \notin \operatorname{var}(p)$ is preserved, so $\alpha(a)$ is again an axiom. Other axioms are clearly preserved. For Modus Ponens, $\alpha(p_i) = \alpha(p_j) \Rightarrow \alpha(p_n)$. For Generalisation, the semi-homomorphism conditions ensure the variable restriction is preserved.

(b) Similar argument using the definition of interpretation. $\square$
