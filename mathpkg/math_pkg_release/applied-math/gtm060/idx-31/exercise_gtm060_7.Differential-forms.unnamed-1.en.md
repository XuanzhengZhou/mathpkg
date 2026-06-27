---
role: exercise
locale: en
chapter: "7"
section: "Differential forms"
exercise_number: "unnamed-1"
---

Show that every closed differential $k$-form on a vector space $\mathbb{R}^n$ is an exterior derivative of some $(k-1)$-form.

*Hint.* Use the cone construction. Let $\omega^k$ be a differential $k$-form on $\mathbb{R}^n$. Define a $(k-1)$-form $p\omega^k$ (the "co-cone over $\omega$") by the relation: for any chain $c_{k-1}$,
$$\int_{c_{k-1}} p\omega^k = \int_{p c_{k-1}} \omega^k.$$
Its explicit value on tangent vectors $\xi_1, \ldots, \xi_{k-1}$ at $x$ is
$$(p\omega)_{\mathbf{x}}(\xi_1, \ldots, \xi_{k-1}) = \int_0^1 \omega_{t\mathbf{x}}(\mathbf{x}, t\xi_1, \ldots, t\xi_{k-1})\, dt.$$
Verify that $d \circ p + p \circ d = \text{id}$, and conclude that if $\omega^k$ is closed, then $d(p\omega^k) = \omega^k$.
