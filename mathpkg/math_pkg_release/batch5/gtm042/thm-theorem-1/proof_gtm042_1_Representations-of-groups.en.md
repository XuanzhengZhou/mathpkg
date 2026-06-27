---
role: proof
locale: en
of_concept: thm-theorem-1
source_book: gtm042
source_chapter: "1"
source_section: "Representations of groups"
---

Let $W'$ be an arbitrary complement of $W$ in $V$, and let $p$ be the corresponding projection of $V$ onto $W$. Form the average $p^0$ of the conjugates of $p$ by the elements of $G$:

$$p^0 = \frac{1}{g} \sum_{t \in G} \rho_t \cdot p \cdot \rho_t^{-1} \quad (g \text{ being the order of } G).$$

Since $p$ maps $V$ into $W$ and $\rho_t$ preserves $W$ we see that $p^0$ maps $V$ into $W$; we have $\rho_t^{-1} x \in W$ for $x \in W$, whence

$$p \cdot \rho_t^{-1} x = \rho_t^{-1} x, \quad \rho_t \cdot p \cdot \rho_t^{-1} x = x, \quad \text{and} \quad p^0 x = x.$$

Thus $p^0$ is a projection of $V$ onto $W$, corresponding to some complement $W^0$ of $W$. We have moreover

$$\rho_s \cdot p^0 = p^0 \cdot \rho_s \quad \text{for all } s \in G.$$

Indeed, computing $\rho_s \cdot p^0 \cdot \rho_s^{-1}$, we find:

$$\rho_s \cdot p^0 \cdot \rho_s^{-1} = \frac{1}{g} \sum_{t \in G} \rho_s \cdot \rho_t \cdot p \cdot \rho_t^{-1} \cdot \rho_s^{-1} =
