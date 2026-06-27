---
role: proof
locale: en
of_concept: tangent-mapping-angle-function
source_book: gtm051
source_chapter: "2"
source_section: "2.1"
---

Choose a partition $a = t_0 < t_1 < \ldots < t_k = b$ fine enough to ensure that $e_1|_{[t_{j-1}, t_j]}$ lies entirely in some open semicircle of $S^1$. This is possible since $e_1$ is continuous.

Choose $\theta(a)$ satisfying $e_1(a) = (\cos \theta(a), \sin \theta(a))$. Then $\theta$ is uniquely determined on $[a, t_1] = [t_0, t_1]$ by the requirement that it be continuous.

If $\theta$ is known on $[t_0, t_{j-1}]$, it has a unique continuous extension to $[t_0, t_j]$: namely, $\theta(t_{j-1})$ is given and there is a unique continuous function $\tilde{\theta}: [t_{j-1}, t_j] \to \mathbb{R}$, with $\tilde{\theta}(t_{j-1}) = \theta(t_{j-1})$, satisfying $e_1(t) = (\cos \tilde{\theta}(t), \sin \tilde{\theta}(t))$. Using $\tilde{\theta}$, we may extend $\theta$ so that it is continuous on $[t_0, t_j]$. By this procedure, $\theta$ may be defined to be continuous on $[a, b]$.

The differentiability of $\theta|_{[t_{j-1}, t_j]}$ follows from the differentiability of $e_1$ and the inverse trigonometric functions.

To see that $\theta(b) - \theta(a)$ is independent of the choice of $\theta$, suppose $\theta_1$ and $\theta_2$ are two such functions. Then $\theta_1(t) - \theta_2(t)$ is a continuous integer-valued function on $[a, b]$, hence constant. Therefore $\theta_1(b) - \theta_1(a) = \theta_2(b) - \theta_2(a)$.
