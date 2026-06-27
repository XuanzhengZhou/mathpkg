---
role: proof
locale: en
of_concept: convex-functional-equivalence
source_book: gtm036
source_chapter: "3"
source_section: "E CONVEX FUNCTIONALS"
---

The text states the equivalence without explicit proof. The reasoning is as follows.

\textbf{(i)+(ii) $\Rightarrow$ (iii):} If $p$ is non-negatively homogeneous and subadditive, then for any finite combination with $a_i \geq 0$ and $\sum a_i = 1$,
$$
p\left(\sum a_i x_i\right) \leq \sum p(a_i x_i) = \sum a_i p(x_i),
$$
using subadditivity then non-negative homogeneity, establishing convexity.

\textbf{(ii)+(iii) $\Rightarrow$ (i):} If $p$ is convex and subadditive, then for any $\lambda \geq 0$ and $x \in E$, applying convexity with weights $(1-\lambda)$ and $\lambda$ at $0$ and $x$ yields $p(\lambda x) = \lambda p(x)$ (non-negative homogeneity).

\textbf{(i)+(iii) $\Rightarrow$ (ii):} If $p$ is non-negatively homogeneous and convex, then
$$
p(x+y) = 2 \cdot p\left(\frac{x+y}{2}\right) \leq 2 \cdot \frac{p(x)+p(y)}{2} = p(x) + p(y),
$$
establishing subadditivity.
