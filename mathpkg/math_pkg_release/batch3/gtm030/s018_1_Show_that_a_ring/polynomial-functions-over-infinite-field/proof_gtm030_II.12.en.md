---
role: proof
locale: en
of_concept: polynomial-functions-over-infinite-field
source_book: gtm030
source_chapter: "II"
source_section: "12"
---

By induction on $r$. The case $r = 1$: a non-zero polynomial in one variable over an infinite field has only finitely many roots, hence there exists $c \in \mathfrak{F}$ with $f(c) \neq 0$.

Assume the theorem holds for $r-1$ variables. Write
$$f(x_1, \cdots, x_r) = B_0 + B_1 x_r + \cdots + B_m x_r^m$$
where $B_i \in \mathfrak{F}[x_1, \cdots, x_{r-1}]$ and $B_m \neq 0$. By the induction hypothesis, there exist $c_1, \cdots, c_{r-1} \in \mathfrak{F}$ such that $B_m(c_1, \cdots, c_{r-1}) \neq 0$. Then $f(c_1, \cdots, c_{r-1}, x_r)$ is a non-zero polynomial in $x_r$, so by the $r = 1$ case there exists $c_r \in \mathfrak{F}$ with $f(c_1, \cdots, c_{r-1}, c_r) \neq 0$.
