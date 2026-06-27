---
role: proof
locale: en
of_concept: ufd-polynomial-ring
source_book: gtm030
source_chapter: "II"
source_section: "6"
---

Let $f(x) \neq 0$ and not a unit in $\mathfrak{A}[x]$. Write $f(x) = d f_1(x)$ where $f_1(x)$ is primitive and $d \in \mathfrak{A}$ is the GCD of the coefficients of $f$. If $f_1(x)$ is reducible, factor it as $f_{11}(x)f_{12}(x)$, where both factors have positive degree. Continuing, we obtain $f_1(x) = q_1(x) \cdots q_h(x)$ where each $q_i(x)$ is irreducible and has positive degree. Also factor $d = p_1 \cdots p_s$ in $\mathfrak{A}$. This gives a factorization of $f(x)$ into irreducibles in $\mathfrak{A}[x]$.

For uniqueness, suppose
$$p_1 \cdots p_s q_1(x) \cdots q_h(x) = p_1' \cdots p_t' q_1'(x) \cdots q_k'(x)$$
where the $p_i, p_i'$ are irreducible in $\mathfrak{A}$ and $q_i(x), q_i'(x)$ are irreducible of positive degree. Passing to the field of fractions and using unique factorization there, the $q_i(x)$ and $q_i'(x)$ can be paired as associates in $\mathfrak{A}[x]$, and by Gauss's Lemma the constant factors then pair off as associates in $\mathfrak{A}$.

By induction, this extends to $\mathfrak{A}[x_1, \cdots, x_r]$, showing it is also Gaussian.
