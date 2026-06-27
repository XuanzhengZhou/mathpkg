---
role: proof
locale: en
of_concept: monotone-approximation-by-simple-functions
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

The theorem is trivial if $\mu(X) = 0$, so suppose $0 < \mu(X) \leq \infty$. Write $h = \sum_{k=1}^m \gamma_k \xi_{E_k}$ with $0 \leq \gamma_1 < \gamma_2 < \cdots < \gamma_m \leq \infty$, the $E_k$'s pairwise disjoint and $X = \bigcup E_k$. If $\gamma_1 = 0$, reduce to the case $\gamma_1 > 0$ by (12.9).\n\nCase (I): $\gamma_m$ finite and $\mu(X) < \infty$. For $\varepsilon > 0$ with $\varepsilon < \gamma_1$, define $S_n = \{x : g_n(x) > h(x) - \varepsilon\}$. Then $S_n \uparrow X$, so $\mu(S_n') \to 0$. We have $L(g_n) \geq L(g_n \xi_{S_n}) \geq L((h - \varepsilon)\xi_{S_n}) = L(h\xi_{S_n}) - \varepsilon\mu(S_n) \geq L(h) - \gamma_m\mu(S_n') - \varepsilon\mu(X)$. For large $n$, this gives $L(g_n) > L(h) - \delta$.\n\nCase (II): $\gamma_m$ finite and $\mu(X) = \infty$. Then $L(h) = \infty$. For $0 < \varepsilon < \gamma_1$, $L(g_n) \geq (\gamma_1-\varepsilon)\mu(S_n)$ with $\mu(S_n) \to \infty$, so $\lim L(g_n) = \infty = L(h)$.\n\nCase (III): $\gamma_m = \infty$ and $\mu(E_m) > 0$. Then $L(h) = \infty$. Choose $\gamma > \gamma_{m-1}$ and replace $\gamma_m$ with $\gamma$ to define $h_\gamma$. Then $\lim L(g_n) \geq L(h_\gamma) \to \infty$ as $\gamma \to \infty$.
