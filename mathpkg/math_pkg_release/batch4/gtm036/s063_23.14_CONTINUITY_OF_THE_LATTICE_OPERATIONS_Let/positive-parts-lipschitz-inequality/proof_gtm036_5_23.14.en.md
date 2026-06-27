---
role: proof
locale: en
of_concept: positive-parts-lipschitz-inequality
source_book: gtm036
source_chapter: "5"
source_section: "23.14"
---

For arbitrary $u$ and $v$ in a vector lattice $E$, the inequality $(u+v)^+ \leq u^+ + v^+$ is obvious from the definition of the positive part. Setting $u = x - y$ and $v = y$, we obtain

$$x^+ = ((x-y)+y)^+ \leq (x-y)^+ + y^+,$$

hence $x^+ - y^+ \leq (x-y)^+$. Since the right-hand side is non-negative, taking the positive part yields

$$(x^+ - y^+)^+ \leq (x-y)^+.$$

By interchanging the roles of $x$ and $y$, we obtain the symmetric inequality

$$(x^+ - y^+)^- = (y^+ - x^+)^+ \leq (y-x)^+ = (x-y)^-.$$

Adding the two inequalities gives

$$|x^+ - y^+| = (x^+ - y^+)^+ + (x^+ - y^+)^- \leq (x-y)^+ + (x-y)^- = |x-y|.$$

Thus $|x^+ - y^+| \leq |x-y|$ for all $x, y \in E$.
