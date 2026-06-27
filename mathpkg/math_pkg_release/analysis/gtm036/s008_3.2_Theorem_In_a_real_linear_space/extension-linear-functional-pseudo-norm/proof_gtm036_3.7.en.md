---
role: proof
locale: en
of_concept: extension-linear-functional-pseudo-norm
source_book: gtm036
source_chapter: "3"
source_section: "3.7"
---

Let $A = \{x \in E : p(x) \leq 1\}$. Since $p$ is a pseudo-norm, $A$ is a convex circled set which is radial at $0$. The condition $|f(x)| \leq p(x)$ for $x \in F$ implies that $|f(x)| \leq 1$ for $x \in A \cap F$. By Corollary 3.6, there exists a linear functional $\overline{f}$ on $E$ extending $f$ such that $|\overline{f}(x)| \leq 1$ for all $x \in A$. For arbitrary $x \in E$, if $p(x) = 0$ then $nx \in A$ for all $n$, so $|\overline{f}(x)| \leq 1/n$ for all $n$, giving $\overline{f}(x) = 0 = p(x)$. If $p(x) > 0$, then $x/p(x) \in A$, so $|\overline{f}(x/p(x))| \leq 1$, hence $|\overline{f}(x)| \leq p(x)$. Thus the extension satisfies the required domination.
