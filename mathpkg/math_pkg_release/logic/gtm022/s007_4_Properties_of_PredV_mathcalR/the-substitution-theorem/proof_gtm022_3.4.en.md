---
role: proof
locale: en
of_concept: the-substitution-theorem
source_book: gtm022
source_chapter: "3"
source_section: "4"
---

**(a)** Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$. We use induction over $n$ to show that $\alpha(p_1), \ldots, \alpha(p_n)$ is a proof of $\alpha(p)$ from $\alpha(A)$.

If $a = ((\forall x)(p \Rightarrow q)) \Rightarrow (p \Rightarrow (\forall x)q)$ is an axiom of type $A_4$, then by Lemma 4.2, the condition $x \notin \text{var}(p)$ is preserved by the semi-homomorphism $(\alpha, \beta)$, and so $\alpha(a)$ is again an axiom. In all other cases, it is clear that the image of an axiom is an axiom. Thus if $p \in \mathcal{A}^{(1)} \cup A$, then $\alpha(p) \in \mathcal{A}^{(2)} \cup \alpha(A)$, where $\mathcal{A}^{(i)}$ is the set of axioms of $\text{Pred}(V_i, \mathcal{R}^{(i)})$. Hence our desired result holds for $n = 1$.

For $n > 1$, we may suppose by induction that $\alpha(p_1), \ldots, \alpha(p_{n-1})$ is a proof of $\alpha(p_{n-1})$ from $\alpha(A)$. If $p_i = p_j \Rightarrow p_n$ for some $i, j < n$, then $\alpha(p_i) = \alpha(p_j) \Rightarrow \alpha(p_n)$, and the result holds. It remains only to consider the case that $p_n = (\forall x)q(x)$ where $q(x)$ is proved from some subset of $A$ in which $x$ does not occur free in the assumptions. By the induction hypothesis and the preservation of the variable condition under the semi-homomorphism, the image of the generalization step is again a valid generalization step in the target calculus.

**(b)** Let $p_1, \ldots, p_n$ be a proof of $p$ from $A$. Let $(U, \varphi, \psi, v)$ be an interpretation of $P(V, \mathcal{R})$ such that $v(A) \subseteq \{1\}$. We have to show that $v(p) = 1$, and we shall use induction on $n$ to prove it. If $n = 1$, $p \in \mathcal{A} \cup A$ and then $v(p) = 1$. Suppose by induction that $n > 1$ and the result holds for proofs of length less than $n$. If $p_i = p_j \Rightarrow p_n$ for some $i, j < n$, then $v(p_i) = v(p_j) = 1$, and it follows that $v(p) = 1$.

Suppose finally that $p_n = (\forall x)q(x)$ and that $q_1(x), \ldots, q_k(x)$ is a proof of $q(x)$ from the subset $A_0$ of $A$ with $x \notin \text{var}(A_0)$. We must use condition $(c_r)$ in the definition of interpretation, where $r$ is the depth of $p_n$. Thus we take a new variable $t$, we put $V' = V \cup \{t\}$, and we consider extensions $\varphi' : V' \rightarrow U$ of $\varphi$ and maps $v'_{r-1} : P_{r-1}(V', \mathcal{R}) \rightarrow \mathbb{Z}_2$, as given in condition $(c_r)$. We have to prove that in every case, $v'_{r-1}(q_k(t)) = 1$. But each $v'_{r-1}$ extends uniquely to a valuation $v' : P(V', \mathcal{R}) \rightarrow \mathbb{Z}_2$ such that $(U, \varphi', \psi, v')$ is an interpretation of $P(V', \mathcal{R})$. By the Substitution Theorem (Theorem 4.3 (a)), $q_1(t), \ldots, q_k(t)$ is a proof of $q(t)$ from $A_0$, and the induction hypothesis applied to this proof in $P(V', \mathcal{R})$ yields $v'(q(t)) = 1$ for all such extensions, which implies $v((\forall x)q(x)) = 1$ by the definition of interpretation at quantifier steps.
