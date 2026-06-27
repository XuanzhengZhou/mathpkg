---
role: proof
locale: en
of_concept: idempotents-and-supplementary-subspaces
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Idempotent Linear Maps Yield Supplementary Subspaces

Let $E$ be a vector space over $\mathbb{K}$ and let $p: E \to E$ be an idempotent linear map, i.e., $p^2 = p$ (equivalently, $p \circ p = p$).

Set $M = \operatorname{Im}(p)$ and $N = \operatorname{Ker}(p)$. We prove that $M$ and $N$ are supplementary linear subspaces of $E$.

First, any $x \in E$ can be decomposed as

$$x = p(x) + (x - p(x)).$$

Clearly $p(x) \in \operatorname{Im}(p) = M$. Moreover,

$$p(x - p(x)) = p(x) - p^2(x) = p(x) - p(x) = \theta,$$

so $x - p(x) \in \operatorname{Ker}(p) = N$. Thus $E = M + N$.

Second, suppose $x \in M \cap N$. Since $x \in M = \operatorname{Im}(p)$, there exists $y \in E$ such that $x = p(y)$. Since $x \in N = \operatorname{Ker}(p)$, we have $p(x) = \theta$. But

$$\theta = p(x) = p(p(y)) = p^2(y) = p(y) = x,$$

hence $x = \theta$. Therefore $M \cap N = \{\theta\}$.

We have shown $E = M + N$ and $M \cap N = \{\theta\}$, i.e., $M$ and $N$ are supplementary subspaces. Moreover, the projector associated with this decomposition (the projection onto $M$ along $N$) is precisely $p$, since for $x = y + z$ with $y \in M$, $z \in N$, we have $p(x) = p(y + z) = p(y) + p(z) = p(y) + \theta$. Writing $y = p(w)$ for some $w$, we get $p(y) = p^2(w) = p(w) = y$, so $p(x) = y$. $\square$
