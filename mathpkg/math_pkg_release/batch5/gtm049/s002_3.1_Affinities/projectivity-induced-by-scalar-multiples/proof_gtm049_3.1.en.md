---
role: proof
locale: en
of_concept: projectivity-induced-by-scalar-multiples
source_book: gtm049
source_chapter: "3"
source_section: "3.1 Affinities"
---

If $g = zf$ then $Mf = Mg$ for any subspace $M$ of $V$ and so $\mathcal{P}(f) = \mathcal{P}(g)$.

Conversely, suppose $\mathcal{P}(f) = \mathcal{P}(g)$. For any non-zero vector $a$ in $V$, the one-dimensional subspace $[a]$ satisfies $[a]f = [a]g$. Hence there exists a non-zero scalar $z_a$ such that $ag = z_a(af)$. If $a$ and $b$ are linearly independent, then $[a+b]f = [a+b]g$, so there exists a non-zero scalar $z_{a+b}$ such that $(a+b)g = z_{a+b}(a+b)f$. But $(a+b)g = ag + bg = z_a(af) + z_b(bf)$ and $z_{a+b}(a+b)f = z_{a+b}(af) + z_{a+b}(bf)$. Since $af$ and $bf$ are linearly independent (because $f$ is an isomorphism and $a, b$ are independent), we deduce $z_a = z_{a+b} = z_b$.

If $a$ and $b$ are linearly dependent we may use the above argument for the one-dimensional case to show that $z_a = z_b$. Alternatively, we may find a vector $c$ in $V$ not linearly dependent on $a$ or $b$, and deduce that $z_a = z_c$, $z_b = z_c$ whence $z_a = z_b$. This establishes the result.
