---
role: proof
locale: en
of_concept: affine-classification-of-quadrics-without-center
source_book: gtm023
source_chapter: "X. Quadrics"
source_section: "§3. Affine equivalence of quadrics"
---

Assume an affine mapping $x \to x'$ carries $Q_1$ into $Q_2$. Since the special points $q_1$ and $q_2$ (the chosen origins on the quadrics) are transformed accordingly, we may assume the mapping has the form
$$x' = \tau(x - q_1) + q_2.$$
Substituting into the equation of $Q_2$, the equation of $Q_1$ can be written as
$$\Phi_2(\tau(x - q_1)) + 2\langle a_2^*, \tau(x - q_1) \rangle = 0.$$
Applying the uniqueness theorem (sec. 10.9) and comparing with the defining equation of $Q_1$, we obtain
$$\Phi_1(x) = \lambda \Phi_2(\tau x),$$
where $\lambda \neq 0$ is a constant. This relation implies that $\Phi_1$ and $\Phi_2$ have the same rank $r$, and that the indices satisfy either $s_2 = s_1$ (if $\lambda > 0$) or $s_2 = r - s_1$ (if $\lambda < 0$). But the equation $s_2 = r - s_1$ is only compatible with the inequalities $2s_1 \geq r$ and $2s_2 \geq r$ (which hold for the indices of quadrics without center) if $s_1 = s_2 = r/2$. Hence, in either case, we must have $s_1 = s_2$.

Conversely, assume that $r_1 = r_2 = r$ and $s_1 = s_2 = s$. To construct an affine mapping transforming $Q_1$ into $Q_2$, consider the tangent spaces $T_{q_1}(Q_1)$ and $T_{q_2}(Q_2)$. As established in sec. 10.12, the restriction of $\Phi_i$ to $T_{q_i}(Q_i)$ ($i = 1, 2$) has the same rank and the same index as $\Phi_i$. Consequently, there exists an isomorphism $\varrho: T_{q_1}(Q_1) \to T_{q_2}(Q_2)$ such that
$$\Phi_1(y) = \Phi_2(\varrho y) \quad \text{for all } y \in T_{q_1}(Q_1).$$

Now select a vector $a_i$ in the nullspace of $\Phi_i$ ($i = 1, 2$) such that
$$\langle a_i^*, a_i \rangle = 1.$$
Define a linear isomorphism $\tau: E \to E$ extending $\varrho$ by setting $\tau a_1 = a_2$. Then one verifies that
$$\Phi_1(x) + 2\langle a_1^*, x \rangle = \Phi_2(\tau x) + 2\langle a_2^*, \tau x \rangle \quad \text{for all } x \in E.$$
Consequently, the affine mapping $x' = \tau(x - q_1) + q_2$ transforms $Q_1$ into $Q_2$, proving affine equivalence.
