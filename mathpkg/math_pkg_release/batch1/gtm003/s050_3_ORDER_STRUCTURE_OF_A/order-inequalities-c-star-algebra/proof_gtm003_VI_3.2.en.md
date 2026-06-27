---
role: proof
locale: en
of_concept: order-inequalities-c-star-algebra
source_book: gtm003
source_chapter: "VI"
source_section: "3.2"
---

(i) By (3.1) there exists $d \in A$ such that $0 \leq y - x = d^*d$. Thus $c^*(y - x)c = c^*d^*dc = (dc)^*dc \geq 0$, whence the first assertion follows. For the second, observe that $\sigma(\|y^*y\|e - y^*y) \subset \mathbb{R}_+$ implies $0 \leq y^*y \leq \|y\|^2e$, so the claim follows.

(ii) follows from $\|x\|^2 = \|x^*x\| = \||x|^2\| = \||x|\|^2$ and the norm estimate from (i).

(iii) By the continuous functional calculus, the square root function $t \mapsto \sqrt{t}$ is operator monotone on $\mathbb{R}_+$, so the inequality $0 \leq x \leq y$ implies $0 \leq \sqrt{x} \leq \sqrt{y}$.

(iv) From $0 < x \leq y$ we have $y^{-1/2} x y^{-1/2} \leq e$, which implies $\|y^{-1/2} x^{1/2}\| \leq 1$. Hence $x^{1/2} y^{-1} x^{1/2} \leq e$, giving $y^{-1} \leq x^{-1}$. Since $x$ is invertible and positive, $0 < y^{-1}$ follows from $x \leq y$.
