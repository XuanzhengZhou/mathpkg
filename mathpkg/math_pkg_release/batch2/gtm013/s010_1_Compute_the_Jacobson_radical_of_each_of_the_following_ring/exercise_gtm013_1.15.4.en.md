---
role: exercise
locale: en
chapter: "1"
section: "15"
exercise_number: 4
---

Let $Q$ be a field, $V_Q$ a vector space over $Q$ with basis $(x_\alpha)_{\alpha \in \Omega}$ indexed by a well-ordered set $\Omega$. For each $\alpha \in \Omega$ set $V_\alpha = \sum_{\beta < \alpha} Q x_\beta$.

Let $R$ be the subset of $\operatorname{End}(V_Q)$ of those $f$ such that for some scalar $a_f \in Q$:

(i) $\dim_K \operatorname{Im}(f - a_f 1_V) < \infty$

(ii) $(f - a_f 1_V)(x_\alpha) \in V_\alpha$ $(\alpha \in \Omega)$.

(1) Prove that $R$ is a subring of $\operatorname{End}(V_Q)$. [Note: $R$ can be represented as the ring of all $\Omega \times \Omega$ upper triangular matrices over $Q$, constant $(= a_f)$ on the diagonal and with at most finitely many non-zero rows above the diagonal.]

(2) Prove that $J = J(R) = \{f \in R \mid a_f = 0\}$.

(3) Prove that if $(f_1, f_2, \ldots)$ is any sequence in $J$, then there exists an $n$ such that $f_n f_{n-1} \cdots f_1 = 0$. [Hint: For each $\alpha \in \Omega$, let $\alpha_n \in \Omega$ be least such that $\operatorname{Im}(f_n f_{n-1} \cdots f_1) \leq V_{\alpha_n}$. If $f_n f_{n-1} \cdots f_1 \neq 0$ for all $n$, then $\alpha_1 > \alpha_2 > \cdots > \alpha_n > \cdots$, a contradiction.]

(4) In particular, deduce from (3) that $J$ is nil.

(5) Prove, however, that $\bigcap_{n=1}^{\infty} J^n \neq 0$. [Hint: Let $\omega$ be the first element of $\Omega$ such that $\{\alpha \in \Omega \mid \alpha < \omega\}$ is uncountable. Define $e_n$ and $f_n$...]
