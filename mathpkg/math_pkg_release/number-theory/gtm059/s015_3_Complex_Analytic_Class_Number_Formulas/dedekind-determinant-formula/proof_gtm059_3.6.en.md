---
role: proof
locale: en
of_concept: dedekind-determinant-formula
source_book: gtm059
source_chapter: "3. Complex Analytic Class Number Formulas"
source_section: "6"
---
Consider the vector space of complex-valued functions on $G$, which has two natural bases: first, the characters $\{\chi\}$, and second, the delta functions $\{\delta_a\}_{a \in G}$ where $\delta_a(b) = 1$ if $a = b$ and $0$ otherwise.

For each $a \in G$, define the linear operator $T_a$ acting on functions by $(T_a g)(x) = g(ax)$. Let
$$T = \sum_{a \in G} f(a) T_a.$$

Then for each character $\chi$, we have
$$T\chi = \sum_{a \in G} f(a) \chi(a) \cdot \chi,$$
so $\chi$ is an eigenvector of $T$ with eigenvalue $\sum_{a \in G} \chi(a) f(a)$. Consequently,
$$\det(T) = \prod_{\chi \in \hat{G}} \sum_{a \in G} \chi(a) f(a).$$

On the other hand, computing $T$ in the delta-function basis yields
$$(T\delta_b)(a) = f(ab^{-1}),$$
so the matrix of $T$ in this basis is precisely $(f(ab^{-1}))_{a,b \in G}$. Therefore
$$\det(T) = \det\left(f(ab^{-1})\right)_{a,b \in G},$$
which completes the proof.
