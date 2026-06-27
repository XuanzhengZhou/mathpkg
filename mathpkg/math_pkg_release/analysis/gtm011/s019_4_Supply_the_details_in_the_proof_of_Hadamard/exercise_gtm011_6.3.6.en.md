---
role: exercise
locale: en
chapter: "6"
section: "3"
exercise_number: "6"
---

Prove Hardy's Theorem: If $f$ is analytic on $B(0; R)$ and not constant then
\[
I(r) = \frac{1}{2\pi} \int_{0}^{2\pi} |f(re^{i\theta})| \, d\theta
\]
is strictly increasing and $\log I(r)$ is a convex function of $\log r$.

Hint: If $0 < r_1 < r < r_2$ find a continuous function $\varphi: [0, 2\pi] \to \mathbb{C}$ such that $\varphi(\theta) f(re^{i\theta}) = |f(re^{i\theta})|$ and consider the function
\[
F(z) = \int_{0}^{2\pi} f(ze^{i\theta}) \varphi(\theta) \, d\theta.
\]
(Note that $r$ is fixed, so $\varphi$ may depend on $r$.)
