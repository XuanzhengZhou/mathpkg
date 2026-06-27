---
role: proof
locale: en
of_concept: "existence-of-pure-states-separating-points"
source_book: gtm039
source_chapter: "1"
source_section: "1.7"
---
Fix $x = x^*$. Let $\Sigma = \{g \in \text{states}: |g(x)| = \|x\|\}$. $\Sigma$ is weak$^*$-compact, convex, and nonempty (Hahn–Banach). By Krein–Milman, $\Sigma$ has an extreme point $g$. If $g = tg_1+(1-t)g_2$ with states $g_i$, then $|g_i(x)| \leqslant \|x\| = |g(x)|$ forces $g_i(x) = g(x)$, so $g_i \in \Sigma$ and $g_1 = g_2 = g$. Thus $g$ is pure. For any $z$, apply this to $x = z^*z$ to get a pure state $f$ with $f(z^*z) = \|z\|^2$. $\square$
