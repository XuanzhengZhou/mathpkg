---
role: proof
locale: en
of_concept: polynomial-depends-on-finite-variables
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

Let $f \in S$ be a polynomial. By definition, $(i)f = 0$ for all but a finite number of multi-indices $(i) \in I_E$. Let $\{(i^{(1)}), \dots, (i^{(r)})\}$ be the finite set of multi-indices for which $(i)f \neq 0$. For each such multi-index $(i^{(k)})$, only finitely many coordinates $i^{(k)}_\alpha$ are non-zero. Taking the union over all $k = 1, \dots, r$, let $\{\beta_1, \dots, \beta_n\} \subseteq E$ be the finite set of all $\alpha \in E$ such that $i^{(k)}_\alpha \neq 0$ for some $k$.

Then for any $\alpha \notin \{\beta_1, \dots, \beta_n\}$, the indeterminate $X_\alpha$ does not appear in any monomial of $f$. Hence $f$ lies in the subring $R[X_{\beta_1}, \dots, X_{\beta_n}]$, which is isomorphic to the ordinary polynomial ring in $n$ variables. Since every $f \in S$ lies in some such finitely-generated subring, $S$ is the union of all its finitely-generated polynomial subrings.
