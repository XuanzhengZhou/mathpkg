---
role: proof
locale: en
of_concept: zero-sets-closed-under-countable-intersection
source_book: gtm043
source_chapter: "1"
source_section: "1.14"
---

Given $f_n \in C(X)$, define $g_n = |f_n| \wedge 2^{-n}$, and let
$$g(x) = \sum_{n \in \mathbb{N}} g_n(x) \quad (x \in X).$$
Since $|g_n| \leq 2^{-n}$, the series converges uniformly, and therefore $g$ is a continuous function on $X$. Clearly,
$$Z(g) = \bigcap_{n \in \mathbb{N}} Z(g_n) = \bigcap_{n \in \mathbb{N}} Z(f_n),$$
because $g(x) = 0$ iff every $g_n(x) = 0$, and $Z(g_n) = Z(f_n)$.
