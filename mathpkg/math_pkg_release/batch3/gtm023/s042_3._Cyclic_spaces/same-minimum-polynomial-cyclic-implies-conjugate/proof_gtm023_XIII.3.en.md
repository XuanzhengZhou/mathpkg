---
role: proof
locale: en
of_concept: same-minimum-polynomial-cyclic-implies-conjugate
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Choose generators $a$ and $b$ of $E$ and $F$. Then the vectors $a_j = \varphi^j(a)$ and $b_j = \psi^j(b)$ ($j = 0, \ldots, n-1$) form bases. The minimum polynomials determine the coefficients $\alpha_j, \beta_j$ via
$$\varphi(a_{n-1}) = \sum_{j=0}^{n-1} \alpha_j a_j, \quad \psi(b_{n-1}) = \sum_{j=0}^{n-1} \beta_j b_j.$$

Since $\mu_{\varphi} = \mu_{\psi}$, it follows that $\alpha_j = \beta_j$ ($j = 0, \ldots, n-1$). Define an isomorphism $\gamma: E \xrightarrow{\cong} F$ by $\gamma(a_j) = b_j$. Then
$$\psi \gamma(a_j) = \psi(b_j) = b_{j+1} = \gamma(a_{j+1}) = \gamma \varphi(a_j) \quad (j = 0, \ldots, n-1),$$
showing $\psi = \gamma \circ \varphi \circ \gamma^{-1}$.
