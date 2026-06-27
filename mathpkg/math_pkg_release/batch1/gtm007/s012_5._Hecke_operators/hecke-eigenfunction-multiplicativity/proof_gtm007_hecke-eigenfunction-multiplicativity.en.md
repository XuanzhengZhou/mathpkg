---
role: proof
locale: en
of_concept: hecke-eigenfunction-multiplicativity
source_book: gtm007
source_chapter: "VII"
source_section: "5.4"
---
By Theorem 7(b), for a normalized eigenfunction we have $c(n) = \lambda(n)$ for all $n$. The Hecke operators satisfy:
\begin{itemize}
\item $T(m)T(n) = T(mn)$ when $(m,n) = 1$,
\item $T(p)T(p^n) = T(p^{n+1}) + p^{2k-1}T(p^{n-1})$ for $p$ prime, $n \geq 1$.
\end{itemize}
Applying these operator identities to the eigenfunction $f$ and using $T(n)f = \lambda(n)f$, the eigenvalues satisfy the same relations. Therefore, since $c(n) = \lambda(n)$, the coefficients satisfy:
\begin{align*}
c(mn) &= c(m)c(n) \quad \text{if } (m,n) = 1,\\
c(p)c(p^n) &= c(p^{n+1}) + p^{2k-1}c(p^{n-1}) \quad (p \text{ prime}, n \geq 1).
\end{align*}
These are exactly formulas (79) and (80) from Theorem 7. In particular, the first formula shows that $n \mapsto c(n)$ is a multiplicative arithmetic function.
