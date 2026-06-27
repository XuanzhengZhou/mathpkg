---
role: exercise
locale: en
chapter: "3"
section: "Problems"
exercise_number: N
---
(Dixon [19]) Let $U$ be an open set in $\mathbb{C}$, and let $\gamma$ be a formal sum of closed rectifiable arcs in $U$ (Prob. H). Suppose given a locally analytic function $f$ on $U$ and set
$$g(\zeta, \lambda) = \begin{cases} \dfrac{f(\zeta) - f(\lambda)}{\zeta - \lambda}, & \zeta \neq \lambda, \\[8pt] f'(\lambda), & \zeta = \lambda. \end{cases}$$

Show that if $V$ denotes the (open) subset of $\mathbb{C}$ at which the winding number $w_{\gamma}$ vanishes, then
$$h(\lambda) = \begin{cases} \displaystyle \frac{1}{2\pi i} \int_{\gamma} g(\zeta, \lambda) \, d\zeta, & \lambda \in U, \\[10pt] \displaystyle \frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} \, d\zeta, & \lambda \in V, \end{cases}$$
defines a locally analytic function on $U \cup V$.

(Hint: It is obvious that the two definitions of $h$ agree on $U \cap V$, so $h$ really defines a function on $U \cup V$. Moreover it is also clear (Prob. G) that $h$ is differentiable at each point of $V$. To complete the proof, use Problems L and M and Morera's theorem (Ex. L).)
