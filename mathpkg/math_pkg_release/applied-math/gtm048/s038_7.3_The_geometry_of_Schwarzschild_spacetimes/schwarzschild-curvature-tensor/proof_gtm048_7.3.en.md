---
role: proof
locale: en
of_concept: schwarzschild-curvature-tensor
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

Since the reader has worked through each step of Proposition 1.4.4, the computation of $\hat{R}$ follows by the same method applied to the Schwarzschild metric on $U = N \cup B$. The metric is given by

$$g = -\left(1 - \frac{2\mu}{r}\right) dt^2 + \left(1 - \frac{2\mu}{r}\right)^{-1} dr^2 + r^2 h$$

where $h$ is the standard round metric on $\mathcal{S}^2$. Define $j = g - r^2 P^* h$ and the $(4,0)$-tensor field $T$ by

$$T(X_1, X_2, X_3, X_4) = \frac{1}{4}\left\{[j(X_1, X_3)(P^* h)(X_2, X_4) - (1 \Leftrightarrow 2)] - [3 \Leftrightarrow 4]\right\}$$

for all $x \in U$ and $X_1, X_2, X_3, X_4 \in U_x$, where $(1 \Leftrightarrow 2)$ and $[3 \Leftrightarrow 4]$ denote interchange of the indicated indices. Then $T$ satisfies all symmetry properties stated in Section 1.0.2a-c. Let $\hat{R}: U \to T_4^0 U$ be the tensor field physically equivalent to the curvature tensor of $U$. A direct computation using the metric components, the connection coefficients, and the definition of the Riemann curvature tensor yields

$$\hat{R} = \frac{4\mu}{r^3}\left[2(dr \wedge dt) \otimes (dr \wedge dt) - r^2 T + 2r^4(P^* \zeta) \otimes (P^* \zeta)\right]$$

where $P: U \to \mathcal{S}^2$ is the projection onto the sphere factor and $\zeta$ is the standard area form on $\mathcal{S}^2$.
