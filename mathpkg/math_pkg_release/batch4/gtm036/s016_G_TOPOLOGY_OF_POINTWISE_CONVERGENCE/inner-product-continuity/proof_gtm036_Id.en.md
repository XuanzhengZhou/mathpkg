---
role: proof
locale: en
of_concept: inner-product-continuity
source_book: gtm036
source_chapter: "I"
source_section: "I(d)"
---

Let $(x_0, y_0) \in E \times E$ and $\varepsilon > 0$. For any $(x,y)$,
$$
\begin{aligned}
|(x,y) - (x_0,y_0)| &= |(x,y) - (x,y_0) + (x,y_0) - (x_0,y_0)| \\
&\leq |(x, y - y_0)| + |(x - x_0, y_0)| \\
&\leq \|x\| \|y - y_0\| + \|x - x_0\| \|y_0\| \quad \text{(by CBS)}.
\end{aligned}
$$

Choose $\delta > 0$ such that if $\|x - x_0\| < \delta$ and $\|y - y_0\| < \delta$, then $\|x\| \leq \|x_0\| + \delta$ and $(\|x_0\| + \delta)\delta + \delta \|y_0\| < \varepsilon$. Then $|(x,y) - (x_0,y_0)| < \varepsilon$, proving joint continuity.
