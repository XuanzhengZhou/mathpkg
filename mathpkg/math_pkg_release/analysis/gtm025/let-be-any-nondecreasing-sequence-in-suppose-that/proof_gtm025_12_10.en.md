---
role: proof
locale: en
of_concept: "let-be-any-nondecreasing-sequence-in-suppose-that"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.10"
---

The theorem is trivial if $\mu(X) = 0$, and so we suppose throughout that $0 < \mu(X) \leq \infty$. Let $h = \gamma_1 \xi_{E_1} + \gamma_2 \xi_{E_2} + \cdots + \gamma_m \xi_{E_m}$, where the $E_k$'s are pairwise disjoint, $X = \bigcup_{k=1}^{m} E_k$, and $0 \leq \gamma_1 < \gamma_2 < \cdots < \gamma_m \leq \infty$. Suppose that $\gamma_1 = 0$; then by (12.9) we have $L(h) = L_{E_1}'(h)$. Supposing that the theorem is established for the case $\gamma_1 > 0$ and letting $E_1'$ take the role of $X$, we have

$$L(h) = L_{E_1}'(h) \leq \lim_{n \to \infty} L_{E_1}'(g_n) \leq

$L(h \xi_{S_n}) + \gamma_m \mu(S'_n)$. Hence

$$L(g_n) \geq L(h) - \gamma_m \mu(S'_n) - \varepsilon \mu(S_n)$$
$$\geq L(h) - \gamma_m \mu(S'_n) - \varepsilon \mu(X)$$
$$\geq L(h) - \gamma_m \mu(S'_n) - \frac{1}{2} \delta.$$

If $n$ is so large that $\gamma_m \mu(S'_n) < \frac{\delta}{2}$, then we have $L(g_n) > L(h) - \delta$. The inequality $\lim_{n \to \infty} L(g_n) \geq L(h)$ follows, as $\delta$ is arbitrary.

Case (II): $\gamma_m$ is finite and $\mu(X) = \infty$. We plainly have $L(h) \geq \gamma_1 \mu(X) = \infty$. Let $\varepsilon$ be any number such that $0 < \varepsilon < \gamma_1$, and define $S_n$ for $n \in N$ just as in Case (I). For $x \in S_n$, we have $g_n(x) > h(x) - \varepsilon \geq \gamma_1 - \varepsilon$. Therefore the relations $L(g_n) \geq L(g_n \xi_{S_n}) \geq L((\gamma_1 - \varepsilon) \xi_{S_n}) = (\gamma_1 - \varepsilon) \mu(S_n)$ obtain, and (10.13) implies that

$$\lim_{n \to \infty} L(g_n) \geq (\gamma_1 - \varepsilon) \lim_{n \to \infty} \mu(S_n) = (\gamma_1 - \varepsilon) (\infty) = \infty = L(h).$$

Case (III): $\mu(E_m)$ is positive and $\gamma_m = \infty$. Here we have $L(h) \geq \gamma_m \mu(E_m) = \infty$. Choose any real number $\gamma > \gamma_{m-1}$, and let $h_\gamma = \gamma_1 \xi_{E_1} + \cd
