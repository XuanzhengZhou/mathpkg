---
role: exercise
locale: en
chapter: "X"
section: "60"
exercise_number: 5f
---

For every Borel set $E$, prove that
$$
\mu(E^{-1}) = \int_E \frac{1}{\Delta(x)}\, d\mu(x).
$$
(Hint: by the uniqueness theorem for right invariant measures, $\mu(E^{-1}) = c \int_E \frac{1}{\Delta(x)}\, d\mu(x)$ for some positive finite constant $c$. This implies that $\int f(x^{-1})\, d\mu(x) = c \cdot \int \frac{f(x)}{\Delta(x)}\, d\mu(x)$ for every integrable function $f$. Replacing $f(x)$ by $f(x^{-1})$, writing $g(x^{-1}) = f(x^{-1})/\Delta(x)$, and applying the last written equation to $g$ in place of $f$, yields the result that
$$
\frac{1}{c} \int g(x^{-1})\, d\mu(x) = c \cdot \int g(x^{-1})\, d\mu(x),
$$
from which $c = 1$ follows.)
