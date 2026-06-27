---
role: proof
locale: en
of_concept: theorem-10-infinite-field
source_book: gtm030
source_chapter: "III"
source_section: "12"
---

**Proof.** The case $r = 1$ is known: a non-zero polynomial in one variable over an infinite field has only finitely many roots, hence there exist infinitely many $c \in \mathfrak{F}$ with $f(c) \neq 0$.

Assume the theorem holds for $r - 1$ variables. Write $f(x_1, x_2, \cdots, x_r)$ as a polynomial in $x_r$ with coefficients in $\mathfrak{F}[x_1, \cdots, x_{r-1}]$:

$$f(x_1, x_2, \cdots, x_r) = B_0 + B_1 x_r + \cdots + B_m x_r^m$$

where $B_i = B_i(x_1, \cdots, x_{r-1}) \in \mathfrak{F}[x_1, \cdots, x_{r-1}]$ and $B_m \neq 0$ (since $f \neq 0$). By the induction hypothesis applied to $B_m$, there exist $c_1, \cdots, c_{r-1} \in \mathfrak{F}$ such that $B_m(c_1, \cdots, c_{r-1}) \neq 0$. For these fixed $c_1, \cdots, c_{r-1}$, the polynomial

$$g(x_r) = f(c_1, \cdots, c_{r-1}, x_r) = B_0(c_1, \cdots, c_{r-1}) + B_1(c_1, \cdots, c_{r-1}) x_r + \cdots + B_m(c_1, \cdots, c_{r-1}) x_r^m$$

is a non-zero polynomial in the single variable $x_r$ over $\mathfrak{F}$ (its leading coefficient $B_m(c_1, \cdots, c_{r-1}) \neq 0$). Since $\mathfrak{F}$ is infinite, there exists $c_r \in \mathfrak{F}$ such that $g(c_r) \neq 0$, i.e., $f(c_1, \cdots, c_{r-1}, c_r) \neq 0$. This completes the induction.
