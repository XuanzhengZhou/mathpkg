---
role: exercise
locale: en
chapter: "5"
section: "18"
exercise_number: 1
---

Show that if $f$ is a feasible flow, then

$$v(f) = \sum_{y \in V \atop (y, y_0) \in D} f(y, y_0) - \sum_{y \in V \atop (y_0, y) \in D} f(y_0, y).$$

Recall how a cut in a network was expressed as the sum of vertex cocycles over a subset of $V$. Classically, a cut is identified with that subset. Thus, by a "cut" we shall mean a subset $U \subseteq V$ such that $x_0 \in U \subseteq V + \{y_0\}$. The "capacity of $U$" is the number

$$k(U) = \sum_{(x, y) \in D \atop x \in U \atop y \in V + U} k(x, y).$$
