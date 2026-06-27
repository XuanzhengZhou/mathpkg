---
role: proof
locale: en
of_concept: elementary-cycle-iff-circuit
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

**Forward direction:** If $\{e_1, \ldots, e_k\}$ are the edges of a circuit, then in the submultigraph $\Gamma_Z$, each vertex $x_i$ in the circuit is incident with exactly two of these edges (namely $e_i$ and $e_{i+1}$, indices modulo $k$). Hence $\sum_{e \in Z} f(e) = \varnothing$ (each vertex appears with coefficient 0 in the sum), so $Z$ is a cycle. Since the edges are distinct and the circuit is nontrivial, $Z$ is an elementary cycle.

**Partial converse:** Assume $Z$ is an elementary cycle of $\Gamma$. Since $\sum_{e \in Z} f(e) = \varnothing$, the vertices of $\Gamma_Z$ all have valence 2 or more (each vertex appearing in $Z$ must be incident with at least two edges from $Z$ to cancel in the sum). By Exercise A6a (if every vertex has valence $\geq 2$, then $\Gamma$ contains a circuit), $\Gamma_Z$ contains a circuit whose edges form a cycle $Z' \in \mathcal{L}(\Gamma_Z) \subseteq \mathcal{L}(\Gamma)$. Clearly $Z' \subseteq Z$. Since $Z$ is elementary (minimal as a cycle), $Z' = Z$, and $\Gamma_Z$ is a circuit.

The converse is only partial: it holds for elementary cycles but not for arbitrary cycles. For example, the union of two disjoint circuits gives a cycle $Z$ for which $\Gamma_Z$ is not a single circuit.
