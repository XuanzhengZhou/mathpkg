---
role: proof
locale: en
of_concept: cx-closed-under-join
source_book: gtm043
source_chapter: "1"
source_section: "1.3"
---

If $f$ is continuous, then $|f|$ is continuous because it is the composition of $f$ with the continuous absolute value function on $\mathbf{R}$. Now for any $f, g \in C(X)$, the identity
$$f \vee g = \frac{1}{2}(f + g + |f - g|)$$
expresses $f \vee g$ as a combination of sums, scalar multiplication, and absolute value of continuous functions. Since all these operations preserve continuity, $f \vee g \in C(X)$. Therefore $C(X)$ is closed under the lattice join operation, and dually under the meet operation, making it a sublattice of $\mathbf{R}^X$.
