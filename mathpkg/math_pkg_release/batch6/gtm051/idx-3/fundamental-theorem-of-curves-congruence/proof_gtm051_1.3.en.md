---
role: proof
locale: en
of_concept: fundamental-theorem-of-curves-congruence
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

Fix $t_0 \in I$. There is precisely one isometry $B$ satisfying
$$Bc(t_0) = \tilde{c}(t_0), \quad Re_i(t_0) = \tilde{e}_i(t_0), \quad 1 \leq i \leq n,$$
where $R$ is the orthogonal component of $B$. Since both Frenet frames are positively oriented, $R$ has determinant $+1$.

From the hypotheses we have $\tilde{\omega}_{ij}(t) = \omega_{ij}(t)$ (equal speeds and curvatures imply equal connection forms), which gives
$$\dot{\tilde{e}}_i(t) = \sum_j \omega_{ij}(t) \tilde{e}_j(t).$$
On the other hand,
$$R\dot{e}_i(t) = \sum_j \omega_{ij}(t) Re_j(t).$$
Thus $\tilde{e}_i(t)$ and $Re_i(t)$ satisfy the same system of linear differential equations. Since they are equal at $t = t_0$, uniqueness of solutions yields $Re_i(t) = \tilde{e}_i(t)$ for all $t \in I$.

In particular, $R\dot{c}(t) = |\dot{c}(t)|Re_1(t) = |\dot{c}(t)|\tilde{e}_1(t) = \dot{\tilde{c}}(t)$. Hence
$$Bc(t) - Bc(t_0) = \int_{t_0}^t R\dot{c}(\tau) \, d\tau = \int_{t_0}^t \dot{\tilde{c}}(\tau) \, d\tau = \tilde{c}(t) - \tilde{c}(t_0),$$
which proves $Bc(t) = \tilde{c}(t)$.

To see uniqueness, let $B'$ be another isometry with $B' \circ c = \tilde{c}$. Then $B'$ must transform the distinguished Frenet frame of $c$ into that of $\tilde{c}$, forcing $B' = B$.
