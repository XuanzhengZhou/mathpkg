---
role: proof
locale: en
of_concept: jet-space-characterization-of-infinitesimal-stability
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Corollary 1.3.** By Theorem 1.2, $[f]_p$ is infinitesimally stable if and only if the equations $(**)$ can be solved to order $m$. The equations $(**)$ solvable to order $m$ means precisely that for any $\tau \in C^\infty(f^*TY)_p$, there exist $\zeta \in C^\infty(TX)_p$ and $\eta \in C^\infty(TY)_q$ such that
\[
\tau - \bigl((df)(\zeta) + f^*\eta\bigr) \in \mathfrak{m}_p^{m+1} \cdot C^\infty(f^*TY)_p,
\]
where $\mathfrak{m}_p$ is the maximal ideal of germs vanishing at $p$. Passing to the quotient by $\mathfrak{m}_p^{m+1}$ gives exactly the $m$-jet space $J^m(f^*TY)_p$. Thus the condition is equivalent to
\[
J^m(f^*TY)_p = (df)_p\, J^m(TX)_p + f^*\, J^m(TY)_q,
\]
where $(df)_p: J^m(TX)_p \to J^m(f^*TY)_p$ and $f^*: J^m(TY)_q \to J^m(f^*TY)_p$ are the maps induced on $m$-jets. $\square$
