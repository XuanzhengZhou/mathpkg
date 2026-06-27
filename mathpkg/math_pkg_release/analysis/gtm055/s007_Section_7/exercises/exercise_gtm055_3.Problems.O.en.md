---
role: exercise
locale: en
chapter: "3"
section: "Problems"
exercise_number: O
---
(The Cauchy-Goursat Theorem and Cauchy Integral Formula: The General Case)

(i) Let $U$ be an open set in $\mathbb{C}$, let $f$ be a locally analytic function on $U$, and let $\gamma$ be a formal sum of closed rectifiable arcs in $U$ with the property that if $\lambda \notin U$ then $w_{\gamma}(\lambda) = 0$. (This condition says, intuitively, that $\gamma$ does not wind around any point of the complement of $U$, and is frequently indicated by writing $\gamma \sim 0$ in $U$.) Show that
$$w_{\gamma}(\lambda) f(\lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} \, d\zeta$$
for every $\lambda \in U \setminus \{\text{range of } \gamma\}$, and consequently that
$$\int_{\gamma} f(\zeta) \, d\zeta = 0.$$
