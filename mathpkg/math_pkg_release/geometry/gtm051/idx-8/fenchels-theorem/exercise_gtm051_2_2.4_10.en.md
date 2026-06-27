---
role: exercise
locale: en
chapter: "2"
section: "2.4"
exercise_number: 10
---

**A proof of Fenchel's theorem.**

**i)** Prove: Let $c: I \to \mathbb{R}^n$ be a closed curve lying on the sphere $S^{n-1}(r) = \{x \in \mathbb{R}^n \mid |x| = r\}$, i.e., $|c(t)| = r$ for all $t \in [0, \omega]$. Suppose $c$ does not lie in any open hemisphere of $S^{n-1}(r)$. Then the length of $c$ is at least $2\pi r$. (A simple proof of this lemma is given by Horn.)

**ii)** Using the result from (i), prove Fenchel's theorem: For any closed curve $c: I \to \mathbb{R}^n$ ($n \geq 3$), the total curvature satisfies

$$K(c) = \int_0^L \kappa(t)\,dt \geq 2\pi.$$

*Hint for (ii):* Consider the tangent indicatrix $\tilde{c}(t) = \dot{c}(t)/|\dot{c}(t)|$ as a curve on the unit sphere $S^{n-1}(1)$. The length of $\tilde{c}$ equals the total curvature $K(c)$. If $\tilde{c}$ is contained in a closed hemisphere, show that $c$ lies in a plane, and apply the Umlaufsatz. Otherwise, apply (i) to $\tilde{c}$.
