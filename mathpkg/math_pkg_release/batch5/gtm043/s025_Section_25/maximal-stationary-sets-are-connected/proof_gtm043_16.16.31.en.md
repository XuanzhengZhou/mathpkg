---
role: proof
locale: en
of_concept: maximal-stationary-sets-are-connected
source_book: gtm043
source_chapter: "16"
source_section: "16.31"
---
If $S$ is a maximal stationary set of $A$, then $S = \bigcap_{f \in A} Z(f - r)$, which reduces to $S = \bigcap_{g} Z(g)$ where $g \in A$, $g \geq 0$, and $g[S] = \{0\}$. Since $Z(g) = \bigcap_{\epsilon > 0} \{x: g(x) \leq \epsilon\}$, we get $S = \bigcap_{g, \epsilon} \{x: g(x) \leq \epsilon\}$. Any finite intersection of such sets is a neighborhood of $S$; if $S$ were disconnected, it could be separated by a partition from such an intersection, contradicting maximality.
