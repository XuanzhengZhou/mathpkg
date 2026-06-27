---
role: proof
locale: en
of_concept: continuous-linear-form-existence
source_book: gtm003
source_chapter: "II"
source_section: "3"
---

If $f \neq 0$ is a continuous linear form on $L$, the subset $A = \{x : |f(x)| < 1\}$ is not equal to $L$, convex, and open.

Conversely, suppose the convex set $A \subset L$ is open and $A \neq L$. Pick $x_0 \notin A$. By Mazur's theorem (Theorem 3.1), there exists a closed hyperplane $H$ containing $x_0$ and not intersecting $A$. Translate so that $H$ passes through $0$, making $H$ a closed hyperplane subspace. Then by the characterization of closed hyperplanes (Chapter I, Proposition 4.2), there exists a non-zero continuous linear form $f$ on $L$ whose kernel is $H$. Since $H$ does not intersect $A - x_0$, we have $f \neq 0$.
