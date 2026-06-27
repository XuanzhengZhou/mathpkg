---
role: proof
locale: en
of_concept: uniqueness-haar-measure-locally-compact
source_book: gtm018
source_chapter: "X"
source_section: "60. Uniqueness"
---

If $S_0$ is the class of all Baire sets in $X$, then $(X, S_0, \mu)$ and $(X, S_0, \nu)$ are measurable groups and hence, by Theorem B, $\mu(E) = c\,\nu(E)$ for every Baire set $E$, with a nonnegative finite constant $c$; the fact that $c$ is positive may be inferred by choosing $E$ to be any bounded open Baire set. Any two regular Borel measures that agree on all Baire sets must agree on all Borel sets (by regularity, each Borel set is approximated from within by compact Baire sets and from without by open Baire sets). Hence $\mu(E) = c\,\nu(E)$ for every Borel set $E$.

---

An alternative approach, applicable more generally to not necessarily finite measures, proceeds as follows. Suppose first that $\mu$ and $\nu$ are left invariant measures such that $\nu \ll \mu$; then there exists a nonnegative integrable function $f$ such that
$$
\nu(E) = \int_E f(x)\, d\mu(x)
$$
for every measurable set $E$. It follows that
$$
\nu(yE) = \int_{yE} f(x)\, d\mu(x) = \int_E f(y^{-1}x)\, d\mu(x),
$$
and hence, since $\nu$ is left invariant, $f(x) = f(y^{-1}x)$ $[\mu]$. If $N_t = \{x : f(x) < t\}$, then
$$
\mu(yN_t - N_t) = \mu\bigl(\{x : f(y^{-1}x) < t\} - \{x : f(x) < t\}\bigr) = 0,
$$
and hence, for each real number $t$, either $\mu(N_t) = 0$ or $\mu(N_t') = 0$. Since this implies that $f$ is constant a.e.\ $[\mu]$, it follows that $\nu = c\,\mu$. To treat the general, not necessarily absolutely continuous, case, replace $\mu$ by $\mu + \nu$. Just as in §59.4, these considerations may be extended to apply to not necessarily finite cases also.
