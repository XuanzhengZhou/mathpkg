---
role: proof
locale: en
of_concept: schwarz-inequality-pure-potentials
source_book: gtm040
source_chapter: "8"
source_section: "5"
---

Form the approximations to $g$ and $\bar{g}$ using Lemma 8-56: let $\{E_n\}$ be an increasing sequence of finite sets with union $S$, and let $g^{(n)}$, $\bar{g}^{(n)}$ be the corresponding finite-restriction potentials. By Lemma 8-55, Schwarz's inequality holds for each pair $(g^{(n)}, \bar{g}^{(n)})$:

$$(g^{(n)}, \bar{g}^{(n)})^2 \leq \mathbf{I}(g^{(n)})\mathbf{I}(\bar{g}^{(n)}).$$

By Lemma 8-56, $(g^{(n)}, \bar{g}^{(n)}) \to (g, \bar{g})$ as $n \to \infty$. Also $\mathbf{I}(g^{(n)}) = (g^{(n)}, g^{(n)}) \to (g, g) = \mathbf{I}(g)$ and similarly for $\bar{g}$. Passing to the limit preserves the inequality, yielding $(g, \bar{g})^2 \leq (g, g)(\bar{g}, \bar{g})$. The finiteness of $(g, \bar{g})$ follows immediately.
