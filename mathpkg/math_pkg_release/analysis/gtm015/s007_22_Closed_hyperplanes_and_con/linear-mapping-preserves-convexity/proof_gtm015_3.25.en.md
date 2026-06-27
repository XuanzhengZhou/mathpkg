---
role: proof
locale: en
of_concept: linear-mapping-preserves-convexity
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Linear mappings preserve convexity

Let $E$ and $F$ be vector spaces over $\mathbb{K}$ and let $u: E \rightarrow F$ be a linear mapping.

(i) If $A$ is convex in $E$, and $u(x), u(y) \in u(A)$, then for $0 \le \alpha \le 1$,
$$\alpha u(x) + (1 - \alpha) u(y) = u(\alpha x + (1 - \alpha) y) \in u(A)$$
since $\alpha x + (1 - \alpha) y \in A$, so $u(A)$ is convex.

(ii) If $B$ is convex in $F$, and $x, y \in u^{-1}(B)$, then $u(x), u(y) \in B$, so for $0 \le \alpha \le 1$,
$$u(\alpha x + (1 - \alpha) y) = \alpha u(x) + (1 - \alpha) u(y) \in B,$$
hence $\alpha x + (1 - \alpha) y \in u^{-1}(B)$, so $u^{-1}(B)$ is convex.

(iii) If $S \subset E$, then $u(\operatorname{conv} S) \subset \operatorname{conv} u(S)$ by (i) applied to $A = \operatorname{conv} S$. Conversely, $u^{-1}(\operatorname{conv} u(S))$ is convex by (ii) and contains $S$, hence contains $\operatorname{conv} S$. Thus $u(\operatorname{conv} S) \subset \operatorname{conv} u(S) \subset u(u^{-1}(\operatorname{conv} u(S))) \subset u(\operatorname{conv} S)$, yielding equality.
