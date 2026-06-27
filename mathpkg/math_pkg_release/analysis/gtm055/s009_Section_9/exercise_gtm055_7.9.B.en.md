---
role: exercise
locale: en
chapter: "7"
section: "9"
exercise_number: B
---

Let $(X, \mathbf{S})$ be a measurable space, let $(X, \mathcal{L}, L)$ be a Lebesgue integral on $(X, \mathbf{S})$, and let $\mu$ be the measure associated with $L$ as in Theorem 7.6. Verify that if $E$ is a set in $\mathbf{S}$ and $\alpha$ is a complex number such that $\alpha \neq 0$ then $\chi_{\alpha E}$ belongs to $\mathcal{L}$ if and only if $\mu(E) < +\infty$, and use this fact to show that a measurable simple function $s$ on $X$ belongs to $\mathcal{L}$ if and only if it vanishes on the complement of a set of finite measure. Conclude that for each simple function $s$ in $\mathcal{L}$ there exist representations of the form $s = \sum_{i=1}^{n} \alpha_i \chi_{E_i}$, where $\mu(E_i) < +\infty$, $i = 1, \ldots, n$, and that, for any such representation, $L(s) = \sum_{i=1}^{n} \alpha_i \mu(E_i)$.

(i) Let $(X, \mathcal{L}', L')$ be a second Lebesgue integral on $(X, \mathbf{S})$, let $\mu'$ be the measure associated with $L'$ as in Theorem 7.6, and suppose $\mu(E) \leq \mu'(E)$, $E \in \mathbf{S}$. Prove that $\mathcal{L}' \subset \mathcal{L}$ and that $L(f) \leq L'(f)$ for every nonnegative function $f$ in $\mathcal{L}'$. (Hint: Use Propositions 6.6 and 7.2.)

(ii) Verify the uniqueness assertion of Theorem 7.6 by showing that if $(X, \mathbf{S}, \mu)$ is a measure space and $(X, \mathcal{L}_1, L_1)$ and $(X, \mathcal{L}_2, L_2)$ are Lebesgue integrals on $X$, each of which satisfies (6) with respect to $\mu$, then $\mathcal{L}_1 = \mathcal{L}_2$ and $L_1 = L_2$.
