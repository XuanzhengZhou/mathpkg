---
role: proof
locale: en
of_concept: riesz-representation-hilbert-space
source_book: gtm036
source_chapter: "4"
source_section: "L (Hilbert Spaces II)"
---
Given $f \neq 0$, let $N = \{x : f(x) = 0\}$ be the null space of $f$. Since $f$ is continuous, $N$ is a closed proper subspace of $H$. Choose $z \in N^\perp$ with $z \neq 0$. Then $f(z) \neq 0$, and for any $x \in H$, consider
$$x - \frac{f(x)}{f(z)} z.$$
This element belongs to $N$ because $f\left(x - \frac{f(x)}{f(z)} z\right) = f(x) - f(x) = 0$. Since $z \in N^\perp$, we have
$$\left(x - \frac{f(x)}{f(z)} z, z\right) = 0,$$
which gives $(x, z) = \frac{f(x)}{f(z)} \|z\|^2$, so
$$f(x) = \left(x, \frac{\overline{f(z)}}{\|z\|^2} z\right).$$
Setting $y = \frac{\overline{f(z)}}{\|z\|^2} z$ yields $f(x) = (x, y)$ for all $x \in H$. The mapping $f \mapsto y$ is conjugate-linear and isometric since $\|f\| = \|y\|$.
