---
role: proof
locale: en
of_concept: polynomial-ring-isomorphism-extension
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

Let $T_0: R \to \bar{R}$ be an isomorphism. Every element of $S = R[x_1, \dots, x_n]$ can be written as $f(x_1, \dots, x_n)$ for a unique polynomial $f \in R[X_1, \dots, X_n]$ (since the $x_i$ are algebraically independent). Define $T: S \to \bar{S}$ by $f(x_1, \dots, x_n) \mapsto (T_0 f)(y_1, \dots, y_n)$, where $T_0 f$ is the polynomial obtained by applying $T_0$ to each coefficient of $f$.

Since $T_0$ is a ring isomorphism, the mapping $f \mapsto T_0 f$ is an isomorphism $R[X_1, \dots, X_n] \to \bar{R}[X_1, \dots, X_n]$. The substitution homomorphism $\bar{R}[X_1, \dots, X_n] \to \bar{S}$ sending $X_i \mapsto y_i$ is an isomorphism precisely when $y_1, \dots, y_n$ are algebraically independent over $\bar{R}$ (this follows from Theorem 7 of §17). The composition gives the desired $T$.

Uniqueness: any $R$-homomorphism extending $T_0$ and sending $x_i \mapsto y_i$ must send the monomial $a x_1^{i_1} \cdots x_n^{i_n}$ to $T_0(a) y_1^{i_1} \cdots y_n^{i_n}$, hence is uniquely determined on all of $S$.
