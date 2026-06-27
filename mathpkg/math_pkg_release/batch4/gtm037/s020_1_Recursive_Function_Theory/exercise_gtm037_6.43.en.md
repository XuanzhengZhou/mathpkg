---
role: exercise
locale: en
chapter: "6"
section: "Recursive Function Theory"
exercise_number: 6.43
---

Show that there exist recursive functions $h, k$ such that

$$h(0) = \mu i\,(g(i) > 3f(i));$$
$$k(0) = \mu i\,(g(i) > 3f(i) \text{ and } g(i) \neq g(h(0)));$$
$$h(n + 1) = \mu i\,(g(i) > 3f(i) \text{ and } \forall j \leq n\,(g(i) \neq g(k(j))) \text{ and}$$
$$\qquad \forall j \leq n\,(f(i) \neq f(h(j))) \text{ and } \forall j \leq n\,(g(i) \neq g(h(j))));$$
$$k(n + 1) = \mu i\,(g(i) > 3f(i) \text{ and } \forall j \leq n + 1\,(g(i) \neq g(h(j))) \text{ and}$$
$$\qquad \forall j \leq n\,(f(i) \neq f(k(j))) \text{ and } \forall j \leq n\,(g(i) \neq g(k(j)))).$$

Let $A = \operatorname{Rng}(g \circ h)$, $B = \operatorname{Rng}(g \circ k)$.
