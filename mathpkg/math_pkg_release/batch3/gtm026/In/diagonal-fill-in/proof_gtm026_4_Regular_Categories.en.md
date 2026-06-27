---
role: proof
locale: en
of_concept: diagonal-fill-in
source_book: gtm026
source_chapter: "4"
source_section: "Regular Categories"
---

The uniqueness assertion is clear since $e$ is an epimorphism (4.3): if $e \cdot h = e \cdot h'$, then $h = h'$. Alternatively, since $m$ is a monomorphism, $h \cdot m = h' \cdot m$ implies $h = h'$. In fact, either triangle implies the other because $e \cdot h = f$ and composing with $m$ gives $e \cdot h \cdot m = f \cdot m$, while $h \cdot m = g$ and composing with $e$ gives $e \cdot h \cdot m = e \cdot g$, and since $f \cdot m = e \cdot g$, the two resulting equations are compatible.

To establish existence, let $(e_1, m_1)$ be the $E$-$M$ factorization of $g$ and let $(e_2, m_2)$ be the $E$-$M$ factorization of $f$, as shown in the diagram:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{e_2} \ar@/^1pc/[dd]^{f} & B \ar[d]^{m_2} \ar@/^1pc/[dd]^{g} \\
\cdot \ar[d]_{m_2} \ar[r]^{\psi} & \cdot \ar[d]^{m_1} \\
C \ar[r]_{m} & D
}$$

Then $(e \cdot e_1, m_1)$ and $(e_2, m_2 \cdot m)$ are both $E$-$M$ factorizations of $f \cdot m = e \cdot g$. By the uniqueness clause of (4.5), there exists an isomorphism $\psi$ such that $e \cdot e_1 \cdot \psi = e_2$ and $\psi \cdot m_2 \cdot m = m_1$. Define $h: B \longrightarrow C = e_1 \cdot \psi \cdot m_2$. Then:

$e \cdot h = e \cdot e_1 \cdot \psi \cdot m_2 = e_2 \cdot m_2 = f$, and

$h \cdot m = e_1 \cdot \psi \cdot m_2 \cdot m = e_1 \cdot m_1 = g$.

Thus $h$ satisfies the required equations.
