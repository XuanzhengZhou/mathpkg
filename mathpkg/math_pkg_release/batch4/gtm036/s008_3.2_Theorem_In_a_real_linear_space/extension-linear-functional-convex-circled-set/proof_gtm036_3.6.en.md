---
role: proof
locale: en
of_concept: extension-linear-functional-convex-circled-set
source_book: gtm036
source_chapter: "3"
source_section: "3.6"
---

If $E$ is complex, regard it as a real linear space. The Minkowski functional $p_A(x) = \inf\{t > 0 : x \in tA\}$ is a pseudo-norm (subadditive, non-negatively homogeneous) since $A$ is convex, circled, and radial at $0$. The condition $|f(x)| \leq 1$ on $A \cap F$ implies $\operatorname{Re} f(x) \leq p_A(x)$ for all $x \in F$. By the Hahn-Banach theorem (3.4), there exists a real-linear extension $g$ of $\operatorname{Re} f$ to $E$ satisfying $g(x) \leq p_A(x)$ for all $x \in E$. Define $\overline{f}$ on $E$ by $\overline{f}(x) = g(x) - i g(ix)$ (for the complex case). Then $|\overline{f}(x)| \leq p_A(x)$ for all $x$, and in particular $|\overline{f}(x)| \leq 1$ on $A$, since $p_A(x) \leq 1$ for $x \in A$.
