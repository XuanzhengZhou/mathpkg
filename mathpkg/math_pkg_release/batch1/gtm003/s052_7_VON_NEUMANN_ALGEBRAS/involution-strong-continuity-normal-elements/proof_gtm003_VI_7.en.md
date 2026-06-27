---
role: proof
locale: en
of_concept: involution-strong-continuity-normal-elements
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

For arbitrary elements $x, y \in \mathcal{L}(H)$ we have the algebraic identity:
$$(x^* - y^*)(x - y) = x^*x - y^*y + y^*(y - x) + (y^* - x^*)y.$$

For $\xi \in H$, applying this to $\xi$ and taking inner products yields:
$$\|x\xi - y\xi\|^2 \leq \|x\xi\|^2 - \|y\xi\|^2 + 2\|\xi\| \|(y^* - x^*)y\xi\|.$$

Now restrict to normal elements: $x$ and $y$ are normal, i.e., $x^*x = xx^*$ and $y^*y = yy^*$. Under this restriction, one uses the identity to bound $\|x^*\xi - y^*\xi\|$ in terms of $\|x\xi - y\xi\|$ and related quantities. The estimate shows that if a net $(x_\alpha)$ of normal elements converges strongly to a normal element $x$, then $(x_\alpha^*)$ converges strongly to $x^*$, establishing the continuity of the involution on the set of normal elements for the strong operator topology.
