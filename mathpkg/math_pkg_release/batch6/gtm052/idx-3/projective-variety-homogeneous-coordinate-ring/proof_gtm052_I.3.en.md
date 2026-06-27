---
role: proof
locale: en
of_concept: projective-variety-homogeneous-coordinate-ring
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

Let $S = S(Y) = k[x_0, \ldots, x_n]/I(Y)$ be the homogeneous coordinate ring of $Y$. We think of $\mathcal{O}(Y)$, $K(Y)$ and $S(Y)$ all as subrings of the quotient field $L$ of $S(Y)$.

For (a), let $f \in \mathcal{O}(Y)$. Then on each standard open $U_i = Y \cap \{x_i \neq 0\}$, $f$ can be written as $g_i/h_i$ where $g_i, h_i \in S(Y)$ are homogeneous of the same degree. This means $f$ is an element of degree $0$ in the localization $S(Y)_{x_i}$ for each $i$. Thus for each $i$, there exist $N_i$ and homogeneous $F_i \in S(Y)_{N_i}$ such that $x_i^{N_i} f \in S(Y)_{N_i}$.

Choose $N \geqslant \sum N_i$. Then $S(Y)_N$ is spanned as a $k$-vector space by monomials of degree $N$ in $x_0, \ldots, x_n$, and in any such monomial, at least one $x_i$ occurs to a power $\geqslant N_i$. Thus we have $S(Y)_N \cdot f \subseteq S(Y)_N$.

Iterating, we have $S(Y)_N \cdot f^q \subseteq S(Y)_N$ for all $q > 0$. In particular, $x_0^N f^q \in S(Y)$ for all $q > 0$. This shows that the subring $S(Y)[f]$ of $L$ is contained in $x_0^{-N} S(Y)$, which is a finitely generated $S(Y)$-module. Since $S(Y)$ is a Noetherian ring, $S(Y)[f]$ is a finitely generated $S(Y)$-module, and therefore $f$ is integral over $S(Y)$.

This means there exist $a_1, \ldots, a_m \in S(Y)$ such that

$$f^m + a_1 f^{m-1} + \cdots + a_m = 0.$$

Since $f$ has degree $0$, we can replace the $a_i$ by their homogeneous components of degree $0$, and still have a valid equation. But $S(Y)_0 = k$, so the $a_i \in k$, and $f$ is algebraic over $k$. Since $k$ is algebraically closed, $f \in k$, which completes the proof of (a).

For (b) and (c), similar arguments using the graded localization $S_{(\mathfrak{p})}$ apply.
