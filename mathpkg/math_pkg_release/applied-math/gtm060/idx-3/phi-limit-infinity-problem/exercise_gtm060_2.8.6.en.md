---
role: exercise
locale: en
chapter: "2"
section: "8"
exercise_number: 6
---
Let in the situation of the previous problem $U(r) \to \infty$ as $r \to \infty$. Find $\lim_{E \to \infty} \Phi(E, M)$.

ANSWER: $\pi/2$.

Hint: The substitution $x = yx_{\max}$ reduces $\Phi$ to the form $\Phi = \int_{y_{\min}}^{1} \frac{dy}{\sqrt{2(W^*(1) - W^*(y))}}$, where $W^*(y) = (y^2/2) + (E^{-1}U(M/(y x_{\max})))$. As $E \to \infty$ we have $x_{\max} \to \infty$ and $y_{\min} \to 0$. Then $W^*(y) \to y^2/2$, and we get $\Phi \to \int_0^1 \frac{dy}{\sqrt{1 - y^2}} = \pi/2$.
