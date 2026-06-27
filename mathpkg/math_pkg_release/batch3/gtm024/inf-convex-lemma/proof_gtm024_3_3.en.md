---
role: proof
locale: en
of_concept: inf-convex-lemma
source_book: gtm024
source_chapter: "§3"
source_section: "3.B"
---

Given $x, y$ and $\varepsilon > 0$, choose $(x, t_x), (y, t_y) \in K$ with $t_x < f(x) + \varepsilon$, $t_y < f(y) + \varepsilon$. By convexity of $K$, $(\alpha x + (1-\alpha)y, \alpha t_x + (1-\alpha)t_y) \in K$, so $f(\alpha x + (1-\alpha)y) \leqslant \alpha f(x) + (1-\alpha)f(y) + \varepsilon$. Let $\varepsilon \to 0$.