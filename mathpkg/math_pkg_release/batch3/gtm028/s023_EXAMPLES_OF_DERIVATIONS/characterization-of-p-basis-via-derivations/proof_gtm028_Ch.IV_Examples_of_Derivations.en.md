---
role: proof
locale: en
of_concept: characterization-of-p-basis-via-derivations
source_book: gtm028
source_chapter: "IV"
source_section: "Examples of Derivations"
---

**Equivalence of p-independence and freeness.** First, we establish that a set $\{x_1, \ldots, x_n\}$ is $p$-independent if and only if the elements are "free" with respect to the relation $\varphi$: $x_i \notin F^p(x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n)$ for each $i$.

If $\{x_1, \ldots, x_n\}$ is free, then $x_n \notin F^p(x_1, \ldots, x_{n-1})$. Consider the polynomial $f(x_1, \ldots, x_{n-1}, X)$ in $F^p(x_1, \ldots, x_{n-1})[X]$ expressing a hypothetical algebraic relation. Since $x_n$ is purely inseparable over $F^p$ (its $p$-th power lies in $F^p$) and $x_n \notin F^p(x_1, \ldots, x_{n-1})$, any such polynomial is nonzero. The degree in $X$ is less than $p$, so the polynomial is separable, hence $x_n$ cannot be a root. This proves $p$-independence.

Conversely, if $\{x_1, \ldots, x_n\}$ is not free, assume $x_n \in F^p(x_1, \ldots, x_{n-1})$. Write $x_n = g(x_1, \ldots, x_{n-1})$ where $g$ is a polynomial with coefficients in $F^p$ and degree less than $p$ in each argument. Then $g(x_1, \ldots, x_{n-1}) - x_n = 0$ is a linear dependence over $F^p$ among the monomials, contradicting $p$-independence.

**Existence of derivations from p-basis.** Let $S$ be a $p$-basis and fix $x \in S$. Consider the set $\mathcal{I}$ of all subsets $S' \subset S$ containing $x$ such that there exists a derivation of $F^p(S')$ trivial on $F^p(S' \setminus \{x\})$ and sending $x$ to $1$. By Zorn's lemma, $\mathcal{I}$ has a maximal element $S'$. If $S' \neq S$, choose $z \in S \setminus S'$. By $p$-independence, $z \notin F^p(S')$, so by Corollary 4 of Theorem 39 there exists a derivation of $F^p(S', z)$ trivial on $F^p(S')$ with $D(z) = 1$, contradicting maximality. Hence $S' = S$, and the derivation $D_{x,S}$ extends to a derivation $D_x$ of $F$ by Corollary 4' of Theorem 39.

**Converse.** Assume for each $x \in S$ there exists a derivation $D_x$ of $F/F^p$ with $D_x(x) = 1$ and $D_x(y) = 0$ for $y \neq x$. For arbitrary $x_1, \ldots, x_n \in S$, the derivation $D_{x_i}$ is trivial on $F^p(x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n)$ while $D_{x_i}(x_i) = 1$. Hence $x_i \notin F^p(x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n)$, showing freeness and thus $p$-independence.

**Basis of the derivation space.** If $F = F^p(x_1, \ldots, x_s)$ with $\{x_1, \ldots, x_s\}$ a $p$-basis, the derivations $D_1, \ldots, D_s$ constructed above satisfy $D_j(x_j) = 1$ and $D_j(x_i) = 0$ for $i \neq j$. They are linearly independent: if $\sum_i a_i D_i = 0$, then $a_j = (\sum_i a_i D_i)(x_j) = 0$. Moreover, for any $K$-derivation $D$, the derivation $D' = D - \sum_i D(x_i) D_i$ vanishes on $K$ and on $\{x_1, \ldots, x_s\}$, hence on $F$. Thus $\{D_1, \ldots, D_s\}$ spans $\mathcal{D}_{F/F^p}$.
