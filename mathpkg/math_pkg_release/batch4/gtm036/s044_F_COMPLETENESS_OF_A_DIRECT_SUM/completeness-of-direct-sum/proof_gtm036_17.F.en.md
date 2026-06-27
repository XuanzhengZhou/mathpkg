---
role: proof
locale: en
of_concept: completeness-of-direct-sum
source_book: gtm036
source_chapter: "17"
source_section: "F"
---

Let $E = \sum \{E_t : t \in A\}$, each $E_t$ being complete; then $E^* = \bigwedge \{E_t^* : t \in A\}$. Let $\phi$ be a linear functional on $E^*$, weak* continuous on every equicontinuous set. By Grothendieck's completeness theorem (17.7), it suffices to show that $\phi$ is represented by a point of $E$.

**(a)** Let $I_t$ be the injection of $E_t^*$ into the product $\bigwedge \{E_t^* : t \in A\}$. Then there is a finite subset $B$ of $A$ such that $\phi \circ I_t = 0$ for each $t \in A \sim B$.

*Proof of (a):* Suppose not. Then there exist distinct $t_n \in A$ and $f_{t_n} \in E_{t_n}^*$ such that $(\phi \circ I_{t_n})(f_{t_n}) = C_n \neq 0$ for $n = 1, 2, \dots$. Consider the set $\{n I_{t_n}(f_{t_n}) / C_n : n = 1, 2, \dots\}$. This set is bounded in the product topology, hence equicontinuous. But $\phi$ evaluated on these elements is $n$, contradicting the weak* continuity of $\phi$ on equicontinuous sets.

**(b)** For each $f \in E^*$, $\phi(f) = \sum \{(\phi \circ I_t)(f_t) : t \in B\}$.

*Proof of (b):* Let $f \in E^*$. Define $g \in E^*$ by $g_t = f_t$ for $t \in B$ and $g_t = 0$ for $t \in A \sim B$. Then $(f - g)_t = 0$ for $t \in B$, so $(\phi \circ I_t)((f - g)_t) = 0$ for all $t \in B$. By (a), $(\phi \circ I_t)((f - g)_t) = 0$ also for $t \in A \sim B$. Using the weak* continuity of $\phi$ on the equicontinuous set of finite partial sums of $f - g$, one obtains $\phi(f - g) = 0$, hence $\phi(f) = \phi(g) = \sum \{(\phi \circ I_t)(f_t) : t \in B\}$.

**(c)** There is a point $x \in \sum \{E_t : t \in B\}$ with $\phi(f) = f(x)$ for all $f \in E^*$.

*Proof of (c):* For each $t \in B$, the linear functional $\phi \circ I_t$ on $E_t^*$ is weak* continuous and hence is given by evaluation at some point $x_t \in E_t$ (each $E_t$ is complete, so Grothendieck's theorem applies). Let $x = \sum_{t \in B} x_t$. Then for any $f \in E^*$, by (b), $\phi(f) = \sum_{t \in B} (\phi \circ I_t)(f_t) = \sum_{t \in B} f_t(x_t) = f(x)$.

Thus $\phi$ is evaluation at $x \in E$, and by Grothendieck's completeness theorem, $E$ is complete.
