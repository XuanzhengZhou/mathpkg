---
role: proof
locale: en
of_concept: trivial-full-enlargement-implies-finite
source_book: gtm022
source_chapter: "VIII"
source_section: "4"
---

$\mathbb{S}$ is a definable subset with description $p(x) = {\sim}F$. If the enlargement is trivial, then $*\mathbb{S} = \mathbb{S}$, so no new elements are added. If $\mathbb{S}$ were infinite, then the binary relation $\rho(x, y) = (x \in \mathbb{S}) \wedge (y \in \mathbb{S}) \wedge (x \neq y)$ would be concurrent (since for any finite set $\{x_1, \ldots, x_n\} \subseteq \mathbb{S}$, there exists $y \in \mathbb{S}$ distinct from all $x_i$, so $\rho(x_i, y)$ holds). Then the full enlargement would introduce a new constant $c_\rho$ witnessing this concurrency, giving an element $c_\rho \in *\mathbb{S}$ with $c_\rho \notin \mathbb{S}$, contradicting triviality. Hence $\mathbb{S}$ is finite.
