---
role: proof
locale: en
of_concept: path-in-sheaf-iff-analytic-continuation
source_book: gtm011
source_chapter: "5"
source_section: "5.6"
---

**Proof.** Suppose that $\sigma: [0, 1] \to \mathcal{S}(G)$ is a path with $\sigma(0) = (a, [f]_a)$, $\sigma(1) = (b, [g]_b)$. Then composing with the projection map $\pi: \mathcal{S}(G) \to G$ gives a path $\gamma = \pi \circ \sigma$ in $G$ from $a$ to $b$. By definition of $\mathcal{S}(G)$, the germ $[g]_b$ is the analytic continuation of $[f]_a$ along $\gamma$.

Conversely, suppose $[g]_b$ is the analytic continuation of $[f]_a$ along a path $\gamma: [0,1] \to G$. Define $\sigma(t) = (\gamma(t), [f]_{\gamma(t)})$ where $[f]_{\gamma(t)}$ is the germ obtained by analytic continuation of $[f]_a$ along $\gamma|_{[0,t]}$. Clearly $\sigma(0) = (a, [f]_a)$ and $\sigma(1) = (b, [f]_b) = (b, [g]_b)$; if it can be shown that $\sigma$ is continuous then $\sigma$ is the desired arc.

Fix $t$ in $[0, 1]$ and let $N(g, V)$ be a neighborhood of $\sigma(t)$. Then $\gamma(t) \in V$ and $[f]_{\gamma(t)} = [g]_{\gamma(t)}$. So there is a number $r > 0$ such that $B(\gamma(t); r) \subset U \cap V$ and $f(z) = g(z)$ for $|z - \gamma(t)| < r$. Also, since $\gamma$ is continuous there is a $\delta > 0$ such that $|\gamma(s) - \gamma(t)| < r$ whenever $|s - t| < \delta$. Combining these last two facts gives that

$$(t - \delta, t + \delta) \subset \sigma^{-1}(N(g, V)).$$

It follows from Exercise 4.3 that $\sigma$ is continuous.
