---
role: proof
locale: en
of_concept: z2-orientation-and-equivalent-conditions-for-orientability
source_book: gtm020
source_chapter: "4"
source_section: "4.3"
---

Let $\omega_x$ be the nonzero element of $H_n(M, M - x; \mathbf{Z}_2)$. For a ball $W$ around $x$ in the domain of a chart, we have $H_n(M, M - W; \mathbf{Z}_2) = \mathbf{Z}_2$, and the nonzero element maps onto $\omega_y$ for each $y \in W$. This proves the first statement (every manifold has a unique $\mathbf{Z}_2$-orientation).

For the equivalence of statements (1) to (3), we prove (2) $\implies$ (1) $\implies$ (2) and (2) $\iff$ (3).

\textbf{(2) $\implies$ (1):} Assuming (2), for a $\mathbf{Z}$-orientation of $M$ we define
$$\omega_x = (\phi^{-1})_*(\alpha_n),$$
where $\alpha_n \in H_n(\phi(U), \phi(U) - \phi(x))$ is the canonical class used in Theorem 3.4, and $(U, \phi) \in \mathcal{A}$. By Theorem 3.4 and the hypothesis (2) that change of coordinates is orientation preserving, the local class $\omega$ is consistent across chart overlaps and thus defines a well-defined orientation. Hence $M$ is orientable.

\textbf{(1) $\implies$ (2):} Conversely, let $\mathcal{A}$ be the atlas consisting of those charts such that $\omega_x = (\phi^{-1})_*(\alpha_n)$ for $x \in U$ and $\alpha_n \in H_n(\phi(U), \phi(U) - \phi(x))$ being the canonical generator. This atlas satisfies the condition in (2). This verifies the equivalence of (1) and (2).

\textbf{(2) $\iff$ (3):} To see that (2) implies (3), observe that the transition functions $D(\psi \circ \phi^{-1})(\phi(x))$ for $x \in U \cap V$ have a positive determinant and are therefore homotopic to transition functions in $\mathrm{SO}(n)$. This gives a reduction of the structure group of $\tau(M)$ from $\mathrm{GL}(n)$ to $\mathrm{SO}(n)$. Conversely, if $\tau(M)$ has $\mathrm{SO}(n)$ as structure group, then there exists an atlas whose transition functions take values in $\mathrm{SO}(n)$, automatically satisfying $\det > 0$.

Finally, if $M$ is connected, the choices of generator $\pm 1$ in $H_n(M, M - x; \mathbf{Z}) \cong \mathbf{Z}$ at a single point determine the orientation globally. Since the fundamental class must be consistent across the manifold, there are precisely two generators at each point, giving exactly two orientations.
