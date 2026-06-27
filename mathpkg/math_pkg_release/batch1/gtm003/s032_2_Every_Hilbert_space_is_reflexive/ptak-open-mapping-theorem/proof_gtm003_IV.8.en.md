---
role: proof
locale: en
of_concept: ptak-open-mapping-theorem
source_book: gtm003
source_chapter: "IV"
source_section: "8"
---

The general case can be reduced to the case in which $u$ is one-to-one, for by (7.2) the null space $N$ of $u$ is closed in $E$, $E/N$ is a Ptak space by (8.3), Corollary 3, and the biunivocal map associated with $u$ is by (7.2) densely defined, has a closed graph, and is obviously nearly open if $u$ is.

We assume, hence, that $u$ is biunivocal with domain $E_0$ dense in $E$ and graph closed in $E \times F$. To prove $u$ is open, it suffices to show that $u_0$ is open. Let $U$ be any closed, convex $0$-neighborhood in $E/N$; if $V = u_0(U)$, then $\bar{V}$ is a $0$-neighborhood in $F$. Denote by $u'_0$ the adjoint of $u_0$; by the corollary of (2.3), $Q = u'_0(F')$ is a dense subspace of $N^\circ \subset E'_\sigma$. By (2.3)(a) we have

$$(u'_0)^{-1}(U^\circ) = [u_0(U)]^\circ = V^\circ = \bar{V}^\circ.$$

Thus $V^\circ$ is closed and equicontinuous, and therefore compact in $F'_\sigma$; $u'_0$ being continuous for $\sigma(F', F)$ and $\sigma(E', E)$, it follows that $u'_0(V^\circ) = U^\circ \cap Q$ is compact and hence closed in $E'_\sigma$. $U$ being arbitrary, the assumed B-completeness of $E$ implies that $Q$ is closed in $E'_\sigma$ (hence $Q = N^\circ$); thus $u_0$ is a weak isomorphism by the corollary of (7.3). Since $U$ is closed in $E/N$, it is weakly closed (by convexity), which implies that $V = u_0(U)$ is weakly closed in $F$, whence $V = \bar{V}$; it follows that $u_0$ is open.

For $E$ being $B_r$-complete when $u$ is one-to-one, the same argument shows $Q$ is dense and relatively weakly closed on equicontinuous sets, so $Q = N^\circ$ by $B_r$-completeness.
