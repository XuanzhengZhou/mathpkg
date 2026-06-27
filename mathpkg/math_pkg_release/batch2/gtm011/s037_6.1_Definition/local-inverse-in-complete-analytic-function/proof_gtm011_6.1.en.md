---
role: proof
locale: en
of_concept: local-inverse-in-complete-analytic-function
source_book: gtm011
source_chapter: "6"
source_section: "6.1"
---

Fix $[g]_a$ in $\mathcal{F}$ (so $(a, [g]_a) \in \mathcal{R}$); then, by hypothesis, $g(a) = \mathcal{F}(a, [g]_a) \in G$. If $b = f(g(a))$ then there is a disk $B$ about $b$ and an analytic function $h: B \to \mathbb{C}$ such that $h(b) = g(a)$ and $f(h(z)) = z$ for all $z$ in $B$. From Proposition 6.18, $[h]_b \in \mathcal{F}$. Also $a = \rho(a, [g]_a) \in \rho(\mathcal{R}) = f(G)$. According to Theorem 5.11 there is a path $\gamma$ in $f(G)$ from $a$ to $b$ such that $[h]_b$ is the continuation along $\gamma$ of $[g]_a$. Let $\{(g_t, D_t)\}$ be a continuation along $\gamma$ with each $D_t$ a disk such that $[g_0]_a = [g]_a$ and $[g_1]_b = [h]_b$. Since $f(h(z)) = z$, the function element $g$ near $a$ satisfies $f(g(z)) = z$ as required.
