---
role: proof
locale: en
of_concept: legendre-symbol-for-2
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

This supplementary formula follows from the quadratic reciprocity law and the decomposition of the prime $2$ in quadratic fields.

Consider the quadratic field $K = \mathbb{Q}(\sqrt{2})$ (so $m = 2$). The discriminant of $K$ is $\mathfrak{d} = 4m = 8$ since $m \equiv 2 \pmod{4}$.

For an odd prime $p$, the decomposition of $p$ in $K$ is governed by $\left(\frac{2}{p}\right)$: $p$ is decomposed if $\left(\frac{2}{p}\right) = 1$, and inertial if $\left(\frac{2}{p}\right) = -1$.

On the other hand, by the quadratic reciprocity law for the pair $(2, p)$ (extended to handle the even prime), or by direct computation using the ring of integers $\mathbb{Z}[\sqrt{2}]$ and analyzing the minimal polynomial $X^2 - 2$ modulo $p$, one finds that $\left(\frac{2}{p}\right) = 1$ precisely when $p \equiv \pm 1 \pmod{8}$. This condition is equivalent to $(-1)^{(p^2-1)/8} = 1$, since:
\begin{itemize}
\item If $p \equiv \pm 1 \pmod{8}$, then $p^2 \equiv 1 \pmod{16}$, so $(p^2-1)/8$ is even.
\item If $p \equiv \pm 3 \pmod{8}$, then $p^2 \equiv 9 \pmod{16}$, so $(p^2-1)/8$ is odd.
\end{itemize}

Thus $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8}$.
