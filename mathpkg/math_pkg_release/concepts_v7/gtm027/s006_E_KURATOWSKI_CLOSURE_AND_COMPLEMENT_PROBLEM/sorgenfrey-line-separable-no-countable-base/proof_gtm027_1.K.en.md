---
role: proof
locale: en
of_concept: sorgenfrey-line-separable-no-countable-base
source_book: gtm027
source_chapter: "1"
source_section: "K"
---

# Proof that the Sorgenfrey Line Is Separable but Has No Countable Base

**Theorem.** The space $(X, \mathfrak{J})$ (the Sorgenfrey line) is separable but $\mathfrak{J}$ has no countable base.

*Proof.*

**Separability:** The rational numbers $\mathbb{Q}$ are dense in $(X, \mathfrak{J})$. To see this, let $[a,b)$ be any nonempty basic open set. Then $a < b$, so there exists a rational $q \in \mathbb{Q}$ with $a \leq q < b$. Thus $q \in [a,b) \cap \mathbb{Q} \neq \emptyset$. Since every nonempty open set contains a basic open set, $\mathbb{Q}$ intersects every nonempty open set, and $\mathbb{Q}$ is countable. Hence $(X, \mathfrak{J})$ is separable.

**No countable base:** Suppose $\mathcal{B} = \{B_n : n \in \mathbb{N}\}$ were a countable base for $\mathfrak{J}$. For each $x \in \mathbb{R}$, the set $[x, x+1)$ is an open neighborhood of $x$. Since $\mathcal{B}$ is a base, there exists $B_{n(x)} \in \mathcal{B}$ such that $x \in B_{n(x)} \subseteq [x, x+1)$. Then $\inf B_{n(x)} = x$ (because $B_{n(x)}$ contains $x$ and is contained in $[x, x+1)$).

The map $x \mapsto n(x)$ from $\mathbb{R}$ to $\mathbb{N}$ must be injective: if $x \neq y$, then $\inf B_{n(x)} = x \neq y = \inf B_{n(y)}$, so $B_{n(x)} \neq B_{n(y)}$ and $n(x) \neq n(y)$. But this gives an injection from an uncountable set $\mathbb{R}$ into a countable set $\mathbb{N}$ — contradiction. Therefore no countable base exists. $\square$
