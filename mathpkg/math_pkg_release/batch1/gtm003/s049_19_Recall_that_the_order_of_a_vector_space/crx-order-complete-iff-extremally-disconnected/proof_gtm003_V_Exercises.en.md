---
role: proof
locale: en
of_concept: crx-order-complete-iff-extremally-disconnected
source_book: gtm003
source_chapter: "V"
source_section: "Exercises"
---

If $X$ is extremally disconnected, the closure of every open set is open. For any bounded subset $A \subset \mathcal{C}_{\mathbf{R}}(X)$ bounded above, the pointwise supremum $s(x) = \sup\{f(x) : f \in A\}$ is upper semicontinuous, and by extremal disconnectedness its regularization is continuous, providing the supremum in $\mathcal{C}_{\mathbf{R}}(X)$.

Conversely, if $\mathcal{C}_{\mathbf{R}}(X)$ is order complete, then for any open set $U \subset X$, the characteristic function $\chi_U$ (as a lower semicontinuous function) is the supremum of $\{f \in \mathcal{C}_{\mathbf{R}}(X) : 0 \leq f \leq \chi_U\}$, so its closure $\overline{U}$ must be open, hence $X$ is extremally disconnected.
