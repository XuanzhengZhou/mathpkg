---
role: proof
locale: en
of_concept: bounded-functional-countably-additive-measure
source_book: gtm036
source_chapter: "19"
source_section: "19.8"
---

Since $m$ is evidently finitely additive, it suffices to prove countable additivity. Let $C_n$ be an increasing sequence of subsets of $A$ such that $g_*C_n = 0$ (i.e., $m(C_n) = 0$), and let $C$ be the union of the sets $C_n$. We must show $g_*C = 0$, which gives $m(C) = 0$.

Suppose, for contradiction, that $g_*C(x) \neq 0$ for some $x$. Define $y_n$ by $y_n(t) = n x(t)$ for $t \in C \setminus C_n$ and $y_n(t) = 0$ otherwise. Then:
$$g(y_n) = g_*C_n(y_n) + g_*(C \setminus C_n)(y_n) = g_*(C \setminus C_n)(y_n) = n g_*(C \setminus C_n)(x) = n g_*C(x).$$

This yields $|g(y_n)| = n |g_*C(x)| \to \infty$, which contradicts the hypothesis that $g$ is bounded, because the sequence $\{y_n\}$ is bounded in the product (its projection on each coordinate space is bounded by construction). Hence $g_*C = 0$, and $m$ is countably additive.
