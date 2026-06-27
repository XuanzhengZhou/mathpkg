---
role: proof
locale: en
of_concept: sorgenfrey-line-subspace-lindelof
source_book: gtm027
source_chapter: "1"
source_section: "K"
---

# Proof that Every Subspace of the Sorgenfrey Line Is Lindelöf

**Theorem.** Each subspace of $(X, \mathfrak{J})$ (the Sorgenfrey line) is a Lindelöf space.

*Proof.* We show that $(X, \mathfrak{J})$ itself is hereditarily Lindelöf; i.e., every open cover of any subspace has a countable subcover. Equivalently, every family of basic open sets has a countable subfamily with the same union.

Let $\mathcal{U} = \{[a_\alpha, b_\alpha) : \alpha \in I\}$ be a collection of basic open sets. We need to show that the union can be covered by countably many of these intervals.

Consider the corresponding family of open intervals in the usual topology: $\mathcal{V} = \{(a_\alpha, b_\alpha) : \alpha \in I\}$. The union $V = \bigcup_{\alpha \in I} (a_\alpha, b_\alpha)$ is open in the usual topology of $\mathbb{R}$, which is second countable (hence hereditarily Lindelöf). So there exists a countable subfamily $\mathcal{V}' \subseteq \mathcal{V}$ with the same union.

Now, what points of $\bigcup \mathcal{U}$ are not covered by $\bigcup \mathcal{V}'$? Only those points $a_\alpha$ that are left endpoints of intervals in $\mathcal{U}$ but are not interior to any $(a_\beta, b_\beta)$. There can be at most countably many such "isolated" left endpoints because they form a discrete set in the Sorgenfrey line (each such point $x$ has a neighborhood $[x, x+\varepsilon)$ that contains no other such point). A discrete subset of a hereditarily Lindelöf space is countable.

Thus we can add countably many more intervals from $\mathcal{U}$ to cover these remaining points, obtaining a countable subcover. $\square$
