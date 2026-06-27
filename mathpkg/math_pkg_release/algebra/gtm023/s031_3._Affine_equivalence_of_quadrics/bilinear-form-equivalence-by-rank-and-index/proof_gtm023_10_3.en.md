---
role: proof
locale: en
of_concept: bilinear-form-equivalence-by-rank-and-index
source_book: gtm023
source_chapter: "X. Quadrics"
source_section: "§3. Affine equivalence of quadrics"
---

Assume first that there exists an isomorphism $\tau: E \to F$ such that $\Phi(x, y) = \Psi(\tau x, \tau y)$ for all $x, y \in E$. Select a basis $a_v$ ($v = 1, \ldots, n$) of $E$ such that
$$\Phi(a_v, a_\mu) = \varepsilon_v \delta_{v\mu}, \quad \varepsilon_v = \begin{cases} +1 & (v = 1, \ldots, s), \\ -1 & (v = s+1, \ldots, r), \\ 0 & (v = r+1, \ldots, n). \end{cases}$$
Then
$$\Psi(\tau a_v, \tau a_\mu) = \Phi(a_v, a_\mu) = \varepsilon_v \delta_{v\mu},$$
showing that $\Psi$ has rank $r$ and index $s$.

Conversely, assume that $\Phi$ and $\Psi$ both have rank $r$ and index $s$. Then there exist bases $a_v$ of $E$ and $b_v$ of $F$ ($v = 1, \ldots, n$) such that
$$\Phi(a_v, a_\mu) = \varepsilon_v \delta_{v\mu} \quad \text{and} \quad \Psi(b_v, b_\mu) = \varepsilon_v \delta_{v\mu}.$$
Define the linear isomorphism $\tau: E \to F$ by $\tau a_v = b_v$ ($v = 1, \ldots, n$). Then
$$\Phi(a_v, a_\mu) = \Psi(\tau a_v, \tau a_\mu) \quad (v, \mu = 1, \ldots, n),$$
and consequently, by bilinearity,
$$\Phi(x, y) = \Psi(\tau x, \tau y) \quad \text{for all } x, y \in E.$$
