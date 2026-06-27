---
role: proof
locale: en
of_concept: canonical-isomorphism-bilinear-forms-linear-maps
source_book: gtm003
source_chapter: "III"
source_section: "Appendix: Tensor Products and Nuclear Spaces"
---

Let $E, F$ be locally convex spaces and let $v \in \mathcal{B}(E, F)$ be a separately continuous bilinear form. For each fixed $x \in E$, the map $y \mapsto v(x, y)$ is a continuous linear functional on $F$, hence defines an element $u(x) \in F'$ by the relation
$$\langle u(x), y \rangle = v(x, y) \qquad (y \in F).$$
The map $u \colon E \to F'$ so obtained is linear because $v$ is linear in its first argument. To see that $u$ is continuous when $F'$ carries the weak topology $\sigma(F', F)$, observe that for each $y \in F$, the scalar function $x \mapsto \langle u(x), y \rangle = v(x, y)$ is continuous on $E$ by separate continuity of $v$. Thus $u \in \mathcal{L}(E, F'_\sigma)$.

Conversely, given any $u \in \mathcal{L}(E, F'_\sigma)$, the formula $v(x, y) = \langle u(x), y \rangle$ defines a bilinear form on $E \times F$ which is separately continuous: for fixed $x$, $y \mapsto \langle u(x), y \rangle$ is continuous because $u(x) \in F'$, while for fixed $y$, $x \mapsto \langle u(x), y \rangle$ is continuous by continuity of $u$ into $F'_\sigma$. This establishes that $v \mapsto u$ is a bijective linear map, hence an algebraic isomorphism $\mathcal{B}(E, F) \cong \mathcal{L}(E, F'_\sigma)$.

By symmetry, the formula $\langle x, u'(y) \rangle = v(x, y)$ defines the adjoint $u' \in \mathcal{L}(F, E'_\sigma)$ and the map $v \mapsto u'$ gives the algebraic isomorphism $\mathcal{B}(E, F) \cong \mathcal{L}(F, E'_\sigma)$.

For the second assertion: $v$ is a *continuous* bilinear form (i.e., jointly continuous) if and only if there exists a $0$-neighborhood $U$ in $E$ such that $\sup_{x \in U} |v(x, y)| < \infty$ for $y$ in some $0$-neighborhood of $F$, which is equivalent to $u(U)$ being an equicontinuous subset of $F'$. Therefore the subspace of $\mathcal{L}(E, F'_\sigma)$ corresponding to $\mathcal{B}(E, F)$ consists of those $u$ that map some $0$-neighborhood in $E$ onto an equicontinuous set in $F'$.
