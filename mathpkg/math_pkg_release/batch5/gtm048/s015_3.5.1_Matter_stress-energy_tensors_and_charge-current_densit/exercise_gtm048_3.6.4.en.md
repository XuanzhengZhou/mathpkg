---
role: exercise
locale: en
chapter: "3"
section: "3.6"
exercise_number: 4
---

**(a)** Let $T$ be a $(p,q)$-tensor field on $M$ with $p > 0$. Let the components of $T$ be $T^{i_1 \dots i_p}_{j_1 \dots j_q}$. We define $\operatorname{div} T$ to be the $(p-1,q)$-tensor field given in components by

$$\left( \operatorname{div} T \right)^{i_1 \dots i_{p-1}}_{j_1 \dots j_q} = T^{i_1 \dots i_{p-1} k}_{j_1 \dots j_q | k}.$$

Show that for $q = 0$, this coincides with the definition given in Section 3.6.2.

**(b)** Show from the second Bianchi identity (Section 3.0.1d) that if $\hat{G}$ is the $(2,0)$-tensor field physically equivalent to the Einstein tensor $G$, then $\operatorname{div} \hat{G} = 0$.

**(c)** Let $C$ be a $(p,0)$-skew-symmetric tensor field. If $p \geq 2$, show $\operatorname{div} C = 0$.

Suppose $\omega$ is a $p$-form, $p \geq 1$. Let $\tilde{\omega}$ be the $(1, p-1)$-tensor field physically equivalent to $\omega$. Then $\operatorname{div} \tilde{\omega}$ is equal to $\delta \omega$ (up to a universal constant), where $\delta$ is the co-differential of Hodge theory which lowers the degree of forms by 1.

**(d)** Suppose that for $A \in \{1, 2\}$, $\eta_A$ is a function $M \to \mathbb{R}^4$ and $P_A$ is a vector field. Use the definitions, the $\mathbb{R}$-linearity and Leibniz properties of a covariant derivative, and (a) to show:

$$\operatorname{div}\left( \eta_1 P_1 \otimes P_1 + \eta_2 P_2 \otimes P_2 \right) = \left[ \operatorname{div}\left( \eta_1 P_1 \right) \right] P_1 + \eta_1 D_{P_1} P_1 + \left[ \operatorname{div}\left( \eta_2 P_2 \right) \right] P_2 + \eta_2 D_{P_2} P_2.$$
