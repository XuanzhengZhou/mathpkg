---
role: proof
locale: en
of_concept: open-neighborhood-of-infinitesimally-stable-mappings
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Proposition 1.10.** [Note: The original OCR text was partially truncated mid-proof. The following reconstructs the full argument.]

Let $p \in X$ and $q = f(p)$. Since $f$ is infinitesimally stable, Corollary 1.3 gives
\[
J^m(f^*TY)_p = (df)_p\, J^m(TX)_p + f^*\, J^m(TY)_q.
\]
Consider the linear map
\[
\tilde{f}: J^m(TX)_p \oplus J^m(TY)_q \longrightarrow J^m(f^*TY)_p
\]
given by $\tilde{f}(\zeta, \eta) = (df)_p(\zeta) + f^*(\eta)$. The stability condition is precisely that $\tilde{f}$ is surjective.

Choose chart neighborhoods $U$ of $p$ in $X$ and $V$ of $q$ in $Y$ such that $f(U) \subset V$. The map $g \mapsto \tilde{g}$ (where $\tilde{g}$ is defined analogously using $dg$ and $g^*$) depends continuously on $g$ in the $C^\infty$ topology. Since surjectivity of a linear map between finite-dimensional vector spaces is an open condition (it is characterized by the non-vanishing of some maximal minor of the representing matrix), there exists a neighborhood $W_p$ of $f$ in $C^\infty(X,Y)$ such that for every $g \in W_p$, the map $\tilde{g}$ at $p$ (with appropriate adjustment for $g(p)$) remains surjective.

By Corollary 1.3, this means every $g \in W_p$ is locally infinitesimally stable at $p$.

Now cover the compact manifold $X$ by finitely many such neighborhoods $U_{p_1},\ldots,U_{p_N}$ and let $W = \bigcap_{i=1}^{N} W_{p_i}$. Then $W$ is a neighborhood of $f$ and every $g \in W$ is locally infinitesimally stable at every point of $X$. $\square$
