---
role: exercise
locale: en
chapter: "IV"
section: "19"
exercise_number: 1
---

Show that if $f$ is a feasible flow in a classical network $((V, D), k, x_0, y_0)$, then

$$v(f) = \sum_{\substack{y \in V \\ (y, y_0) \in D}} f(y, y_0) - \sum_{\substack{y \in V \\ (y_0, y) \in D}} f(y_0, y).$$

That is, the value of the flow equals the net inflow at the sink $y_0$.
