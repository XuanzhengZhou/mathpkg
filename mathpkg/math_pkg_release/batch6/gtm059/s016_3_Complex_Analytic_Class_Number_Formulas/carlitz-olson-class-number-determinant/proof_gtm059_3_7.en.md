---
role: proof
locale: en
of_concept: carlitz-olson-class-number-determinant
source_book: gtm059
source_chapter: "3"
source_section: "7"
---

Starting from the class number formula for the maximal real subfield $K^+ = \mathbb{Q}(\zeta_p + \zeta_p^{-1})$,

$$h_p^+ = 2p \prod_{\substack{\chi \text{ even} \\ \chi \neq 1}} \left(-\frac{1}{2} B_{1, \chi^{-1}}\right)$$

where $B_{1,\chi}$ are generalized Bernoulli numbers. Using the expression of $L(1, \chi)$ in terms of logarithms of cyclotomic units (Theorem 2.2) and the decomposition of $L$-series (Section 3), one obtains an expression involving the character values. Let $\omega$ be the Teichm\"uller character and write even characters as $\chi = \omega^{\nu}$ with $\nu$ even, $2 \leq \nu \leq p-3$.

The Dedekind determinant formula (Theorem 6.1) applied to the group $G = (\mathbb{Z}/p\mathbb{Z})^{\times}/\{\pm 1\}$ with the function $f(a) = R(a)$ transforms the product over characters into the determinant $\det(R(gh^{-1}))_{g,h \in S}$. Further manipulation using the symmetry $R(-a) = p - R(a)$ and properties of the group determinant yields

$$\pm h_p^+ = \det\bigl(R(gh^{-1}) - R(-gh^{-1})\bigr)_{g,h \in S}.$$

Each entry $R(gh^{-1}) - R(-gh^{-1})$ lies in $\{-1, 0, 1\}$ because $R(x)$ is the least positive residue and $R(x) \in \{1, \dots, p-1\}$, while $R(-x) = p - R(x)$, so the difference satisfies $|R(x) - R(-x)| \leq 1$. The matrix has size $\frac{p-3}{2}$, corresponding to the number of non-trivial even characters of $(\mathbb{Z}/p\mathbb{Z})^{\times}$.
