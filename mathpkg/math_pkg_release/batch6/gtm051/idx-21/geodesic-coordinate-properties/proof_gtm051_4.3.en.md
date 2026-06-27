---
role: proof
locale: en
of_concept: geodesic-coordinate-properties
source_book: gtm051
source_chapter: "4"
source_section: "4.3"
---

**Proof of Lemma 4.3.6.**

1. Since $c'(s_0) \neq 0$, we may assume, after possibly restricting the domain of definition of $c$, that $c'(s) \neq 0$ for $s \in \mathring{I}$. This being done, we may assert the existence of the Frenet frame $e_1(s), e_2(s)$. For each $s \in \mathring{I}$ let $c(t, s) = \tilde{f} \circ v(t, s)$ be the geodesic with $c(0, s) = c(s)$ and $(\partial c / \partial t)(0, s) = e_2(s)$. Each of these geodesics is defined for $t < \epsilon(s)$ and by shrinking the domain of definition of $c(s)$ again, if necessary, we may assume that there is an $\epsilon' > 0$ such that $\epsilon(s) > \epsilon'$ for $s \in \mathring{I}$.

2. The mapping $(t, s) \in (-\epsilon', \epsilon') \times \mathring{I} \mapsto (v^1(t, s), v^2(t, s)) \in V$ is differentiable because the $v^1(t, s)$ are solutions to the equation for geodesics and those solutions depend differentiably on the initial conditions.

Since $g^{12} = -g_{12}/\det(g_{ik})$, the equation above implies $g_{12}g_{21,1} = 0$ or $\frac{1}{2}(g_{12}^2)_{,1} = 0$. Since $g_{12}(0, u^2)$ is the inner product of $e_1(s)$ with $e_2(s)$ along $c(s)$ and hence equals $0$, it follows that $g_{12} = 0$. Of course, $g_{22} = \det(g_{ik}) > 0$. This proves (ii) and the first part of (iii). (To see that the curves $u^1 = a$ and $u^1 = b$ cut off an arc of length $b - a$ on any geodesic $u^2 = \text{constant}$, simply observe that $u^1 = s$ is arc length on the curve $u^2 = \text{constant}$.)

4. We now prove the second part of (iii). Suppose $g_{11} = 1$, $g_{12} = 0$, and $g_{22} > 0$. By (4.2.4), $\Gamma_{11}^1 = \Gamma_{11}^2 = 0$. Therefore $\nabla f_{u^1}/\partial u^1 = \sum_t \Gamma_{11}^t f_{u^t} = 0$. In other words, the curves $u^2 = \text{constant}$ are unit-speed geodesics cutting the curves $u^1 = \text{constant}$ orthogonally. Any one of the curves $u^1 = \text{constant}$ may serve as basis curve.

5. Suppose $c(s)$ is a unit-speed geodesic. Then

$$0 = \frac{d}{ds} (e_1(s) \cdot e_2(s)) = \frac{\nabla e_1}{ds} \cdot e_2 + \frac{\nabla e_2}{ds} \cdot e_1 = \frac{\nabla e_2}{ds} \cdot e_1.$$

Similarly, $\nabla e_2 / ds$ is perpendicular to $e_2$ itself, so $\nabla e_2 / ds$ vanishes on the basis curve. This implies that the Christoffel symbols vanish on the basis curve, completing the verification of the special case properties.
