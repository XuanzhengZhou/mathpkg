---
role: exercise
locale: en
chapter: "VI"
section: "1"
exercise_number: 3
---

Apply Exercise 2 with the following data: $X = G(s, V)$, $x$ is an $s$-dimensional subspace $K$ of $V$, $Y = \operatorname{Hom}(V, W)$, $y$ is a linear map $A \in \operatorname{Hom}(V, W)$ with $\operatorname{Ker} A = K$, $Z = L^0(Q, W)$, and $z = A \circ \pi$ where $\pi$ is as in Proposition 1.4. (Note that $V/K$ is the fiber of $Q$ above $x$ and $L^0(V/K, W)$ is the fiber of $Z$ above $x$.) Let $\rho = \pi^*: L^0(Q, W) \to \operatorname{Hom}(V, W)$ and let $\sigma: L^0(Q, W) \to G(s, V)$ be the canonical projection. Note that $T_y Y = T_A \operatorname{Hom}(V, W) \cong \operatorname{Hom}(V, W)$ and

$$
T_z Z_x = T_{A \circ \pi} \operatorname{Hom}(V/K, W) \cong \operatorname{Hom}(V/K, W)
$$

since $\operatorname{Hom}$ spaces are vector spaces.

(i) Show that $(d\rho)_z: T_z Z_x \to T_y Y$ is an injection. In particular show that the image consists of all maps containing $K$ in their kernels.

(ii) From (i) conclude that $(d\rho)_z(T_z Z_x) \cong \operatorname{Hom}(V/K, W)$.

(iii) Finally conclude that $T_y Y / (d\rho)_z(T_z Z_x) \cong \operatorname{Hom}(K, W)$.

Moreover, show that all these identifications are canonical.
