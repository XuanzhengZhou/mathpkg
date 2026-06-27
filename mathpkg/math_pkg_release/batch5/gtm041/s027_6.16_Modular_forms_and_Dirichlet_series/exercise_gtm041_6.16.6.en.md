---
role: exercise
locale: en
chapter: "6"
section: "6.16"
exercise_number: 6
---

The recursion relation $f(p^{k+1}) = f(p)f(p^k) - \alpha(p)f(p^{k-1})$ shows that $f(p^n)$ is a polynomial in $f(p)$, say
$$f(p^n) = Q_n(f(p)).$$
The sequence $\{Q_n(x)\}$ is determined by the relations
$$Q_1(x) = x, \quad Q_2(x) = x^2 - \alpha(p), \quad Q_{r+1}(x) = xQ_r(x) - \alpha(p)Q_{r-1}(x) \;\; \text{for } r \geq 2.$$

Show that
$$Q_n(2\alpha(p)^{1/2} x) = \alpha(p)^{n/2} U_n(x),$$
where $U_n(x)$ is the Chebyshev polynomial of the second kind defined by
$$U_n(\cos \theta) = \frac{\sin((n+1)\theta)}{\sin \theta}.$$
