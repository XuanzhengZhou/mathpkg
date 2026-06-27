---
role: proof
locale: en
of_concept: smooth-germs-form-local-ring
source_book: gtm014
source_chapter: "III"
source_section: "3. The Generalized Malgrange Preparation Theorem"
---

It is easy to verify that the ring operations are well-defined on $C_p^\infty(X)$: if $f_1 = f_2$ and $g_1 = g_2$ on some neighborhoods of $p$, then $f_1 + g_1 = f_2 + g_2$ and $f_1 g_1 = f_2 g_2$ on the intersection of those neighborhoods. The additive identity is the germ of the constant zero function, and the multiplicative identity is the germ of the constant function $1$.

To see that $M_p(X)$ is the unique maximal ideal, consider the evaluation map $\operatorname{ev}_p: C_p^\infty(X) \to \mathbf{R}$ defined by $\operatorname{ev}_p([f]_p) = f(p)$. This is a well-defined surjective ring homomorphism whose kernel is precisely $M_p(X)$. Hence $C_p^\infty(X) / M_p(X) \cong \mathbf{R}$, a field. Therefore $M_p(X)$ is a maximal ideal.

To show uniqueness, suppose $I \subseteq C_p^\infty(X)$ is any proper ideal. If $[f]_p \in I$ has $f(p) \neq 0$, then $f$ is nonvanishing on some neighborhood of $p$, so $1/f$ is smooth there and $[1/f]_p$ is a multiplicative inverse of $[f]_p$ in $C_p^\infty(X)$, which would imply $I = C_p^\infty(X)$, a contradiction. Hence every element of a proper ideal must vanish at $p$, i.e., $I \subseteq M_p(X)$. Thus $M_p(X)$ contains every proper ideal, making it the unique maximal ideal. Therefore $C_p^\infty(X)$ is a local ring with maximal ideal $M_p(X)$.
