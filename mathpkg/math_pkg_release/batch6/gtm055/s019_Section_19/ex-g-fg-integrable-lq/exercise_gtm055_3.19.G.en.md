---
role: exercise
locale: en
chapter: "3"
section: "19"
exercise_number: "G"
---

Let $(X, \mathbf{S}, \mu)$ be a finite measure space and suppose that $1 \leq p < +\infty$. Let $g$ be a measurable function on $X$ with the property that the product $fg$ is integrable $[\mu]$ whenever $f \in L_p(X)$. Show that $g$ must then be an element of $L_q(X)$, where, as usual, $1/p + 1/q = 1$ (if $p = 1$, then $q = +\infty$; if $p = +\infty$, then $q = 1$).

(Hint: If the function $g$ is bounded, and therefore does belong to $L_q(X)$, then the norm of the functional $f \rightarrow \int fg \, d\mu$ on $L_p(X)$ is given by $\|g\|_q$ (cf. Theorem 17.5 for the case $1 < p < +\infty$). Let $E_n = \{x \in X : |g(x)| \leq n\}$, set $g_n = g \chi_{E_n}$, and recall Example 12V.) Extend this result to a $\sigma$-finite measure space.
