---
role: proof
locale: en
of_concept: hadamard-theorem
source_book: gtm051
source_chapter: "6"
source_section: "6.6"
---

**1. $\exp_p$ is a local diffeomorphism.** The assumption that $K \leq 0$ allows us to use (6.5.6) and (6.5.2) to conclude that $\exp_p: T_p M \to M$ is everywhere regular (of maximal rank) and therefore is a local diffeomorphism.

**2. $\exp_p$ is surjective.** Suppose $q \in M$. Consider a curve $b = b(s)$, $s_0 \leq s \leq s_1$, joining $p$ to $q$. We may lift this curve to $T_p M$, via the inverse of $\exp_p$ on a neighborhood of $p$, to obtain a curve $\tilde{b}$ in $T_p M$ starting at $0 \in T_p M$. By the homotopy lifting property of the local diffeomorphism $\exp_p$, the lift can be extended along the entire curve $b(s)$, yielding a point $\tilde{q} \in T_p M$ such that $\exp_p(\tilde{q}) = q$. Hence $\exp_p$ is surjective.

**3. $\exp_p$ is injective.** Suppose $\exp_p(v_1) = \exp_p(v_2) = q$ with $v_1 \neq v_2$. Then the radial geodesics $t \mapsto \exp_p(t v_1)$ and $t \mapsto \exp_p(t v_2)$ are two distinct geodesics from $p$ to $q$. Since $M$ is simply connected, these two geodesics are homotopic with fixed endpoints. But the Homotopy Geodesic Length Lemma (with $K_1 = 0$, so $2\pi/\sqrt{K_1} = +\infty$) implies that two distinct geodesics from $p$ to $q$ cannot be homotopic — a contradiction. Therefore $\exp_p$ is injective.

**4.** Since $\exp_p$ is a bijective local diffeomorphism, it is a global diffeomorphism. Thus $M$ is diffeomorphic to $T_p M \cong \mathbb{R}^2$.

**5. Uniqueness of minimal geodesics.** Any geodesic joining $p$ to $q$ corresponds under $\exp_p^{-1}$ to a straight line segment in $T_p M$ from $0$ to $\exp_p^{-1}(q)$. Since straight lines in $\mathbb{R}^2$ are unique, there is exactly one such geodesic. By the homotopy lemma, this geodesic is length-minimizing among all curves joining $p$ and $q$, hence it is the unique minimal geodesic.

**Remarks.** 
1. The theorem holds under the slightly weaker condition that there are no geodesic segments with conjugate points on $M$ (cf. (6.8.4)).
2. The last statement sharpens the Hopf–Rinow result (6.4.6); this is proved without using (6.4.6).
3. The injectivity of $\exp_p$ also follows from (6.3.3 (iv)).
