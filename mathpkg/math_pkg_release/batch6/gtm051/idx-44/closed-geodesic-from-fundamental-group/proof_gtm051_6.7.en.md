---
role: proof
locale: en
of_concept: closed-geodesic-from-fundamental-group
source_book: gtm051
source_chapter: "6"
source_section: "6.7"
---

**Proof.** (i) The fact that $\gamma$ operates as a fixed-point free isometry is established in the preceding Lemma.

(ii) Consider the function $f(\tilde{p}) = \tilde{d}(\tilde{p}, \gamma \tilde{p})$ on $\tilde{M}$. We have the estimate:

$$\tilde{d}(\tilde{p}, \gamma \tilde{p}) \leq \tilde{d}(\tilde{p}, \tilde{q}) + \tilde{d}(\tilde{q}, \gamma \tilde{q}) + \tilde{d}(\gamma \tilde{q}, \gamma \tilde{p}) = \tilde{d}(\tilde{q}, \gamma \tilde{q}) + 2\tilde{d}(\tilde{p}, \tilde{q}),$$

which shows that $f$ is a continuous function. Let $\{\tilde{p}_n\}$ be a sequence on $\tilde{M}$ such that $\lim_n f(\tilde{p}_n) = \omega = \inf f$. Fix $\tilde{p}_0 \in \tilde{M}$, and let $d/2$ be the diameter of $M$ (the maximum distance $d(p, q)$ between two points in $M$). Then, for every $n \geq 1$, there exists a $\gamma_n \in \Gamma$ such that $\tilde{d}(\gamma_n \tilde{p}_n, \tilde{p}_0) < d$. Therefore the sequence $\{\gamma_n \tilde{p}_n\}$ lies in a compact set, and we may assume it converges to some point $\tilde{q}$. By continuity of $f$ and the fact that $f$ is $\Gamma$-invariant (since $\Gamma$ acts by isometries), $f(\tilde{q}) = \omega$. Let $\tilde{c}(t)$ be the unit-speed geodesic from $\tilde{q}$ to $\gamma \tilde{q}$ with $\tilde{c}(0) = \tilde{q}$ and $\tilde{c}(\omega) = \gamma \tilde{q}$. By the first variation formula and the minimizing property of $f$ at $\tilde{q}$, we obtain that $\gamma \circ \tilde{c}(t) = \tilde{c}(t + \omega)$ for all $t$. The projection $c = \pi \circ \tilde{c}$ is then a closed geodesic in $M$ of length $\omega$.

(iii) Suppose $K < 0$. To prove (iii), it suffices to show that if $\tilde{c}(t)$ and $\tilde{c}'(t)$, $t \in \mathbb{R}$, are $\gamma$-invariant geodesics in $\tilde{M}$, i.e.,

$$\gamma \tilde{c}(t) = \tilde{c}(t + \omega); \quad \gamma \tilde{c}'(t) = \tilde{c}'(t + \omega'),$$

then $\tilde{c}'(t) = \tilde{c}(t + t_0)$ for some fixed $t_0$.

To see this, consider the geodesic quadrilateral with vertices $\tilde{c}(0), \tilde{c}(\omega), \tilde{c}'(\omega')$, and $\tilde{c}'(0)$. By the properties of geodesics in a Riemannian manifold, this figure is uniquely defined. If this quadrilateral were nondegenerate, the sum of the interior angles at the vertices would be $2\pi$. This is because $\gamma$ is an isometry which maps the edge $\tilde{c}(0)\tilde{c}'(0)$ into the edge $\tilde{c}(\omega)\tilde{c}'(\omega')$ and maps the geodesics $\tilde{c}$ and $\tilde{c}'$ into themselves. But by the Gauss-Bonnet theorem (Corollary 6.3.3 (ii)), the sum of the interior angles of a geodesic quadrilateral must be $< 2\pi$ when $K < 0$. Therefore the quadrilateral is degenerate, which means there must exist a $t_0 \in \mathbb{R}$ with $\tilde{c}'(t) = \tilde{c}(t + t_0)$ for all $t$.

(iv) Suppose $\gamma$ and $\gamma'$ are nontrivial commuting elements in $\Gamma$. Let $\tilde{c}(t)$, $t \in \mathbb{R}$, and $\tilde{c}'(t)$, $t \in \mathbb{R}$, be the corresponding invariant geodesics in $\tilde{M}$. By (iii), they are unique up to choice of initial points. Since $\gamma\gamma' = \gamma'\gamma$, we have

$$\gamma(\gamma' \tilde{c}(t)) = \gamma'(\gamma \tilde{c}(t)) = \gamma' \tilde{c}(t + \omega).$$

Thus $\gamma' \circ \tilde{c}$ is also a $\gamma$-invariant geodesic. By the uniqueness result (iii), $\gamma' \tilde{c}$ and $\tilde{c}$ differ only by a parameter translation, which implies that the corresponding $\gamma'$-invariant geodesic $\tilde{c}'$ coincides with $\tilde{c}$ up to a parameter translation.
