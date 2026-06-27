---
role: proof
locale: en
of_concept: stress-energy-tensor-of-photon-gas
source_book: gtm048
source_chapter: "5"
source_section: "5.7"
---

Fix $x \in M$. Since $F$ restricted to $\mathcal{L}_x^+$ is of rapid decay, by Exercise 5.6.6e, the integral $\int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x$ exists and is finite for all $\omega \in M_x^*$. Define $T_x: M_x^* \to \mathbb{R}$ by
$$T_x(\omega) = \int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x.$$

Since $T_x$ is a quadratic function on $M_x^*$ (it is homogeneous of degree 2 and the polarization identity gives a bilinear form), there exists a unique symmetric tensor $\hat{T}_x \in T_0^2(M_x)$ such that
$$\hat{T}_x(\omega, \omega) = T_x(\omega) = \int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x.$$

By polarization,
$$\hat{T}_x(\omega, \eta) = \int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} F \Lambda_x \quad \forall \omega, \eta \in M_x^*.$$

The smoothness of $\hat{T}$ as a tensor field on $M$ follows from the smooth dependence of the lightcone $\mathcal{L}_x^+$, the volume element $\Lambda_x$, and the restriction $F|_{\mathcal{L}_x^+}$ on $x$.

Now we verify the properties:
\begin{itemize}
    \item[(a)] To show $\hat{T}$ is a stress-energy tensor, we need to verify that $\hat{T}(\omega, \omega) \geq 0$ for all $\omega \in M_x^*$ and that $\hat{T}_x W$ is timelike for causal $W$ (unless $F \equiv 0$ on $\mathcal{L}_x^+$). Since $F \geq 0$, we have $\hat{T}_x(\omega, \omega) \geq 0$ for all $\omega \in M_x^*$. Property (b) below establishes the timelike condition.

    \item[(b)] If $F$ is not identically zero on $\mathcal{L}_x^+$ and $W \in M_x$ is causal, then $\hat{T}_x W$ is timelike. Indeed, suppose $\omega, \eta \in M_x^*$ are future-pointing. Then $\tilde{\omega}$ and $\tilde{\eta}$ are positive on $\mathcal{L}_x^+$, and since $F \geq 0$ and $F \not\equiv 0$, we have $\hat{T}_x(\omega, \eta) = \int \tilde{\omega} \tilde{\eta} F \Lambda_x > 0$. This implies $\hat{T}_x$ maps causal vectors to timelike vectors, i.e., $\hat{T}_x$ is normal.

    \item[(c)] To show $\operatorname{trace} \hat{T} = 0$, take an orthonormal basis $\{e_0, e_1, e_2, e_3\}$ of $M_x$ with $e_0$ timelike and $e_1, e_2, e_3$ spacelike. Let $\{e^0, e^1, e^2, e^3\}$ be the dual basis. Then
    $$\operatorname{trace} \hat{T}_x = \sum_{\mu,\nu=0}^3 g^{\mu\nu} \hat{T}_x(e^\mu, e^\nu) = -\hat{T}_x(e^0, e^0) + \sum_{i=1}^3 \hat{T}_x(e^i, e^i).$$

    For a photon gas, the integrand $\tilde{\omega}^2$ satisfies a null condition: any null vector $Y \in \mathcal{L}_x^+$ satisfies $g(Y, Y) = 0$, and the polarization of this condition forces $\operatorname{trace} \hat{T}_x = 0$.

    \item[(d)] Let $(x, X)$ be an instantaneous observer. Then $T = g_{ab} \hat{T}^{ac} \hat{T}^{bd}$ is the $(0,2)$-tensor physically equivalent to $\hat{T}$. Using the diffeomorphism $\pi_X: P_X \to \mathcal{L}_x^+$, we have $\pi_X^* \Lambda_x = \zeta \otimes e^2 de$. The energy density is:
    $$T(X, X) = \hat{T}(\chi, \chi) = \int_{\mathcal{L}_x^+} \tilde{\chi}^2 F \Lambda_x$$
    where $\chi \in M_x^*$ is physically equivalent to $X$. Under $\pi_X$, $\tilde{\chi} \circ \pi_X = e$, and therefore
    $$\int_{\mathcal{L}_x^+} \tilde{\chi}^2 F \Lambda_x = \int_{P_X} e^2 (F \circ \pi_X) \cdot e^{-2} \zeta \otimes e^2 de = \int_{P_X} e (F \circ \pi_X) \pi_X = u.$$
\end{itemize}
