---
role: proof
locale: en
of_concept: stable-complement-theorem
source_book: gtm042
source_chapter: "1"
source_section: "1.3"
---

Let $W'$ be an arbitrary complement of $W$ in $V$, and let $p$ be the corresponding projection of $V$ onto $W$. Form the average $p^0$ of the conjugates of $p$ by the elements of $G$:

$$p^0 = \frac{1}{g} \sum_{t \in G} \rho_t \cdot p \cdot \rho_t^{-1}$$

where $g$ is the order of $G$. Since $p$ maps $V$ into $W$ and $\rho_t$ preserves $W$, we see that $p^0$ maps $V$ into $W$. For $x \in W$, we have $\rho_t^{-1} x \in W$, whence

$$p \cdot \rho_t^{-1} x = \rho_t^{-1} x, \quad \rho_t \cdot p \cdot \rho_t^{-1} x = x, \quad \text{and} \quad p^0 x = x.$$

Thus $p^0$ is a projection of $V$ onto $W$, corresponding to some complement $W^0$ of $W$. We have moreover

$$\rho_s \cdot p^0 = p^0 \cdot \rho_s \quad \text{for all } s \in G.$$

Indeed, computing $\rho_s \cdot p^0 \cdot \rho_s^{-1}$:

$$\rho_s \cdot p^0 \cdot \rho_s^{-1} = \frac{1}{g} \sum_{t \in G} \rho_s \cdot \rho_t \cdot p \cdot \rho_t^{-1} \cdot \rho_s^{-1} = \frac{1}{g} \sum_{t \in G} \rho_{st} \cdot p \cdot \rho_{st}^{-1} = p^0.$$

Thus $\rho_s \cdot p^0 = p^0 \cdot \rho_s$. If $x \in W^0$, then $p^0 x = 0$, so $p^0 \cdot \rho_s x = \rho_s \cdot p^0 x = 0$, which shows $\rho_s x \in W^0$. Hence $W^0$ is stable under $G$, completing the proof.
