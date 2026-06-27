---
role: proof
locale: en
of_concept: maximum-principle-corollary-bounded
source_book: gtm011
source_chapter: "X"
source_section: "1.9"
---

First take $w = u$ and $v = 0$ in Theorem 1.7. The hypothesis that $w(z) = 0$ on $\partial G$ gives $\limsup_{z \to a} w(z) = 0 \leq \liminf_{z \to a} 0$ for each $a \in \partial_\infty G$. Hence Theorem 1.7 yields either $w(z) < 0$ for all $z \in G$ or $w \equiv 0$.

Now take $w = v$ and $u = 0$ in Theorem 1.7. The same boundary condition gives $0 = \limsup_{z \to a} 0 \leq \liminf_{z \to a} w(z)$, so either $0 < w(z)$ for all $z \in G$ or $w \equiv 0$.

Since both conclusions hold simultaneously, we must have $w \equiv 0$ on $G$.
