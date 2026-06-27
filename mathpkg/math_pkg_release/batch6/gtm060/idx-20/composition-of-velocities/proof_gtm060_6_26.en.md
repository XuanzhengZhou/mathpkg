---
role: proof
locale: en
of_concept: composition-of-velocities
source_book: gtm060
source_chapter: "6"
source_section: "26"
---

The general case is reduced to the two special cases (pure rotation and pure translation) by introducing an auxiliary coordinate system $K_1$ which moves by translation with respect to $k$ and with respect to which $K$ moves by rotating around $0 \in K_1$.

For pure rotation (the moving system $K$ rotates relative to $0 \in k$), we have $q = BQ$, hence
$$
v = \dot{q} = \dot{B} Q + B \dot{Q}.
$$
Identifying $\dot{B}Q = [\omega, q]$ (from the property $\dot{B}X = B[\Omega, X] = [\omega, BX]$) and $B\dot{Q} = v'$, we obtain $v = v' + v_n$ with $v_n = [\omega, q]$.

For the general case with translation $q = BQ + r$, applying the same reasoning to the composition through the auxiliary frame $K_1$ yields the full decomposition
$$
v = v' + v_n + v_0,
$$
with $v_0 = \dot{r}$ being the translational velocity of the moving coordinate system's origin.
