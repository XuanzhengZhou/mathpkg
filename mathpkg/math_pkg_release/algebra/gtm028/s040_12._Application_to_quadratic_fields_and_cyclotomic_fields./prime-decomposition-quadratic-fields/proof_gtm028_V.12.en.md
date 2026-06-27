---
role: proof
locale: en
of_concept: prime-decomposition-quadratic-fields
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

The proof proceeds by analyzing the decomposition of rational primes in $K = \mathbb{Q}(\sqrt{m})$ in terms of the factorization of the minimal polynomial modulo $p$.

Let $R$ be the ring of integers of $K$. The discriminant $\mathfrak{d}$ of $R$ over $\mathbb{Z}$ is computed from the criterion for algebraic integers: if $m \equiv 1 \pmod{4}$, then $\{1, \frac{1}{2}(1+\sqrt{m})\}$ is an integral basis and $\mathfrak{d} = m$; if $m \equiv 2, 3 \pmod{4}$, then $\{1, \sqrt{m}\}$ is an integral basis and $\mathfrak{d} = 4m$.

For an odd prime $p$, the decomposition type is determined by whether $p$ divides $\mathfrak{d}$ and by the Legendre symbol $\left(\frac{m}{p}\right)$. If $p \mid \mathfrak{d}$, then $p$ divides the discriminant, which is equivalent to $p$ being ramified in $K$ (by the general theory of Dedekind domains, the ramified primes are precisely the divisors of the discriminant).

If $p \nmid \mathfrak{d}$, then $p$ is unramified. The ring $R/pR$ is a direct sum of fields, each isomorphic to the finite field with $p^f$ elements, where $f$ is the relative degree. The number of components $g$ satisfies $fg = 2$ (since $[K:\mathbb{Q}] = 2$). The minimal polynomial of a generator of $R$ over $\mathbb{Z}$ reduces modulo $p$, and its factorization determines the decomposition:
\begin{itemize}
\item If the polynomial splits into distinct linear factors modulo $p$, then $g = 2$, $f = 1$ (decomposed case).
\item If the polynomial remains irreducible modulo $p$, then $g = 1$, $f = 2$ (inertial case).
\end{itemize}

This factorization is equivalent to whether $m$ is a quadratic residue modulo $p$: the polynomial $X^2 - m$ splits if and only if $\left(\frac{m}{p}\right) = 1$, and it is irreducible if and only if $\left(\frac{m}{p}\right) = -1$.

For the prime $2$, when $m \equiv 1 \pmod{4}$, the prime $2$ does not divide $\mathfrak{d} = m$, so it is unramified. In this case $\{1, \frac{1}{2}(1+\sqrt{m})\}$ is an integral basis. The minimal polynomial of $\frac{1}{2}(1+\sqrt{m})$ over $\mathbb{Q}$ is $X^2 - X - (m-1)/4$. Modulo $2$, this polynomial reduces to $X^2 - X - (m-1)/4 \equiv X^2 + X + (m-1)/4 \pmod{2}$. This polynomial is reducible over $\mathbb{Z}/(2)$ if and only if $(m-1)/4$ is even, i.e., $m \equiv 1 \pmod{8}$. Thus $2$ is decomposed if $m \equiv 1 \pmod{8}$ and inertial if $m \equiv 5 \pmod{8}$.
