---
role: proof
locale: en
of_concept: collar-theorem
source_book: gtm033
source_chapter: "IV"
source_section: "6"
---

# Proof of Collar Theorem (Theorem 6.1)

**Theorem (6.1).** Every $C^\infty$ manifold with boundary admits a collar neighborhood of its boundary.

*Proof.* A proof using differential equations is given in Section 5.2. An alternative proof using retractions and partitions of unity is outlined as follows.

**Step 1: Local retraction onto the boundary.** Find a $C^\infty$ retraction $r: W \to \partial M$ of a neighborhood of $\partial M$ onto $\partial M$. This is obviously possible locally, and two local retractions into coordinate domains can be glued together with a bump function. A standard globalization technique (e.g., Theorem 2.2.11) produces a global retraction defined on a neighborhood $W$ of $\partial M$.

**Step 2: A distance function.** Find a neighborhood $U \subset M$ of $\partial M$ and a map

$$g: U \to [0, \infty),$$

with $g(\partial M) = 0$ having $0$ as a regular value. This is easily done with a partition of unity.

**Step 3: Combining the maps.** Observe that the map

$$h = (r, g): W \cap U \to \partial M \times [0, \infty)$$

maps a neighborhood of $\partial M$ diffeomorphically onto a neighborhood of $\partial M \times \{0\}$ in $\partial M \times [0, \infty)$, and $h(x) = (x, 0)$ for $x \in \partial M$.

**Step 4: Obtaining the collar.** Finally, let $\varphi: \partial M \times [0, \infty) \to h(W \cap U)$ be an embedding which fixes $\partial M \times \{0\}$ pointwise. Then

$$h^{-1} \circ \varphi: \partial M \times [0, \infty) \to M$$

is a collar of $\partial M$ in $M$. ∎

**Remark.** It is also true that boundaries of $C^0$ manifolds have collars, although this is far from obvious. An elegant and surprising proof is given by M. Brown [2].
