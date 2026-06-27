---
role: proof
locale: en
of_concept: seminorm-closed-unit-ball-properties
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Basic properties of seminorms — balanced convex unit balls and seminorm inequality

Let $E$ be a vector space over $\mathbb{K}$ and let $p$ be a seminorm on $E$.

**(i) The sets $B = \{x : p(x) \leq 1\}$ and $U = \{x : p(x) < 1\}$ are balanced and convex.**

*Balanced:* If $x \in B$ and $|\lambda| \leq 1$, then $p(\lambda x) = |\lambda| p(x) \leq p(x) \leq 1$, so $\lambda x \in B$. Similarly for $U$.

*Convex:* If $x, y \in B$ and $0 \leq t \leq 1$, then $p(tx + (1-t)y) \leq t p(x) + (1-t) p(y) \leq t + (1-t) = 1$, so $tx + (1-t)y \in B$. Similarly for $U$.

**(ii) One has $|p(x) - p(y)| \leq p(x - y)$ for all $x, y \in E$.**

*Proof.* From the triangle inequality, $p(x) = p((x - y) + y) \leq p(x - y) + p(y)$, so $p(x) - p(y) \leq p(x - y)$. Similarly, $p(y) - p(x) \leq p(y - x) = p(x - y)$. Hence $|p(x) - p(y)| \leq p(x - y)$.
