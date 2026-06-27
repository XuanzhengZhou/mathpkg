---
role: proof
locale: en
of_concept: basis-deformation-theorem
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§8. Oriented vector spaces"
---

**Necessity**: Suppose $x_v(t)$ is a deformation from $a_v$ to $b_v$. Let $\Delta \neq 0$ be a determinant function and define $\Phi(t) = \Delta(x_1(t), \ldots, x_n(t))$. By continuity of $\Delta$ and of the maps $t \mapsto x_v(t)$, $\Phi$ is continuous. Moreover, $\Phi(t) \neq 0$ for all $t$ because the vectors $x_v(t)$ are linearly independent. Thus $\Phi$ has constant sign on $[t_0, t_1]$.

Now $\Phi(t_1) = \Delta(b_1, \ldots, b_n) = \Delta(\varphi a_1, \ldots, \varphi a_n) = \det \varphi \cdot \Delta(a_1, \ldots, a_n) = \det \varphi \cdot \Phi(t_0)$. Since $\Phi(t_0)$ and $\Phi(t_1)$ have the same sign, $\det \varphi > 0$.

**Sufficiency**: Assume $\det \varphi > 0$. First, assume that the vector $n$-tuples $(a_1, \ldots, a_i, b_{i+1}, \ldots, b_n)$ are linearly independent for each $i = 0, \ldots, n-1$. Write $b_n = \sum_v \beta^v a_v$. Since $(a_1, \ldots, a_{n-1}, b_n)$ are linearly independent, $\beta^n \neq 0$. Define $\varepsilon_n = \operatorname{sgn}(\beta^n)$ and the deformation
$$x_v(t) = a_v\;(v = 1, \ldots, n-1), \quad x_n(t) = (1-t)a_n + t\varepsilon_n b_n, \quad 0 \leq t \leq 1.$$
One checks that $x_v(t)$ remain linearly independent. This deforms $(a_1, \ldots, a_n)$ to $(a_1, \ldots, a_{n-1}, \varepsilon_n b_n)$.

Iterating this process yields a deformation from $(a_1, \ldots, a_n)$ to $(\varepsilon_1 b_1, \ldots, \varepsilon_n b_n)$ with $\varepsilon_v = \pm 1$. By construction, $\det(\varphi: a_v \mapsto \varepsilon_v b_v) > 0$, hence $\varepsilon_1 \cdots \varepsilon_n = +1$, so the number of $-1$ signs is even. Pairing the negative signs, a rotation in the corresponding 2-dimensional planes (using sine/cosine parametrization) deforms each pair $(-b_i, -b_j)$ to $(b_i, b_j)$. Thus $(\varepsilon_1 b_1, \ldots, \varepsilon_n b_n)$ deforms to $(b_1, \ldots, b_n)$.

If the linear independence hypothesis fails, perturb the $a_v$ slightly within spherical neighborhoods where $\Delta \neq 0$, ensuring the required independence, deform the perturbed basis, and combine with the initial perturbation to obtain the desired deformation.
