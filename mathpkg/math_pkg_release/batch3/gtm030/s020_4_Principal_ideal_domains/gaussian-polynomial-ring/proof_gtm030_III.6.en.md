---
role: proof
locale: en
of_concept: gaussian-polynomial-ring
source_book: gtm030
source_chapter: "III"
source_section: "6"
---

Let $\mathfrak{A}$ be a Gaussian domain and let $\mathfrak{J}$ be its field of fractions.

Let $f(x) \in \mathfrak{A}[x]$ be non-zero and not a unit. Write $f(x) = d f_1(x)$ where $f_1(x)$ is primitive and $d \in \mathfrak{A}$ is the g.c.d. of the coefficients of $f(x)$.

If $f_1(x)$ is not a unit and is reducible, factor it as $f_1(x) = f_{11}(x) f_{12}(x)$ where each $f_{1i}(x)$ has positive degree (otherwise one factor would be a constant, contradicting primitivity). Then $\deg f_{1i}(x) < \deg f_1(x)$. Continuing this process, we obtain a factorization
$$f_1(x) = q_1(x) q_2(x) \cdots q_h(x)$$
where each $q_i(x)$ is irreducible in $\mathfrak{A}[x]$ and of positive degree. Also factor the constant $d$ as $d = p_1 p_2 \cdots p_s$ where the $p_i$ are irreducible in $\mathfrak{A}$ (hence also irreducible in $\mathfrak{A}[x]$). This yields a factorization
$$f(x) = p_1 p_2 \cdots p_s \cdot q_1(x) q_2(x) \cdots q_h(x)$$
into irreducibles in $\mathfrak{A}[x]$.

For uniqueness, suppose $f(x)$ has two factorizations into irreducibles. By Gauss's Lemma, primitive irreducible factors in $\mathfrak{A}[x]$ remain irreducible in $\mathfrak{J}[x]$. Since $\mathfrak{J}[x]$ is a principal ideal domain (hence Gaussian), the factorization in $\mathfrak{J}[x]$ is unique up to units. Using Gauss's Lemma to relate factors in $\mathfrak{A}[x]$ and $\mathfrak{J}[x]$, the two factorizations in $\mathfrak{A}[x]$ can be paired off into associate pairs. Hence the factorization in $\mathfrak{A}[x]$ is essentially unique, and $\mathfrak{A}[x]$ is Gaussian.
