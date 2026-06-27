---
role: proof
locale: en
of_concept: cauchy-nets-product-characterization
source_book: gtm036
source_chapter: "7"
source_section: ""
---

In the product topology, convergence to $0$ is equivalent to coordinate-wise convergence to $0$. Thus $x_\alpha - x_\beta \to 0$ in the product topology iff for each $t \in A$, $x_\alpha(t) - x_\beta(t) \to 0$ in $E_t$, which is exactly the condition that $\{x_\alpha(t)\}$ is a Cauchy net in $E_t$ for each $t$.

If each $E_t$ is complete, then for each $t$, the Cauchy net $\{x_\alpha(t)\}$ converges to some $y_t \in E_t$. Define $y \in \prod E_t$ by $y(t) = y_t$. Then $x_\alpha \to y$ coordinate-wise, hence in the product topology. Thus the product is complete.

Conversely, if the product is complete, fix $t_0 \in A$. For any Cauchy net $\{z_\alpha\}$ in $E_{t_0}$, define a net in the product by setting the $t_0$-coordinate to $z_\alpha$ and all other coordinates to $0$. This net is Cauchy in the product, hence converges to some limit. The $t_0$-coordinate of the limit is the limit of $\{z_\alpha\}$ in $E_{t_0}$, showing $E_{t_0}$ is complete.
